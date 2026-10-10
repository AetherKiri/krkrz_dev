# Storages

Storages 类是持有与吉里吉里本体的**存储系统**相关的方法和属性的类。无法从该类创建对象。

## 成员列表

### 属性

- [currentPath](#currentpath)

### 方法

- [addAutoPath](#addautopath)
- [removeAutoPath](#removeautopath)
- [getFullPath](#getfullpath)
- [getPlacedPath](#getplacedpath)
- [isExistentStorage](#isexistentstorage)
- [extractStorageExt](#extractstorageext)
- [extractStorageName](#extractstoragename)
- [extractStoragePath](#extractstoragepath)
- [chopStorageExt](#chopstorageext)
- [searchCD](#searchcd)
- [getLocalName](#getlocalname)
- [selectFile](#selectfile)
- [selectDirectory](#selectdirectory)
- [addCacheTargetExtension](#addcachetargetextension)
- [addDecodeTargetExtension](#adddecodetargetextension)
- [removeDecodeTargetExtension](#removedecodetargetextension)
- [clearArchiveCache](#cleararchivecache)
- [clearCache](#clearcache)
- [clearAllCaches](#clearallcaches)
- [clearTransientCaches](#cleartransientcaches)
- [clearFastCache](#clearfastcache)
- [clearOldCache](#clearoldcache)
- [commitSavedata](#commitsavedata)
- [deleteFile](#deletefile)
- [dirlist](#dirlist)
- [dirtree](#dirtree)
- [getFileProperty](#getfileproperty)
- [isCacheLoading](#iscacheloading)
- [isExistentDirectory](#isexistentdirectory)
- [isFastCacheLoading](#isfastcacheloading)
- [getLastModifiedFileTime](#getlastmodifiedfiletime)
- [moveFile](#movefile)
- [requestCache](#requestcache)
- [requestFastCache](#requestfastcache)
- [isImagePrefetchLoading](#isimageprefetchloading)
- [pinCache](#pincache)
- [unpinCache](#unpincache)
- [isCachePinned](#iscachepinned)
- [getFileCacheList](#getfilecachelist)
- [getImageCacheList](#getimagecachelist)
- [dumpFileCacheList](#dumpfilecachelist)
- [dumpImageCacheList](#dumpimagecachelist)
- [rollbackSavedata](#rollbacksavedata)
- [setCacheMaxSize](#setcachemaxsize)
- [fstat](#fstat)
- [getTime](#gettime)
- [createDirectory](#createdirectory)
- [removeDirectory](#removedirectory)
- [copyFile](#copyfile)
- [exportFile](#exportfile)
- [truncateFile](#truncatefile)
- [getMD5HashString](#getmd5hashstring)
- [getTemporaryName](#gettemporaryname)
- [isExistentStorageNoSearchNoNormalize](#isexistentstoragenosearchnonormalize)
- [clearStorageCaches](#clearstoragecaches)

---

### currentPath

属性 \ 访问: `r`

**类型**: `String`

**说明**

当前目录

以存储名 ( 末尾为 `/` ) 的形式返回进程的当前目录。
可以像 `Storages.getFullPath(Storages.currentPath + name)` 这样，用作相对路径的基准。
在没有当前目录概念的环境中会变为空字符串。

引擎本体版是只读的。在加载了 fstat 插件的环境 ( WINVER ) 中
会被替换为插件版，可以通过赋值更改当前目录。

---

### addAutoPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要添加到自动搜索路径的路径。<br>路径的末尾，在指定归档内的根文件夹时需要用 '>'，指定普通文件夹时<br>需要用 '/' 结尾<br>( 例 : `"Archive/arc.xp3>"` 或 `"System/"` ) 。<br>从 2.19 beta 14 起，归档的分隔符从 '#' 改为 '>'。 |

**说明**

向自动搜索路径添加

向**自动搜索路径**添加指定的路径。吉里吉里在搜索可用存储时，
会查找注册在这个自动搜索路径中的路径。

自动搜索路径中，后指定的会被优先搜索。

另外，项目文件夹会被最优先搜索。

**相关:** [Storages.removeAutoPath](Storages.md#removeautopath)

---

### removeAutoPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要从自动搜索中删除的路径。 |

**说明**

删除自动搜索路径

从自动搜索路径中删除指定的路径。

**相关:** [Storages.addAutoPath](Storages.md#addautopath)

---

### getFullPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要变为完整统一存储名的存储名。 |

**返回值**

完整的统一存储名

**说明**

获取完整的统一存储名

把 path 指定的存储名转换为完整的**统一存储名**。

冗长的路径访问 ( 例如 `system/flags/../data/` 等 ) 会被全部压缩。

未指定当前介质、当前文件夹时会进行补全。

**相关:** [Storages.getPlacedPath](Storages.md#getplacedpath)

---

### getPlacedPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要搜索的存储名。 |

**返回值**

找到的位置会以统一存储名返回。未找到时返回空字符串。

**说明**

搜索存储

从**自动搜索路径**中搜索 storage 指定的存储。

**相关:** [Storages.getFullPath](Storages.md#getfullpath) / [Storages.isExistentStorage](Storages.md#isexistentstorage)

---

### isExistentStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要确认是否存在的存储名。 |

**返回值**

能确认存在则返回真，不存在则返回假。

**说明**

确认存储是否存在

确认 storage 指定的存储是否存在。比使用 getPlacedPath 更高速。

**相关:** [Storages.getPlacedPath](Storages.md#getplacedpath)

---

### extractStorageExt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要抽取扩展名部分的存储名。 |

**返回值**

返回扩展名部分。扩展名部分也包含 `.` (点)。没有扩展名时
返回空字符串。

**说明**

抽取存储名的扩展名

从指定的存储名中抽取扩展名部分并返回。

**相关:** [Storages.extractStorageName](Storages.md#extractstoragename) / [Storages.extractStoragePath](Storages.md#extractstoragepath) / [Storages.chopStorageExt](Storages.md#chopstorageext)

---

### extractStorageName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要抽取存储名的存储名。 |

**返回值**

返回存储名。没有存储名时返回空字符串。

**说明**

抽取存储名

从指定的存储名中抽取存储名部分 ( 除去路径 ) 并返回。

例如传入 `"System/hoge.txt"` 时，返回 `"hoge.txt"`。

**相关:** [Storages.extractStorageExt](Storages.md#extractstorageext) / [Storages.extractStoragePath](Storages.md#extractstoragepath)

---

### extractStoragePath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要抽取路径的存储名。 |

**返回值**

返回路径。没有路径时返回空字符串。

**说明**

抽取存储名的路径

从指定的存储名中抽取路径部分并返回。

例如传入 `"file://home/dee/hoge.txt"` 时，返回 `"file://home/dee/"`。

**相关:** [Storages.extractStorageExt](Storages.md#extractstorageext) / [Storages.extractStorageName](Storages.md#extractstoragename)

---

### chopStorageExt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要切掉扩展名部分的存储名。 |

**返回值**

返回切掉扩展名部分的存储名。

**说明**

切掉存储名的扩展名

从指定的存储名中切掉扩展名部分并返回。

例如传入 `"file://home/dee/hoge.txt"` 时，返回 `"file://home/dee/hoge"`。

**相关:** [Storages.extractStorageExt](Storages.md#extractstorageext)

---

### searchCD

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `volume` | `&nbsp;` | 指定要搜索的 CD 的卷标。 |

**返回值**

返回找到的 CD-ROM 驱动器的驱动器号。

**说明**

CD 搜索

查找具有指定卷标的 CD 驱动器，返回其驱动器号 ( 如 'H' )。

当然，驱动器中必须已插入相应的 CD-ROM。

---

### getLocalName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要转换为**本地文件名**的统一存储名。 |

**返回值**

返回本地文件名。无法转换为本地文件名时会返回空字符，
或抛出异常。

**说明**

获取本地文件名

把指定的统一存储名转换为 OS 原生形式 ( 本地文件名 ) 并返回。

---

### selectFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `params` | `&nbsp;` | 指定用于数据传递的字典数组。<br>传给该方法时，可以指定以下成员。另外，<br>部分成员会在该方法结束后值被更改。<br>**filter**<br>以数组形式传入过滤器字符串。<br>过滤器字符串由过滤器的说明与过滤器用 \| (半角竖线) 分隔来指定，<br>过滤器中指定通配符。一个过滤器对应多个<br>扩展名时用 ; (半角分号) 分隔。<br>要指定多个过滤器时以数组指定。<br>省略时不使用过滤器。<br>例 :<br>`["画像ファイル(*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg)\|*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg", `<br>` "スクリプトファイル(*.tjs;*.ks)\|*.tjs;*.ks"]`<br>**filterIndex**<br>指定已选中的过滤器编号 ( filter 中指定的 ) 。<br>指定 1 时，filter 中指定的第一个过滤器在初始状态下<br>处于选中状态。指定 2 时变为选中第 2 个过滤器的状态<br>( 注意不是从 0 开始的索引编号；<br>开头是 1 )。<br>省略时选中开头的过滤器。<br>另外，用户按下 OK 按钮时，最后在对话框上<br>被选中的过滤器索引会被设置到该成员。<br>**name**<br>指定文件名。省略或指定空字符串时，可以让初始状态下不选择任何文件。<br>另外，用户按下 OK 按钮时，选中的文件会被设置到该成员。<br>**initialDir**<br>指定初始状态下显示的文件夹。<br>省略时使用当前目录。<br>**title**<br>显示对话框的标题。<br>省略时为默认的“打开”或“另存为”<br>( 取决于 save 成员的设置 )。<br>**save**<br>指定对话框的种类。<br>为 false(默认) 时，使用“打开”对话框。<br>为 true 时，使用“另存为”对话框。<br>**defaultExt**<br>指定默认的扩展名。用户未指定扩展名时<br>自动附加该扩展名。这里指定的扩展名中请勿指定 . (句点)。<br>省略时不会附加扩展名。<br>**平台差异**<br>Windows 原生版使用 OS 标准的文件对话框 ( GetOpenFileName )，<br>SDL 版使用 SDL 的文件对话框 ( 两者均面向桌面 )。<br>SDL 版中 filter 的通配符 ( 例 `*.png;*.jpg` ) 会被转换为 SDL 形式后<br>应用，但 title / defaultExt / filterIndex ( 初始选择、返回值 ) 可能会因环境<br>而被忽略。选择结果的 name 会与 Windows 版同样以规范化后的<br>存储名写回。 |

**返回值**

用户选择文件并按下 OK 按钮则为真，按下取消按钮则为假。

**说明**

显示文件选择对话框

打开文件选择对话框。

var params = %[

filter : [ "テキストファイル(*.txt)|*.txt", "バイナリファイル(*.bin)|*.bin" ],

filterIndex : 1,

name : "",

initialDir : System.exePath,

title : "ファイルを開く",

save : false,

];

if(Storages.selectFile(params))

System.inform("選択したファイルは : " + params.name);

---

### selectDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `params` | `&nbsp;` | 指定用于数据传递的字典数组。可以指定的成员<br>如下。<br>**name**<br>指定初始选中的文件夹。用户按下 OK 时，所选文件夹的<br>规范化存储名会被写回该成员。<br>**title**<br>指定对话框的标题 ( 仅 WINVER 构建生效 )。<br>**rootDir**<br>指定初始显示的文件夹 ( 未指定 name 时的回退 ) 。<br>**window**<br>指定作为父窗口的窗口 ( 可省略 )。<br>**平台差异**<br>Windows 原生版使用 OS 标准的文件夹选择对话框 ( IFileOpenDialog )，<br>SDL 版使用 SDL 的文件夹选择对话框 ( SDL_ShowOpenFolderDialog )。<br>SDL 版中 title 可能会被忽略。 |

**返回值**

用户选择文件夹并按下 OK 按钮则为真，取消则为假。

**说明**

显示文件夹选择对话框

以模态方式打开文件夹 ( 目录 ) 选择对话框。

var params = %[

name : "",

title : "フォルダを選択",

rootDir : System.exePath,

];

if(Storages.selectDirectory(params))

System.inform("選択したフォルダは : " + params.name);

---

### addCacheTargetExtension

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ext` | `&nbsp;` | 指定作为对象的扩展名。如果开头没有 `.` (句点)，<br>会自动补上。 |
| `minSize` | `0` | 指定对该扩展名应用的最小文件大小 ( 字节 )。<br>指定 0 ( 默认 ) 时无大小阈值，小于它<br>的文件不会成为 cache 对象。 |

**说明**

添加内存中缓存对象的扩展名

添加在文件加载时放入内存中缓存 ( file 层 ) 的扩展名。
在这里注册的扩展名的文件，在从存储读取时
内容会被保留在内存中，省略再次访问时的磁盘 I/O。

**相关:** [Storages.requestCache](Storages.md#requestcache) / [Storages.addDecodeTargetExtension](Storages.md#adddecodetargetextension)

---

### addDecodeTargetExtension

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ext` | `&nbsp;` | 指定作为对象的扩展名。如果开头没有 `.` (句点)，<br>会自动补上。 |
| `minSize` | `0` | 指定对该扩展名应用的最小文件大小 ( 字节 )。<br>指定 0 ( 默认 ) 时无大小阈值。 |

**说明**

添加 decode 缓存对象的扩展名

添加放入图像解码结果 ( decode 层缓存 ) 的扩展名。
在这里注册的扩展名的文件会由 [Storages.requestCache](Storages.md#requestcache)
在后台执行到解码为止并放入缓存。

**相关:** [Storages.removeDecodeTargetExtension](Storages.md#removedecodetargetextension) / [Storages.requestCache](Storages.md#requestcache)

---

### removeDecodeTargetExtension

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ext` | `&nbsp;` | 指定要删除的扩展名。 |

**说明**

删除 decode 缓存对象的扩展名

把通过 [Storages.addDecodeTargetExtension](Storages.md#adddecodetargetextension)
添加的扩展名从 decode 缓存对象中排除。

**相关:** [Storages.addDecodeTargetExtension](Storages.md#adddecodetargetextension)

---

### clearArchiveCache

方法

**说明**

丢弃归档缓存

丢弃打开 XP3 等归档时引擎内部保留的归档
元信息与解压缓冲区的全部缓存。

在依次切换大量归档等想要抑制内存使用量的场合
使用。

---

### clearCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `""` | 指定要丢弃的文件的路径。省略或指定空字符串时，<br>仅丢弃所有 transient 缓存 ( 未被 pin 的 )。 |

**说明**

丢弃缓存

丢弃通过 `Storages.requestCache` 读取的文件缓存。
file 层 / decode 层两层均为对象。

**相关:** [Storages.requestCache](Storages.md#requestcache) / [Storages.clearAllCaches](Storages.md#clearallcaches) / [Storages.clearTransientCaches](Storages.md#cleartransientcaches)

---

### clearAllCaches

方法

**说明**

丢弃全部缓存

丢弃 file 层 / decode 层的所有缓存。
因为连被 pin 的条目也会一并删除，相当于最大强度的 `doCompact(clAll)`。

**相关:** [Storages.clearCache](Storages.md#clearcache) / [Storages.clearTransientCaches](Storages.md#cleartransientcaches)

---

### clearTransientCaches

方法

**说明**

丢弃临时缓存

把未被 pin ( transient 的 ) 的缓存条目从 file 层 / decode 层
两方丢弃。设想用于返回标题画面等轻量缓存
清除用途。

**相关:** [Storages.pinCache](Storages.md#pincache) / [Storages.clearAllCaches](Storages.md#clearallcaches)

---

### clearFastCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `""` | 指定要丢弃的文件的路径。省略或指定空字符串时<br>丢弃所有缓存。 |

**说明**

丢弃高速缓存

丢弃通过 `Storages.requestFastCache` 读取的文件缓存。

**相关:** [Storages.requestFastCache](Storages.md#requestfastcache)

---

### clearOldCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `keepTime` | `0` | 指定保留的秒数。指定 0 时所有缓存<br>均为对象。 |
| `force` | `0` | 指定非 0 时，即使正在被引用也会强制丢弃。<br>默认值为 0 ( 不丢弃正在被引用的 ) 。 |

**说明**

丢弃旧缓存

丢弃超过一定时间未被访问的缓存条目。

---

### commitSavedata

方法

**说明**

提交存档数据

确定 ( 提交 ) 写入到存档数据 ( savedata ) 区域的内容。
在部分平台上，对 savedata 区域的写入有时会缓冲
到本次调用为止。

**相关:** [Storages.rollbackSavedata](Storages.md#rollbacksavedata)

---

### deleteFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要删除的文件的存储名。 |

**返回值**

删除成功则返回真，失败则返回假。

**说明**

删除文件

删除指定的存储文件。同时也会从自动搜索路径的缓存
中移除相应条目。

**相关:** [Storages.moveFile](Storages.md#movefile)

---

### dirlist

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要获取列表的目录的存储名。<br>末尾需要以 `/` 结尾。 |

**返回值**

返回以文件名 / 目录名为元素的数组。

**说明**

获取目录内列表

以数组返回指定目录正下方的文件名和子目录名。

子目录的条目会以末尾附加 `/` 的形式出现。
在未定义 `TVP_NO_NORMALIZE_PATH` 的构建中，结果全部会
被规范化为小写。

不包含 `.` / `..` ( 自身与父级 )。

除了本地实际文件夹之外，也可以列举归档内或插件提供的介质
( `proxy://` 等 ) 中的文件夹。

**相关:** [Storages.dirtree](Storages.md#dirtree)

---

### dirtree

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要遍历的目录的存储名。 |
| `dironly` | `false` | 指定真时仅返回目录。默认值为假。 |

**返回值**

返回以路径为元素的数组。

**说明**

获取目录树

递归遍历指定目录之下，以数组返回文件 / 目录名。

**相关:** [Storages.dirlist](Storages.md#dirlist)

---

### getFileProperty

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要获取属性的文件名。 |

**返回值**

以字典形式返回属性。没有属性时返回 null。

**说明**

获取文件属性

从指定的存储名获取属性并返回。

---

### isCacheLoading

方法

**返回值**

正在读取中则返回真，否则返回假。

**说明**

判断通常缓存是否正在读取

如果通过 `Storages.requestCache` 请求的文件仍在后台
线程中读取，则返回真。

**相关:** [Storages.requestCache](Storages.md#requestcache)

---

### isExistentDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要确认的目录的存储名。<br>末尾需要以 `/` 结尾。 |

**返回值**

存在则返回真，不存在则返回假。传入不对应本地实际文件夹的
存储名 ( 归档内等 ) 时也返回假
( 不会抛出异常 )。

**说明**

确认目录是否存在

确认指定的目录是否存在。

**相关:** [Storages.isExistentStorage](Storages.md#isexistentstorage)

---

### isFastCacheLoading

方法

**返回值**

正在读取中则返回真，否则返回假。

**说明**

判断高速缓存是否正在读取

如果通过 `Storages.requestFastCache` 请求的文件仍在后台
线程中读取，则返回真。

**相关:** [Storages.requestFastCache](Storages.md#requestfastcache)

---

### getLastModifiedFileTime

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要获取最后更新时间的文件的存储名。 |

**返回值**

以 Windows 的 FILETIME 形式的 64bit 整数值
( 以 1601-01-01 00:00:00 UTC 为起点、以 100 纳秒为刻度的经过时间 ) 返回最后更新时间。
获取失败时返回 0。
因为全平台共通返回相同的单位与纪元，所以除了大小比较、差分检测
之外，也可以把值本身解释为绝对时间
( 与 fstat 插件的 Storages.getLastModifiedFileTime 同一规格 )。

**说明**

获取文件的最后更新时间

获取指定存储文件的最后更新时间。

---

### moveFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 指定移动源的存储名。 |
| `to` | `&nbsp;` | 指定移动目标的存储名。 |

**返回值**

移动成功则返回真，失败则返回假。

**说明**

移动 ( 重命名 ) 文件

把指定的存储文件移动 ( 重命名 ) 到别处。
移动成功时也会更新自动搜索路径的缓存。

**相关:** [Storages.deleteFile](Storages.md#deletefile)

---

### requestCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定读取对象的文件的存储名。 |
| `minSize` | `0` | 指定仅限本次调用的最小文件大小阈值 ( 字节 )。<br>指定 0 ( 默认 ) 时遵循扩展名侧的注册设置。 |

**说明**

向文件缓存发起读取请求

把指定的文件在后台读取到通常的文件缓存中。
通过 `Storages.addCacheTargetExtension` 注册的扩展名会放入 file 层的 cache，
通过 `Storages.addDecodeTargetExtension` 注册的图像扩展名会放入 decode 层的 cache
( 解码结果 )。两边都符合的扩展名会在两层并行触发。

**相关:** [Storages.clearCache](Storages.md#clearcache) / [Storages.isCacheLoading](Storages.md#iscacheloading) / [Storages.isImagePrefetchLoading](Storages.md#isimageprefetchloading) / [Storages.requestFastCache](Storages.md#requestfastcache)

---

### requestFastCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定读取对象的文件的存储名。 |
| `minSize` | `0` | 指定仅限本次调用的最小文件大小阈值 ( 字节 )。<br>指定 0 ( 默认 ) 时遵循扩展名侧的注册设置。 |

**说明**

向高速文件缓存发起读取请求

把指定的文件在后台读取到高速缓存中。
内部队列与通常缓存是不同系统，
会以比 `Storages.requestCache` 更高的优先级处理。

**相关:** [Storages.clearFastCache](Storages.md#clearfastcache) / [Storages.isFastCacheLoading](Storages.md#isfastcacheloading) / [Storages.requestCache](Storages.md#requestcache)

---

### isImagePrefetchLoading

方法

**返回值**

进行中则返回真，否则返回假。

**说明**

判断图像 decode prefetch 的进行状况

由 [Storages.requestCache](Storages.md#requestcache) 等触发的
图像 decode prefetch ( decode 层 ) 作业仍在后台
处理中时返回真。
`Storages.isCacheLoading` 查看的是 file 层，而这个是用于 decode 层
的 polling。

**相关:** [Storages.requestCache](Storages.md#requestcache) / [Storages.isCacheLoading](Storages.md#iscacheloading)

---

### pinCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要 pin 的文件的存储名。 |

**说明**

将缓存条目变为 pin 状态

把指定路径的 cache 条目在 file 层 / decode 层两方设为 **pin** 状态，
使其不属于 `clearCache(空字符串)` 和 `clearTransientCaches` 的对象。
同时，如果还没有放入 cache，会自动触发异步加载。
即使是经由 autopath 的文件，也会规范化到实体路径后 pin。

**相关:** [Storages.unpinCache](Storages.md#unpincache) / [Storages.isCachePinned](Storages.md#iscachepinned) / [Storages.clearTransientCaches](Storages.md#cleartransientcaches)

---

### unpinCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要解除 pin 的文件的存储名。 |

**说明**

解除缓存条目的 pin

解除通过 [Storages.pinCache](Storages.md#pincache) pin 的条目。
解除后会回到 transient 清除对象 ( 不会被立即丢弃 )。

**相关:** [Storages.pinCache](Storages.md#pincache)

---

### isCachePinned

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要判定的文件的存储名。 |

**返回值**

处于 pin 状态则返回真，否则返回假。

**说明**

判断 cache 条目是否被 pin

返回指定路径在 file 层或 decode 层是否处于 pin 状态。

**相关:** [Storages.pinCache](Storages.md#pincache) / [Storages.unpinCache](Storages.md#unpincache)

---

### getFileCacheList

方法

**返回值**

cache 条目的字典数组。

**说明**

获取 file 层缓存列表

以字典数组返回 file 层缓存 ( `requestCache` 系确保的二进制 ) 的条目
列表。

各条目持有以下键。

- `path`        : 规范化后的存储路径 ( String )
- `size`        : 字节数 ( Integer )
- `lastaccess`  : 最后访问时间 ( 平台相关的整数 )
- `usecount`    : 当前的引用计数 ( Integer )
- `pinned`      : pin 状态 ( 0 or 1 )

**相关:** [Storages.dumpFileCacheList](Storages.md#dumpfilecachelist) / [Storages.getImageCacheList](Storages.md#getimagecachelist)

---

### getImageCacheList

方法

**返回值**

cache 条目的字典数组。

**说明**

获取 decode 层缓存列表

以字典数组返回 decode 层缓存 ( 解码完成的 Bitmap ) 的条目列表。

各条目持有以下键。

- `path`    : 规范化后的存储路径 ( String )
- `keyidx`  : 同一路径内的变体编号 ( Integer )
- `mode`    : 读取模式 ( Integer; 内部常量 )
- `dw, dh`  : 显示大小 ( Integer )
- `width, height` : 原始 Bitmap 大小 ( Integer )
- `bytes`   : 占用字节数 ( Integer )
- `pinned`  : pin 状态 ( 0 or 1 )

**相关:** [Storages.dumpImageCacheList](Storages.md#dumpimagecachelist) / [Storages.getFileCacheList](Storages.md#getfilecachelist)

---

### dumpFileCacheList

方法

**说明**

输出 file 层缓存列表的日志

以 WARNING 级别把 file 层缓存条目列表输出到日志。
MASTER 构建中也会输出。与 REPL 的 `.fcache` 同等。

**相关:** [Storages.getFileCacheList](Storages.md#getfilecachelist) / [Storages.dumpImageCacheList](Storages.md#dumpimagecachelist)

---

### dumpImageCacheList

方法

**说明**

输出 decode 层缓存列表的日志

以 WARNING 级别把 decode 层缓存条目列表输出到日志。
MASTER 构建中也会输出。与 REPL 的 `.icache` 同等。

**相关:** [Storages.getImageCacheList](Storages.md#getimagecachelist) / [Storages.dumpFileCacheList](Storages.md#dumpfilecachelist)

---

### rollbackSavedata

方法

**说明**

回滚存档数据

丢弃对存档数据区域的写入，返回到最后提交的状态。

**相关:** [Storages.commitSavedata](Storages.md#commitsavedata)

---

### setCacheMaxSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `size` | `&nbsp;` | 以“字节单位”指定缓存的最大大小<br>( 不是条目数 )。 |

**说明**

设置文件缓存的最大大小

设置 `Storages.requestCache` 系所保持的文件缓存整体的最大大小。
已缓存文件的合计大小超过该值时，会从旧
条目开始依次被丢弃。默认值为 200MB ( 200 * 1024 * 1024 )。

---

### fstat

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定对象的存储名。 |

**返回值**

返回 `%[ size, mtime ]` 的字典。无法打开时抛出异常。

**说明**

获取文件的大小与更新时间

以字典返回指定存储的大小和最后更新时间。

- `size` … 文件大小 ( 字节数 )
- `mtime` … 最后更新时间 ( Date 对象 )。无法取得时间时不会放入

归档内的文件或插件提供的介质 ( `proxy://` 等 ) 没有实际文件，
因此只放入 `size`。

在加载了 fstat 插件的环境中，会被替换为插件版 ( 也返回 `atime` / `ctime` )。
想以数值比较更新时间时，请使用
[Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime)。

**相关:** [Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime)

---

### getTime

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 指定对象的文件或文件夹的存储名。 |

**返回值**

返回 `%[ mtime ]` 的字典。找不到时抛出异常。

**说明**

获取更新时间

以 `%[ mtime ]` 的字典返回本地实际文件或文件夹的最后更新时间
( `mtime` 是 Date 对象 )。归档内的文件不能作为对象。

在加载了 fstat 插件的环境中，会被替换为插件版 ( 也返回 `ctime` / `atime` )。

**相关:** [Storages.fstat](Storages.md#fstat) / [Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime)

---

### createDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要创建的目录的存储名。 |

**返回值**

能创建则返回真，不能则返回假。

**说明**

创建目录

创建指定的目录。如果中途的层级不存在，也会一并创建。

**相关:** [Storages.removeDirectory](Storages.md#removedirectory)

---

### removeDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定要删除的目录的存储名。 |

**返回值**

能删除则返回真，不能则返回假。

**说明**

删除目录

删除指定的目录。如果里面还残留文件则不会删除。

**相关:** [Storages.createDirectory](Storages.md#createdirectory)

---

### copyFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 指定复制源的存储名。 |
| `to` | `&nbsp;` | 指定复制目标的存储名。 |
| `failIfExist` | `false` | 指定真时，如果复制目标已存在则什么都不做并返回假。<br>为假 ( 默认 ) 时则覆盖。 |

**返回值**

能复制则返回真，因复制目标存在而中止时返回假。

**说明**

复制文件

把存储空间中的文件复制到别的存储名。
复制源也可以是归档内的文件。

**相关:** [Storages.exportFile](Storages.md#exportfile)

---

### exportFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要写出的文件的存储名。 |
| `dest` | `&nbsp;` | 指定写出目标的存储名。 |

**说明**

写出文件

把存储空间中的文件 ( 包含归档内的文件 ) 写出到指定的存储名。
如果写出目标已存在则覆盖。

**相关:** [Storages.copyFile](Storages.md#copyfile)

---

### truncateFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定对象的存储名。 |
| `size` | `&nbsp;` | 指定截断后的大小 ( 字节数 )。 |

**返回值**

能截断则返回真，不能则返回假。

**说明**

截断文件

把本地实际文件截断到指定的大小。
成功后会丢弃该文件的读取缓存。

---

### getMD5HashString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定对象的存储名。 |

**返回值**

返回 32 个字符的 16 进制字符串 ( 小写 )。无法打开时抛出异常。

**说明**

获取 MD5 哈希值

返回指定存储内容的 MD5 哈希值。
归档内的文件也可以作为对象。

---

### getTemporaryName

方法

**返回值**

返回临时文件名。

**说明**

获取临时文件名

发放 1 个可用于临时文件的本地文件名。

存放位置是 OS 的临时文件夹 (Windows 按环境变量 TMP → TEMP → USERPROFILE 的顺序)。
无法写入那里时，或在不含任何环境变量的状态下启动而变成了 Windows 目录时，
会在日志中输出警告，并使用存档数据的文件夹
([System.dataPath](System.md#datapath))。取出归档内的插件 DLL 时
也使用相同的位置。

---

### isExistentStorageNoSearchNoNormalize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要确认的存储名。 |

**返回值**

存在则返回真，不存在则返回假。

**说明**

不经规范化与搜索的存在确认

既不进行路径的规范化，也不从自动搜索路径搜索，确认存储是否存在。

**相关:** [Storages.isExistentStorage](Storages.md#isexistentstorage)

---

### clearStorageCaches

方法

**说明**

丢弃存储的缓存

丢弃归档 ( XP3 ) 的分段缓存和自动搜索路径的缓存。
在引擎之外添加或删除文件之后调用。

---

## 插件扩展: fstat

伪代码形式的手册

Copyright 2007 GoWatanabe

### 成员列表

#### 方法

- [fstat](#fstat)
- [exportFile](#exportfile)
- [deleteFile](#deletefile)
- [truncateFile](#truncatefile)
- [moveFile](#movefile)
- [dirlist](#dirlist)
- [dirlistEx](#dirlistex)
- [dirtree](#dirtree)
- [removeDirectory](#removedirectory)
- [createDirectory](#createdirectory)
- [createDirectoryNoNormalize](#createdirectorynonormalize)
- [changeDirectory](#changedirectory)
- [setFileAttributes](#setfileattributes)
- [resetFileAttributes](#resetfileattributes)
- [getFileAttributes](#getfileattributes)
- [selectDirectory](#selectdirectory)
- [isExistentDirectory](#isexistentdirectory)
- [getTime](#gettime)
- [setTime](#settime)
- [getLastModifiedFileTime](#getlastmodifiedfiletime)
- [setLastModifiedFileTime](#setlastmodifiedfiletime)
- [copyFile](#copyfile)
- [copyFileNoNormalize](#copyfilenonormalize)
- [isExistentStorageNoSearchNoNormalize](#isexistentstoragenosearchnonormalize)
- [getDisplayName](#getdisplayname)
- [getMD5HashString](#getmd5hashstring)
- [searchPath](#searchpath)
- [getTemporaryName](#gettemporaryname)

---

### fstat

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

**返回值**

存放属性信息的字典
size: 文件大小
mtime: 更新日期时间 (Date 对象)
atime: 访问日期时间 (Date 对象)
ctime: 创建日期时间 (Date 对象)

**说明**

获取文件属性

※本体中也有同名方法，但加载本插件后
会被这个版本覆盖。与本体版的差异: 本体版只返回 size 和 mtime，不返回 atime / ctime。

---

### exportFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 保存源文件 |
| `dest` | `&nbsp;` | 保存目标文件 |

**说明**

抽取吉里吉里存储空间中的文件

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.exportFile](Storages.md#exportfile)。

---

### deleteFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` | 删除对象文件 |

**返回值**

实际被删除则为 true
仅在存在实际文件时才会被删除

**说明**

删除吉里吉里存储空间中的指定文件。

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.deleteFile](Storages.md#deletefile)。

---

### truncateFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` | 文件 |
| `size` | `&nbsp;` | 指定大小 |

**返回值**

能更改大小则为 true
仅在存在实际文件时才会处理

**说明**

更改吉里吉里存储空间中的指定文件的大小 ( 截断 )

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.truncateFile](Storages.md#truncatefile)。

---

### moveFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fromFile` | `&nbsp;` | 移动对象文件 |
| `toFile` | `&nbsp;` | 移动目标路径 |

**返回值**

实际被移动则为 true
仅在移动对象文件实际存在、且移动目标路径中没有文件时才会移动
※路径不会经过 Normalize/Placed 检查，请填写完整路径

**说明**

移动指定的文件。

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.moveFile](Storages.md#movefile)。

---

### dirlist

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |

**返回值**

存放文件名列表的数组

**说明**

获取指定目录的文件列表

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.dirlist](Storages.md#dirlist)。

---

### dirlistEx

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |

**返回值**

存放文件信息列表的数组
[ %[ name:文件名, size, attrib, mtime, atime, ctime ], ... ]
与 dirlist 不同，name 中对于文件夹不会附加末尾的 "/"，请注意 ( 通过 attrib 判断 )

**说明**

获取指定目录的文件列表和详细信息

---

### dirtree

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |
| `dironly` | `false` | 仅文件夹名，排除文件 |

**返回值**

存放列表的数组 ( 不是树结构，而是包含子文件夹的全部列举 )
列表中不包含 ./ ../ 系的自身与父级引用

**说明**

获取指定目录以下的文件与文件夹列表 ( 包含子文件夹 )

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.dirtree](Storages.md#dirtree)。

---

### removeDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |

**返回值**

实际被删除则为 true
仅在目录中没有文件时才会被删除

**说明**

删除指定的目录

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.removeDirectory](Storages.md#removedirectory)。

---

### createDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |

**返回值**

实际创建成功则为 true

**说明**

创建目录

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.createDirectory](Storages.md#createdirectory)。

---

### createDirectoryNoNormalize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |

**返回值**

实际创建成功则为 true

**说明**

不经路径规范化创建目录

( 目录名不会被转换为小写 )

---

### changeDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |

**返回值**

实际更改成功则为 true

**说明**

更改当前目录

---

### setFileAttributes

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |
| `attr` | `&nbsp;` | 要设置的属性(FILE_ATTRIBUTE_READONLY,FILE_ATTRIBUTE_HIDDEN,...) |

**说明**

设置文件的属性

---

### resetFileAttributes

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |
| `attr` | `&nbsp;` | 要解除的属性(FILE_ATTRIBUTE_READONLY,FILE_ATTRIBUTE_HIDDEN,...) |

**说明**

解除文件的属性

---

### getFileAttributes

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件/目录名 |

**返回值**

获取到的属性(FILE_ATTRIBUTE_READONLY,FILE_ATTRIBUTE_HIDDEN,...)

**说明**

获取文件的属性

---

### selectDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `params` | `%[name:"", title:"", window:void, rootDir:""]` | 设置与 selectFile 相同的参数 |

**返回值**

选择文件夹并按下 OK 按钮则为真，按下取消按钮则为假
params.name 指定文件夹名。按下 OK 按钮时，所选的文件夹会被设置到该成员
params.title 显示对话框的标题
params.window 指定打开对话框的 Window 对象 (void 时为 mainWindow，未指定时为桌面成为所有者窗口。所有者窗口为桌面时为无模式)
params.rootDir 指定文件夹选择的根 ( 仅显示该文件夹以下 )

**说明**

打开文件夹选择对话框

※在引擎本体中已实现 Storages.selectDirectory 的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。

---

### isExistentDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 目录名 |

**返回值**

目录存在则为 true/不存在则为 -1/不是目录则为 false

**说明**

目录的存在检查

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.isExistentDirectory](Storages.md#isexistentdirectory)。

---

### getTime

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 对象文件或目录 |

**返回值**

存放时间戳信息的字典
mtime: 更新日期时间 (Date 对象)
atime: 访问日期时间 (Date 对象)
ctime: 创建日期时间 (Date 对象)
⇒与 fstat 的差异是仅限非归档文件，且不返回 size
※引擎本体中也有同名方法，但加载本插件后
会被这个版本覆盖。与引擎本体版的差异: 引擎本体版只返回 mtime，不返回 ctime / atime。

**说明**

获取时间戳

---

### setTime

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 对象文件或目录 |
| `times` | `&nbsp;` | 存放时间戳信息的字典<br>mtime: 更新日期时间 (Date 对象)<br>atime: 访问日期时间 (Date 对象)<br>ctime: 创建日期时间 (Date 对象) |

**返回值**

是否成功

**说明**

设置时间戳

---

### getLastModifiedFileTime

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 对象文件或目录 |

**返回值**

时间 (WINDOWS 的 FILETIME 64bit 值)

**说明**

获取更新日期 ( 高速版 )

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime)。

---

### setLastModifiedFileTime

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 对象文件或目录 |
| `time` | `&nbsp;` | 时间 (WINDOWS 的 FILETIME 64bit 值) |

**返回值**

是否成功

**说明**

设置更新日期 ( 高速版 )

---

### copyFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 复制源文件 |
| `to` | `&nbsp;` | 复制目标文件 |
| `failIfExist` | `&nbsp;` | 文件存在时失败则为 ture，覆盖则为 false |

**返回值**

实际复制成功则为 true

**说明**

复制吉里吉里存储空间中的指定文件

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.copyFile](Storages.md#copyfile)。

---

### copyFileNoNormalize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 复制源文件 |
| `to` | `&nbsp;` | 复制目标文件 |
| `failIfExist` | `&nbsp;` | 文件存在时失败则为 ture，覆盖则为 false |

**返回值**

实际复制成功则为 true
※to 必须像“file://./c/~”这样以完整路径记述，否则会抛出异常

**说明**

不经路径规范化复制吉里吉里存储空间中的指定文件

( 复制目标文件的文件名不会被转换为小写 )

---

### isExistentStorageNoSearchNoNormalize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |

**返回值**

文件存在则为 true

**说明**

不经路径规范化，也不从 autoPath 搜索，
进行文件的存在确认

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.isExistentStorageNoSearchNoNormalize](Storages.md#isexistentstoragenosearchnonormalize)。

---

### getDisplayName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 ( 父目录以上的路径会被丢弃，请注意 )。 |

**返回值**

显示名

**说明**

获取显示名

返回在资源管理器中实际显示的文件名 ( 依据 SHGetFileInfo )

---

### getMD5HashString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 对象文件名 |

**返回值**

哈希值 ( 32 个字符的 16 进制哈希字符串 ( 小写 ) )

**说明**

获取 MD5 哈希值

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.getMD5HashString](Storages.md#getmd5hashstring)。

---

### searchPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 搜索对象文件名 |
| `searchpath` | `&nbsp;` | 搜索对象路径 ( 本地表记 (c:\~ 等 )，以 ";" 分隔，省略时为系统的默认搜索路径 ) |

**返回值**

未找到时为 void，找到时为文件的完整路径 (file://./~)

**说明**

搜索路径

---

### getTemporaryName

方法

**返回值**

临时文件名 ( TVPGetTemporaryName() 的字符串 )

**说明**

获取临时文件名

※在引擎本体中已有同名方法的环境中会使用引擎本体版
( 本插件仅在引擎本体没有该方法的旧环境中进行补充注册 )。
规格请参照引擎本体的 [Storages.getTemporaryName](Storages.md#gettemporaryname)。

---

## 插件扩展: memfile

伪代码形式的手册

通过 mem://./文件名 可以将其作为在内存中确保的文件进行访问。

### 成员列表

#### 方法

- [isExistMemoryFile](#isexistmemoryfile)
- [isExistMemoryDirectory](#isexistmemorydirectory)
- [deleteMemoryFile](#deletememoryfile)
- [deleteMemoryDirectory](#deletememorydirectory)
- [getMemoryFileInfo](#getmemoryfileinfo)
- [getMemoryFileData](#getmemoryfiledata)
- [getMemoryDirectory](#getmemorydirectory)

---

### isExistMemoryFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 对象文件名 ( 不带 mem:/// ) |

**返回值**

存在则为 true

**说明**

确认内存文件是否存在

---

### isExistMemoryDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

**返回值**

存在则为 true

**说明**

确认内存目录是否存在

---

### deleteMemoryFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 对象文件名 ( 不带 mem:/// ) |

**返回值**

文件被删除则为 true

**说明**

删除内存文件

---

### deleteMemoryDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dirname` | `&nbsp;` | 对象目录名 ( 不带 mem:/// ) |

**返回值**

目录被删除则为 true

**说明**

删除内存目录

---

### getMemoryFileInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 对象文件名 ( 不带 mem:/// ) |

**返回值**

文件信息 %[name:名称, size:大小, isDirectory:是目录则为 true]

**说明**

获取内存文件信息

---

### getMemoryFileData

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 对象文件名 ( 不带 mem:/// ) |

**返回值**

文件存在则以 octet 返回内容。没有则为 void

**说明**

获取内存文件信息

---

### getMemoryDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dirname` | `&nbsp;` | 对象目录名 ( 不带 mem:/// ) |

**返回值**

文件信息的数组 %[name:名称, size:大小, isDirectory:是目录则为 true]

**说明**

获取内存目录信息

---

## 插件扩展: minizip

Storages 类功能扩展

### 成员列表

#### 方法

- [mountZip](#mountzip)
- [unmountZip](#unmountzip)

---

### mountZip

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 域名 |
| `zipfile` | `&nbsp;` | 要挂载的 ZIP 文件名 |

**返回值**

挂载成功则为 true

**说明**

把 zip 文件作为文件系统挂载

通过 zip://域名/文件名 可以访问。会变为只读。

---

### unmountZip

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 域名 |

**返回值**

卸载成功则为 true

**说明**

卸载 zip 文件

---
