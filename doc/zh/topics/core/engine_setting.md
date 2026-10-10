# 引擎设置的添加/编辑
## 以往的方法
在吉里吉里2 中，本体是取得由 TVPGetCommandDesc 得到的以 "|" 分隔 ( 也有其他分隔字符 ) 的字符串，并据此显示引擎设置的条目。  
另外，插件是在注释部分加入 --has-option--、公开 GetOptionDesc 函数，并在其中以与本体相同的字符串格式写入设置的详细内容。  
以前是通过链接器的 /COMMENT: 添加 --has-option--，但近来的 Visual Studio 会忽略它，因此用通常的方法已经无法将其放入 DLL 二进制中。

## 吉里吉里Z 以后的方法
在吉里吉里Z 中，设置条目的列表改为 JSON，并把方法改成不嵌入源码、而是放入资源。  
JSON 的具体格式，看一下文件应该就能大致明白。

### 本体侧的定义文件 (SSOT) 与语言选择

本体的定义由 `src/core/resource/optiondesc.json` ( 日语 = 基底 ) 及
其按语言拆分的文件 `optiondesc-en.json` / `optiondesc-chs.json` / `optiondesc-cht.json`
这 4 个文件构成 SSOT ( 以前为 WINVER 单独管理的 `win32/vcproj/option_desc_*.json`
已于 2026-08 废止，统一到这边 )。编辑时请保持 4 种语言的结构 ( 分类与
选项的排列 ) 一致。

读取时在运行期选择语言 ( OS 语言 = `System.systemLanguage`，或者启动选项
`-language`。如果没有支持的语言，则 en → 基底依次回退 )：

- SDL3 构建 … 直接读取 `resource/optiondesc<言語suffix>.json`
- WINVER 构建 … `resource/*` 会以文件名的原样作为 **BINARY** 资源嵌入 exe，
  并按照同样的规则选择。找不到时会回退到以前的 TEXT 资源
  ( `IDR_OPTION_DESC_JSON`，实体是 `resource/optiondesc.json` )
  ( 这是把 `KRKRZ_RESOURCE_DIR` 替换为项目资源时的保险 )

### 插件侧

插件侧需要稍微注意。  
资源的种类是 TEXT，ID 以字符串 IDR_OPTION_DESC_JSON 存入 DLL。  

具体来说，在 *.rc 文件中像下面这样记述并添加到资源中。  
IDR_OPTION_DESC_JSON TEXT "option_desc_ja.json"

resource.h 中不要定义 IDR_OPTION_DESC_JSON。  
如果定义了 IDR_OPTION_DESC_JSON，资源 ID 就会以数值形式被添加。

在 SDL3 / 通用构建的插件 ( .so 等无法持有 Win32 资源的形式 ) 中，
把与 DLL 相邻的 `<basename>.options.json` ( 例: `myplugin.options.json` ) 放置
在那里就会被读取。没有的话就单纯按没有设置条目来处理。

### JSON 的格式

顶层是**分类的数组**，每个分类在 `options` 中持有选项定义的数组。
本体的实物请参照 `src/core/resource/optiondesc.json` ( 7 个分类 / 66 个选项 )。

```json
[
  {
    "category": "システム全般",
    "options": [
      {
        "caption":     "データ保存場所",
        "description": "吉里吉里が様々なデータを保存する場所を指定します。

...",
        "name":        "datapath",
        "type":        "string",
        "length":      255,
        "user":        false,
        "value":       "$(exepath)\savedata"
      },
      {
        "caption":     "処理ウェイト",
        "description": "...",
        "name":        "contfreq",
        "type":        "select",
        "user":        true,
        "values": [
          { "value": "0",  "desc": "ウェイトをかけない", "default": true },
          { "value": "60", "desc": "60Hz" }
        ]
      }
    ]
  }
]
```

#### 分类

| 键 | 内容 |
|---|---|
| `category` | 出现在设置工具的标签页 / 标题中的分类名 |
| `options`  | 属于这个分类的选项定义的数组 |

#### 选项定义

| 键 | 必需 | 内容 |
|---|---|---|
| `caption`     | ○ | 在设置工具中显示的条目名 |
| `description` | ○ | 说明文。`
` 可以换行 |
| `name`        | ○ | 命令行选项名 ( 不要写开头的 `-`。`datapath` 的话就是 `-datapath=` ) |
| `type`        | ○ | `"select"` ( 从候选值中选择 ) 或者 `"string"` ( 自由输入 ) |
| `user`        | ○ | 是否显示在面向最终用户的设置工具 ( `-userconf` ) 中。`false` 的话只出现在 Releaser 的制作者向设置中 |
| `values`      | 仅 `select` | 候选值的数组 |
| `value`       | 仅 `string` | 初始值 |
| `length`      | 仅 `string` | 输入框的最大字符数 |

#### 候选值 ( `values` 的元素 )

| 键 | 必需 | 内容 |
|---|---|---|
| `value`   | ○ | 实际传递给选项的值 ( 例 `"60"` ) |
| `desc`    | ○ | 作为候选值显示的字符串 |
| `default` | | 为 `true` 时这就是默认值。分类内只能指定 1 个 |

!!! note "与命令行选项说明的关系"
    这里写的 `description` 是**出现在设置工具中的说明**，
    与 [命令行选项](../../guide/CommandLine.md) 的文档是分开管理的。
    添加 / 更改选项时，两边的更新都必不可少。
