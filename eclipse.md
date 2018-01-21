## eclipse ##

### 自动提示 ###
打开 Eclipse -> Window -> Perferences -> Java -> Editor -> Content Assist，在右边最下面一栏找到 auto-Activation ，下面有三个选项，找到第二个“Auto activation triggers for Java:”选项 在其后的文本框中会看到一个“.”存在。这表示:只有输入“.”之后才会有代码提示和自动补全，我们要修改的地方就是这里。把该文本框中的“.”换掉，换成“abcdefghijklmnopqrstuvwxyz.”，这样，你在Eclipse里面写Java代码就可以做到按“abcdefghijklmnopqrstuvwxyz.”中的任意一个字符都会有代码提示。

### 显示行号 ###
Window -- Preferences -- General -- Editors -- Text Editors -- show line numbers

### 调整字体 ###
window -》 preferences -》 Generalappearance -》 colors   and   fonts -》 java -》 "java   editor   text  font "，然后点edit，可以设置字体的大小。

### Java注释 ###
/* 注释 */

### XML注释 ###
	<!-- 注释 -->

### 快捷键 ###
1.	自动补全
Alt + /
2.	代码格式化
Ctrl + shift + F
3.	变量定义补全，导入包
Ctrl + 1（数字）
4.	快速导入全部包
Ctrl + shift + O（字母）
5.	父子类关系显示
F4
6.	模拟器横竖显示切换
Ctrl + F12

### 支持python ###
1. 在eclipse目录下，创建links文件夹
2. 在links文件夹目录下，拷贝PyDev
3. 在links文件夹目录下，创建PyDev.link文件
4. 在PyDev.link文件中，书写

	path=D:\\eclipse\\links\\PyDev
