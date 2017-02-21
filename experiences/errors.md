Python“TypeError: 'NoneType' object is not iterable"
原因带把一个表达式或NONE作为参数提供给函数时，就会引发TYPEERROR，因为这是不可迭代的。

TypeError: 'int' object is not callable
原因：函数名和变量名相同

UnboundLocalError: local variable 'client_obj' referenced before assignment
原因：在选择模式下，某种模式创建client_obj对象，其它模式在未创建该对象，却试图访问该对象的属性或方法

ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
原因: 目标机处于连接状态而终止

fatal: Exiting because of an unresolved conflict.
原因:本地代码与库代码出现冲突
解决方法：git pull origin master
	git merge master
	git status
	git diff
	手工修改代码
	git add .
	git comment -m "xxx"
	git push origin master
