### bat脚本 ###
1. 设备变量
	1. set device=abc
2. 打印变量
	1. echo %device%
3. 脚本运行完成后，等待用户确认
	1. pause
4. bat脚本相互调用
	1. call input.bat
5. 输出提示信息
	1. echo hello
6. 关闭命令显示
	1. @echo off
7. 打开命令显示（默认开启）
	1. @echo on
8. 注释（双冒号开头）
	1. ::
9. for循环

		for /l %%i in (1,1,16) do (
			echo %%i
		 )