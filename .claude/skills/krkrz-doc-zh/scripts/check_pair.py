#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
krkrz_dev 文档成对检查：doc/ 日文原文 ↔ doc/zh/ 中文译文。

用法（仓库根或任意子目录执行）:
  python3 check_pair.py --all                    # 检查所有已存在的译文对
  python3 check_pair.py --untranslated           # 列出还没有译文的日文文件
  python3 check_pair.py doc/guide/Startup.md ...  # 只检查指定文件（可给日文或译文路径）

选项:
  --root DIR       仓库根（默认：从 cwd / 给定路径向上找 mkdocs.yml）
  --fail-on-warn   WARNING 也返回非 0（CI 严格模式）
  --quiet          只输出问题与汇总

检查项:
  [E] 代码块（``` 围栏）内容不一致 —— 必须逐行一致（不含行尾空白）
  [E] 标题层级序列不一致 —— 漏译 / 多译小节
  [E] 相对链接 / 图片目标不存在 —— 译文树与日文树里都找不到（等价于 mkdocs 的解析规则）
  [W] 中文文件里残留平假名 / 片假名（代码与行内代码除外；引用日文原文时可保留）
  [W] 锚点找不到对应标题（按 MkDocs 默认 slugify 推算，供参考）
  [W] frontmatter 键不一致
  [W] 代码块的语言标记不同

退出码: 有 ERROR（或 --fail-on-warn 下有 WARNING）→ 1，否则 0。
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

KANA_RE = re.compile(r"[\u3041-\u3096\u30A1-\u30FA\u30FC\u309D-\u309E\u30FD-\u30FE]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_OPEN_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
LINK_RE = re.compile(
    r"(!?)\[([^\]]*)\]\(\s*(?P<url><[^>\s]+>|[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)"
)
REFDEF_RE = re.compile(r"^\[([^\]]+)\]:\s*(\S+)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
ATTR_ID_RE = re.compile(r"\{\s*:?\s*#([^\s#}]+)\s*\}")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "ftp://", "//")
EXCLUDE_TOP_DIRS = {"zh", "_assets"}
EXCLUDE_NAMES = {"_missing.md", "_inventory.json"}

# ---------------------------------------------------------------------------
# 解析
# ---------------------------------------------------------------------------


def parse_document(text: str) -> dict:
    """把 markdown 拆成围栏 / 标题 / 链接 / 假名行等结构。"""
    fences: list[dict] = []
    headings: list[dict] = []
    links: list[dict] = []
    refdefs: list[dict] = []
    kana: list[tuple[int, str]] = []

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        m = FENCE_OPEN_RE.match(line)
        if m:
            char, count = m.group(2)[0], len(m.group(2))
            info = m.group(3).strip()
            body: list[str] = []
            start = i + 1  # 1-based，围栏行
            i += 1
            while i < len(lines) and not re.match(
                r"^\s*%s{%d,}\s*$" % (re.escape(char), count), lines[i]
            ):
                body.append(lines[i])
                i += 1
            fences.append({"info": info, "body": body, "start": start})
            i += 1  # 跳过闭合围栏
            continue

        hm = HEADING_RE.match(line)
        if hm:
            headings.append(
                {"level": len(hm.group(1)), "text": hm.group(2), "line": i + 1}
            )

        for lm in LINK_RE.finditer(line):
            links.append(
                {
                    "line": i + 1,
                    "image": bool(lm.group(1)),
                    "text": lm.group(2),
                    "url": lm.group("url").strip("<>"),
                }
            )

        rd = REFDEF_RE.match(line)
        if rd:
            refdefs.append({"line": i + 1, "label": rd.group(1), "url": rd.group(2)})

        stripped = INLINE_CODE_RE.sub("", line)
        if KANA_RE.search(stripped):
            kana.append((i + 1, line.strip()))

        i += 1

    return {
        "fences": fences,
        "headings": headings,
        "links": links,
        "refdefs": refdefs,
        "kana": kana,
        "frontmatter_keys": _frontmatter_keys(text),
    }


def _frontmatter_keys(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    keys = []
    for line in text[4:end].split("\n"):
        m = re.match(r"^([A-Za-z0-9_.-]+):", line)
        if m:
            keys.append(m.group(1))
    return keys


def _slugify(value: str) -> str:
    """复刻 Python-Markdown 默认 slugify（ASCII 化）。"""
    value = INLINE_CODE_RE.sub(lambda m: m.group(0)[1:-1], value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("**", "").replace("__", "")
    value = value.replace("*", "")
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-")


def heading_ids(headings: list[dict]) -> set[str]:
    seen: set[str] = set()
    for h in headings:
        m = ATTR_ID_RE.search(h["text"])
        if m:  # attr_list 固定锚点（{ #id } / {: #id }）优先
            hid = m.group(1)
            while hid in seen:
                hid += "_1"
            seen.add(hid)
            continue
        hid = _slugify(h["text"])
        while hid in seen or not hid:
            m = re.search(r"-(\d+)$", hid)
            if m:
                hid = hid[: m.start()] + str(int(m.group(1)) + 1)
            else:
                hid = hid + "_1"
        seen.add(hid)
    return seen


# ---------------------------------------------------------------------------
# 路径与树
# ---------------------------------------------------------------------------


def find_root(start: Path) -> Path:
    p = start.resolve()
    for parent in [p, *p.parents]:
        if (parent / "mkdocs.yml").exists() and (parent / "doc").is_dir():
            return parent
    fail("找不到仓库根（需要同时存在 mkdocs.yml 与 doc/）。用 --root 指定。")


def fail(msg: str):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(2)


def ja_files(root: Path) -> list[Path]:
    out = []
    for p in sorted((root / "doc").rglob("*.md")):
        rel = p.relative_to(root / "doc")
        if rel.parts and rel.parts[0] in EXCLUDE_TOP_DIRS:
            continue
        if rel.name in EXCLUDE_NAMES:
            continue
        out.append(p)
    return out


def zh_path_for(root: Path, ja: Path) -> Path:
    return root / "doc" / "zh" / ja.relative_to(root / "doc")


def locate_ja(root: Path, path: Path) -> Path:
    """给定日文或译文路径，归一化为日文侧路径。"""
    p = path.resolve()
    zh_root = (root / "doc" / "zh").resolve()
    if zh_root in p.parents:
        rel = p.relative_to(zh_root)
        return root / "doc" / rel
    return p


# ---------------------------------------------------------------------------
# 检查
# ---------------------------------------------------------------------------


def check_pair(root: Path, ja_file: Path) -> list[tuple[str, str]]:
    zh_file = zh_path_for(root, ja_file)
    problems: list[tuple[str, str]] = []
    prefix = str(zh_file.relative_to(root)) if zh_file.is_relative_to(root) else str(zh_file)

    if not zh_file.exists():
        return [("MISS", prefix)]

    ja = parse_document(ja_file.read_text(encoding="utf-8", errors="replace"))
    zh = parse_document(zh_file.read_text(encoding="utf-8", errors="replace"))

    # --- 代码块 ---
    if len(ja["fences"]) != len(zh["fences"]):
        problems.append(
            ("E", f"代码块数量不一致: 日文 {len(ja['fences'])} / 中文 {len(zh['fences'])}")
        )
    for idx, (a, b) in enumerate(zip(ja["fences"], zh["fences"]), start=1):
        tag_a = a["info"].split()[:1]
        tag_b = b["info"].split()[:1]
        if tag_a != tag_b:
            problems.append(
                ("W", f"第 {idx} 个代码块的语言标记不同: 日文 {a['info']!r} / 中文 {b['info']!r}")
            )
        la = [l.rstrip() for l in a["body"]]
        lb = [l.rstrip() for l in b["body"]]
        if la != lb:
            j = 0
            while j < min(len(la), len(lb)) and la[j] == lb[j]:
                j += 1
            problems.append(
                (
                    "E",
                    f"第 {idx} 个代码块内容不一致（日文第 {a['start'] + 1 + j} 行 / "
                    f"中文第 {b['start'] + 1 + j} 行）；代码块必须原样保留",
                )
            )

    # --- 标题结构 ---
    lv_ja = [h["level"] for h in ja["headings"]]
    lv_zh = [h["level"] for h in zh["headings"]]
    if lv_ja != lv_zh:
        n = 0
        while n < min(len(lv_ja), len(lv_zh)) and lv_ja[n] == lv_zh[n]:
            n += 1
        problems.append(
            (
                "E",
                f"标题结构不一致（第 {n + 1} 个标题起）: 日文 {lv_ja!r} / 中文 {lv_zh!r}",
            )
        )

    # --- 链接 / 图片 ---
    zh_dir = zh_file.parent
    ja_dir = ja_file.parent
    doc_root = root / "doc"
    zh_ids: dict[str, set[str]] = {}
    ja_ids = heading_ids(ja["headings"])

    def ids_for(path: Path, cache: dict) -> set[str]:
        key = str(path)
        if key not in cache:
            if path.exists() and path.suffix == ".md":
                doc = parse_document(path.read_text(encoding="utf-8", errors="replace"))
                cache[key] = heading_ids(doc["headings"])
            else:
                cache[key] = set()
        return cache[key]

    for link in [*zh["links"], *zh["refdefs"]]:
        url = link["url"]
        if not url or url.startswith("#") or url.startswith(SKIP_SCHEMES):
            if url.startswith("#"):
                anchor = url[1:]
                if anchor and anchor not in ids_for(zh_file, zh_ids):
                    problems.append(
                        (
                            "W",
                            f"第 {link['line']} 行: 锚点 '#{anchor}' 在本文档找不到对应标题",
                        )
                    )
            continue
        target, _, anchor = url.partition("#")
        target = target.strip()
        if not target:
            continue
        decoded = _unquote(target)

        candidates = [(zh_dir / decoded)]
        rel = Path(os.path.normpath(zh_dir / decoded))
        try:
            rel_from_doc = rel.relative_to(doc_root)
            if rel_from_doc.parts[:1] == ("zh",):
                candidates.append(doc_root / Path(*rel_from_doc.parts[1:]))
        except ValueError:
            pass
        candidates.append(ja_dir / decoded)

        resolved: Path | None = None
        for cand in candidates:
            norm = Path(os.path.normpath(cand))
            if norm.exists():
                resolved = norm
                break
        if resolved is None:
            problems.append(
                (
                    "E",
                    f"第 {link['line']} 行: {'图片' if link['image'] else '链接'}目标不存在: "
                    f"{url}（译文树与日文树都找不到）",
                )
            )
            continue
        if anchor:
            ids = ids_for(resolved, zh_ids)
            if ids and anchor not in ids:
                problems.append(
                    (
                        "W",
                        f"第 {link['line']} 行: 目标 {url} 的锚点 '{anchor}' 找不到对应标题",
                    )
                )

    # --- 假名残留 ---
    for line_no, snippet in zh["kana"]:
        problems.append(
            ("W", f"第 {line_no} 行: 残留日文假名: {snippet[:60]}")
        )

    # --- frontmatter ---
    if ja["frontmatter_keys"] != zh["frontmatter_keys"]:
        problems.append(
            (
                "W",
                f"frontmatter 键不一致: 日文 {ja['frontmatter_keys']} / 中文 {zh['frontmatter_keys']}",
            )
        )

    return problems


def _unquote(s: str) -> str:
    from urllib.parse import unquote

    return unquote(s)


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(
        description="doc/ 日文 ↔ doc/zh/ 中文 成对检查",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("paths", nargs="*", help="要检查的文件（日文或译文均可）")
    ap.add_argument("--all", action="store_true", help="检查所有已存在的译文对")
    ap.add_argument("--untranslated", action="store_true", help="列出未翻译的日文文件")
    ap.add_argument("--root", type=Path, default=None, help="仓库根（默认自动查找）")
    ap.add_argument("--fail-on-warn", action="store_true", help="WARNING 也返回非 0")
    ap.add_argument("--quiet", action="store_true", help="只输出问题与汇总")
    args = ap.parse_args()

    if args.root:
        root = args.root.resolve()
        if not (root / "mkdocs.yml").exists():
            fail(f"--root {root} 下没有 mkdocs.yml")
    elif args.paths:
        root = find_root(Path(args.paths[0]).parent if Path(args.paths[0]).parent.parts else Path.cwd())
    else:
        root = find_root(Path.cwd())

    all_ja = ja_files(root)

    if args.untranslated:
        missing = [p for p in all_ja if not zh_path_for(root, p).exists()]
        if not args.quiet:
            for p in missing:
                print(p.relative_to(root))
        counts: dict[str, int] = {}
        for p in missing:
            top = p.relative_to(root / "doc").parts[0]
            counts[top] = counts.get(top, 0) + 1
        print(
            f"== 未翻译: {len(missing)} / {len(all_ja)} 篇 "
            f"({', '.join(f'{k}: {v}' for k, v in sorted(counts.items()))}) =="
        )
        return 0

    if args.paths:
        targets = [locate_ja(root, Path(p)) for p in args.paths]
    elif args.all:
        targets = [p for p in all_ja if zh_path_for(root, p).exists()]
        if not targets:
            print("== 还没有任何译文（doc/zh/ 为空？） ==")
            return 0
    else:
        ap.print_help()
        return 0

    n_err = n_warn = n_miss = n_ok = 0
    for ja in targets:
        rel = ja.relative_to(root)
        problems = check_pair(root, ja)
        if problems and problems[0][0] == "MISS":
            print(f"[ ] 未翻译: {rel}（没有 doc/zh/ 对应文件）")
            n_miss += 1
            continue
        if not problems:
            n_ok += 1
            continue
        print(f"\n--- {rel} → doc/zh/{ja.relative_to(root / 'doc')} ---")
        for level, msg in problems:
            print(f"[{level}] {msg}")
            if level == "E":
                n_err += 1
            else:
                n_warn += 1

    print(
        f"\n== 汇总: {len(targets)} 篇 / OK {n_ok} / ERROR {n_err} / WARNING {n_warn}"
        + (f" / 未翻译 {n_miss}" if n_miss else "")
        + " =="
    )
    if n_err or (args.fail_on_warn and n_warn):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
