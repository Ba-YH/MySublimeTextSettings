# MySublimeTextSettings

前排提示，为作者本人的个人配置，XCPC算法向(c++)
包含`FastOlympicCoding`,`FastOlympicCodingHook`,`sublimelinter`,`sublimelinter-gcc`等刷题用插件<br>和一些基础配置(包括`git`,`ConvertUTF-8`等)

## 为什么选择 SublimeText

从cp-editor转过来，一个很让人头疼的原因是，cp-editor配置clang后的语法检查依然非常的鸡肋，没有具体的错误信息页没有快捷键支持。代码片段的导入也差点意思。
当然，如果你还不了解[cp-editor](https://cpeditor.org/zh/),它快速导入测试样例和远程提交的特色或许会成为你不错的选择。

## 使用说明

git clone或者下载压缩包，点击`sublime_text.exe`即可运行

## 快捷键说明

| 操作                                     | 快捷键                | 自定义                                                       |
| ---------------------------------------- | --------------------- | ------------------------------------------------------------ |
| Listen to CC                             | ctrl+shift+o          | 设置->热键设置中修改<br />"command": "fast_olympic_coding_hook"” |
| 运行测试用例                             | ctrl+‘                | 在 `SublimeText\Data\Packages\CppFastOlympicCoding\Default(windows).sublime-keymap`中修改 |
| 删除exe和__tests文件                     | ctrl+shift+c          | 设置->热键设置中修改                                         |
| G++语言检查器<br />开始检查/显示所有错误 | ctrl+k / ctrl+shift+a | 在`设置->packages settings->sublimelinet->key bindings`进行修改 |

## 其它指南

1. [添加代码片段](https://9iphp.com/web/html/sublime-text-code-snippets.html#) 作者的路径在`Data/packages/User/snippet`，有初始和快读模版
2. [添加代码补全方案](https://www.sublimetext.com/docs/completions.html) 在`User`下创建`.sublime-completions`文件写入相关配置
3. 开启FastOlympicCoding的语法检查，在对应设置文件中进行更改，不建议开启，在编码完后使用g++统一查看错误
4. [新建文件自带模版](https://cloud.tencent.com/developer/article/1546590#) 作者有初始模版，所以没有安装，可根据自己的需求进行安装
5. 配置Wakatime，下载插件，在用户设置中填写api即可

## 注意事项

1. 作者使用的字体为[FiraCode](https://github.com/tonsky/FiraCode)，进行下载安装或者在用户设置中更换`font-face`
2. 如果`.sublime-keymap`文件打开是空白，注意！！不要保存，更改文件后缀为`.txt`，进行修改后再改回

	
