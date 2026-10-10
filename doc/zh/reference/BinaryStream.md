# BinaryStream

## 成员列表

### 构造函数

- [BinaryStream](#binarystream)

### 属性

- [storage](#storage)
- [mode](#mode)

### 方法

- [finalize](#finalize)
- [open](#open)
- [close](#close)
- [read](#read)
- [write](#write)
- [readI8](#readi8)
- [readI16LE](#readi16le)
- [readI32LE](#readi32le)
- [readI64LE](#readi64le)
- [readI16BE](#readi16be)
- [readI32BE](#readi32be)
- [readI64BE](#readi64be)
- [writeI8](#writei8)
- [writeI16LE](#writei16le)
- [writeI32LE](#writei32le)
- [writeI64LE](#writei64le)
- [writeI16BE](#writei16be)
- [writeI32BE](#writei32be)
- [writeI64BE](#writei64be)
- [copy](#copy)
- [compress](#compress)
- [decompress](#decompress)
- [setProgressCallback](#setprogresscallback)
- [setFilter](#setfilter)
- [seek](#seek)
- [tell](#tell)

### 常量

- [bsRead](#bsread)
- [bsWrite](#bswrite)
- [bsAppend](#bsappend)
- [bsUpdate](#bsupdate)
- [bsSeekSet](#bsseekset)
- [bsSeekCur](#bsseekcur)
- [bsSeekEnd](#bsseekend)

---

### BinaryStream

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` |  |
| `mode` | `&nbsp;` |  |

**说明**

构造函数／析构函数

---

### storage

属性 \ 访问: `r`

**说明**

当前打开的存储

未打开时为 void

---

### mode

属性 \ 访问: `r`

**说明**

当前模式

未打开时为 -1

---

### finalize

方法

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 目标存储 |
| `mode` | `&nbsp;` | 模式指定 (bsRead, bsWrite, bsAppend, bsUpdate) |

**说明**

打开存储

---

### close

方法

**说明**

关闭已打开的存储

---

### read

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `size` | `&nbsp;` | 读取的大小（字节） |

**返回值**

读取到的数据（octet 格式）在到达末尾等情况下无法读取时为 void（注意不是 length=0 的 octet）

**说明**

读取指定的字节数

---

### write

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `data` | `&nbsp;` | 要写入的数据（octet 格式或字符串） |

**返回值**

写入的字节数

**说明**

写入数据

data 为字符串时按 wchar 写入（不支持编码转换）

---

### readI8

方法

**返回值**

读取到的数值 / 在到达末尾等情况下无法读取时为 void

**说明**

将 {1,2,4,8} 字节作为数值读取

※除 8 字节以外的数值按 unsigned 读取（不做符号扩展）
※仅在连 1 字节都无法读取时才会返回 void
在读取到 1 字节以上但不足指定字节数时，返回的是将不足部分用 0 填补后的值，请注意

---

### readI16LE

方法

**说明**

读取 2 字节 (Little Endian)

---

### readI32LE

方法

**说明**

读取 4 字节 (Little Endian)

---

### readI64LE

方法

**说明**

读取 8 字节 (Little Endian)

---

### readI16BE

方法

**说明**

读取 2 字节 (Big Endian)

---

### readI32BE

方法

**说明**

读取 4 字节 (Big Endian)

---

### readI64BE

方法

**说明**

读取 8 字节 (Big Endian)

---

### writeI8

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` | 要写入的数值 |

**返回值**

写入的字节数

**说明**

以 {1,2,4,8} 字节写入数值

---

### writeI16LE

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**说明**

写入 2 字节 (Little Endian)

---

### writeI32LE

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**说明**

写入 4 字节 (Little Endian)

---

### writeI64LE

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**说明**

写入 8 字节 (Little Endian)

---

### writeI16BE

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**说明**

写入 2 字节 (Big Endian)

---

### writeI32BE

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**说明**

写入 4 字节 (Big Endian)

---

### writeI64BE

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**说明**

写入 8 字节 (Big Endian)

---

### copy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 复制源存储（与当前打开的存储相同时会抛出异常） |
| `elm` | `void` | 动作指定用字典（in/out）的内容如下：（省略时为单纯复制，无 [out]）<br>offset  :[in] 复制源存储的读取开始偏移（省略时为开头）<br>length  :[in] 复制源存储的最大读取大小（省略时为文件大小）<br>filter  :[in] 进行过滤处理的函数名（省略时不做过滤处理）<br>fparam  :[in] 传递给过滤器的参数值 (int)<br>nocopy  :[in] 指定 true 时不写入输出（省略时为 false，只想获取 hash 等情况下指定）<br>md5     :[in] 指定 true 时返回输出的 MD5 摘要<br>hash    :[out]读取到的文件的哈希值（Adler32）<br>read    :[out]读取到的字节数<br>digest  :[out]写入的数据的 MD5 摘要（octet） ※仅在 md5 为 true 时有效 |

**返回值**

写入的字节数

**说明**

从其他存储复制数据

目标存储中从 offset 开始 length 长度的内容，会从当前流的位置开始写入
过滤器的详情请参阅 setFilter() 的说明

---

### compress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 复制源存储（与当前打开的存储相同时会抛出异常） |
| `elm` | `void` | 动作指定用字典（in/out）的内容与 copy() 相同，另加以下内容：<br>comp_lv :[in] zlib 压缩级别（1~9）。省略时，或 elm 本身未指定时为 9 |

**返回值**

写入的字节数

**说明**

从其他存储复制数据的同时进行压缩

将目标存储用 zlib/deflate 压缩，并从当前流的位置开始写入
过滤函数应用于压缩前的二进制数据

---

### decompress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 复制源存储（与当前打开的存储相同时会抛出异常） |
| `elm` | `void` | 动作指定用字典（in/out）的内容与 copy() 相同 |

**返回值**

写入的字节数

**说明**

从其他存储复制数据的同时进行解压

将目标存储用 zlib/inflate 解压，并从当前流的位置开始写入
解压失败时会抛出异常
过滤函数应用于解压后的二进制数据
hash[out] 针对解压后/过滤后的二进制数据计算

---

### setProgressCallback

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | 回调函数 function(storage, read_size) { return true_if_cancel; }<br>为 void 时解除 |

**说明**

设置进度回调

设置 copy/compress/decompress 处理过程中回调的函数。
回调（在当前的实现中）会在每读取 1MiB 时以及读取到末尾时被调用。
从回调返回 true 即可取消处理。
※回调的间隔可能会被更改

在 TJS 层面，处理会卡住虽然属于规格行为，但通过另外使用 windowExProgress 插件等，
即可接受来自用户的取消。

---

### setFilter

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dll` | `&nbsp;` | 目标 DLL 文件（为 void 时解除设置） |

**说明**

设置过滤器 DLL

对 copy/compress/decompress 的数据设置使用外部 DLL 的过滤器
在 elm.filter 中指定函数名时，将使用该 DLL 中以下列形式导出的函数作为过滤器
void (__stdcall *FilterProc)(uint32 hash, uint64 offset, void *buffer, uint32 length);

---

### seek

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `pos` | `&nbsp;` | 位置 |
| `whence` | `&nbsp;` | 基准位置 (bsSeekSet, bsSeekCur, bsSeekEnd) |

**返回值**

移动后的位置

**说明**

更改流的位置

---

### tell

方法

**返回值**

位置

**说明**

获取流的当前位置

---

### bsRead

常量

值: `0`

**说明**

读取

---

### bsWrite

常量

值: `1`

**说明**

写入

---

### bsAppend

常量

值: `2`

**说明**

追加写入

---

### bsUpdate

常量

值: `3`

**说明**

更新

---

### bsSeekSet

常量

值: `0`

**说明**

从开头

---

### bsSeekCur

常量

值: `1`

**说明**

从当前位置

---

### bsSeekEnd

常量

值: `2`

**说明**

从末尾

---
