远程重启电脑
	> shutdown -r -m 10.0.0.10
	
在当前目录下cmd
	选中目录，输入cmd，回车
	
添加路由
	> route add 172.22.0.3 mask 255.255.0.0 172.22.0.1

删除路由
	> route delete 172.22.0.3 mask 255.255.0.0 172.22.0.1
	
查看路由
	> route print

清除路由表
	> route -F
	> route -f
	
启动windows服务界面	
	Windows运行框中输入「services.msc」
	
过滤检索
	> ipconfig | findstr 192.168.
	

	
	