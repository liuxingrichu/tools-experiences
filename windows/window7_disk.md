## Windows 硬盘问题 ##
- 现象
	- windows 检测到一个硬盘问题
- 原因
	- 硬盘有磁盘坏块
- 解决方法
	- 硬盘有磁盘坏道了，从现在开始到修复之前不要再运行任何大型程序、游戏了。
应该做的是进行磁盘修复，就在和碎片整理相同的地方：打开我的电脑，在C盘上点右键 - 属性 - 工具 - 差错->开始检查，把“自动修复...”和“扫描并试图恢复坏扇区”都选上，然后开始检查。（D\E\F\G盘也要这样，分别都做个检查），对每个盘都检查完了重新启动电脑，重新启动后电脑进行的自动扫描让它扫描完，不要取消。
如果对DOS比较熟悉，也可以进入DOS输入“chkdsk c: /f”进行磁盘检查，对D/E/F/G分别作相同的处理，比如D盘用 chkdsk d: /f
