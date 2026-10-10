# 演示 (浏览器运行)

吉里吉里Z 的核心演示 + 跨插件演示可以**在浏览器中直接运行**。
把 `krkrz_dev/data` 的集成演示画廊 (全部 20 个演示) 用 Emscripten (wasm) 构建，
并嵌入到本页面。从菜单选择演示后，**无需重启**即可切换，
**按 ESC 返回菜单**（与桌面版完全相同的 hub 工作方式）。

!!! note "运行环境"
    - 在 **PC 版 Chrome / Edge / Firefox 最新版**上运行（使用 `SharedArrayBuffer` / wasm 线程。异步处理使用全浏览器兼容的 Asyncify 构建）。
    - 首次访问时会为了注册 Service Worker 而**自动重新加载一次**。
    - 启动时会加载 **约 39 MB**（wasm + 数据 + 日文/emoji 字体）。只有点击下方的“▶ 运行演示”时才会加载。
    - 使用 Elements 面板的演示通过鼠标操作，其他的通过底部栏或键盘（参见各演示的操作说明）运行。
    - 嵌入的是 **2026-09-01 构建版 (全部 20 个演示)**。更新了引擎或演示的
      情况下需要重新构建 wasm 并替换 (最新列表见仓库的
      `data/ROADMAP.md`)。

<div id="krkrz-demo-holder" markdown="0" style="margin:1.5em 0;">
  <button id="krkrz-demo-run"
          style="display:block;width:100%;aspect-ratio:16/9;border:0;border-radius:10px;
                 background:#14161c;color:#e6ebf5;font-size:1.2rem;cursor:pointer;
                 display:flex;align-items:center;justify-content:center;gap:.6em;">
    ▶ 运行演示（将加载约 39 MB）
  </button>
</div>

<p>
  如果显示不正常，请
  <a href="../_assets/demo/" target="_blank" rel="noopener">在新标签页中全屏显示</a>
  试试看。
</p>

<script>
(function () {
  var btn = document.getElementById("krkrz-demo-run");
  if (!btn) return;
  btn.addEventListener("click", function () {
    var holder = document.getElementById("krkrz-demo-holder");
    var f = document.createElement("iframe");
    f.src = "../_assets/demo/";
    f.setAttribute("allow", "autoplay; fullscreen; gamepad");
    f.setAttribute("allowfullscreen", "");
    f.style.cssText =
      "width:100%;aspect-ratio:16/9;border:0;border-radius:10px;background:#000;";
    holder.innerHTML = "";
    holder.appendChild(f);
  });
})();
</script>

## 机制

- 引擎本体是**一个共享的 wasm 二进制文件**，演示数据以 preload（`krkrz.data`）方式随附。
- GitHub Pages 无法设置 COOP/COEP 响应头，因此通过 `coi-serviceworker` 在
  客户端侧注入，使 `crossOriginIsolated` 成立（COEP 默认是
  `credentialless`）。
- 构建使用外围仓库 [krkrz_web](https://github.com/wamsoft/krkrz_web)，
  交付物放置在 `doc/_assets/demo/`。引擎更新时在 krkrz_web 中重新构建
  并替换。

各演示的内容、操作请参见 [data/README](https://github.com/wamsoft/krkrz_dev/blob/develop/data/README.md)
以及各演示文件夹中的 `readme.txt`。
