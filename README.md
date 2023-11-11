# MySublimeTextSettings
前排提示，为作者本人的个人配置，XCPC算法向(c++)
包含`FastOlympicCoding`,`FastOlympicCodingHook`,`sublimelinter`,`sublimelinter-gcc`等刷题用插件<br>和一些基础配置(包括`git`,`ConvertUTF-8`等)
## 为什么选择 SublimeText
从cp-editor转过来，一个很让人头疼的原因是，cp-editor配置clang后的语法检查依然非常的鸡肋，没有具体的错误信息页没有快捷键支持。代码片段的导入也差点意思。
当然，如果你还不了解[cp-editor](https://cpeditor.org/zh/),它快速导入测试样例和远程提交的特色或许会成为你不错的选择。

## 使用说明
绿色版，git clone或者下载压缩包，点击`sublime_text.exe`即可运行

## 初始快捷键与如何修改
1. listen to CC  `ctrl+shift+o`  在热键设置中修改
2. 删除exe和__texts文件 `ctrl+shift+x` 在热键设置中修改
3. 运行测试用例 `ctrl+'` 
<br>在 `SublimeText\Data\Packages\CppFastOlympicCoding\Default(windows).sublime-keymap`中修改
   **！！注意，如果你用Vscode或者sublime打开是空白！！不要保存，修改后缀为txt修改内容后保存**
4. g++语法检查器，`ctrl+k`开始检查，然后`ctrl+shift+a`可以看到详细错误提示
   在`设置->packages settings->sublimelinet->key bindings`进行修改
5. 下载FiraCode字体，[FiraCode](https://github.com/tonsky/FiraCode)下载右键安装即可，如果不想使用，记得在用户设置中修改