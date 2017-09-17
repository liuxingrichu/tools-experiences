【简介】
OpenVPN是一个用于创建虚拟专用网络(Virtual Private Network)加密通道的免费开源软件。
使用OpenVPN可以方便地在家庭、办公场所、住宿酒店等不同网络访问场所之间搭建类似于局域网的专用网络通道。
OpenVPN允许参与创建VPN的单点使用公开密钥、电子证书、或者用户名／密码来进行身份验证。
它大量使用了OpenSSL加密库中的SSLv3/TLSv1协议函数库。目前OpenVPN能在Solaris、Linux、OpenBSD、FreeBSD、NetBSD、Mac OS X与Windows
 2000／XP／Vista/Windows 7以及Android上运行，并包含了许多安全性的功能。它并不是一个基于Web的VPN软件，也不与IPsec及其他VPN软件包兼容。
 
【加密】
OpenVPN使用OpenSSL库加密数据与控制信息：它使用了OpenSSL的加密以及验证功能，意味着，它能够使用任何OpenSSL支持的算法。
它提供了可选的数据包HMAC功能以提高连接的安全性。此外，OpenSSL的硬件加速也能提高它的性能。

【验证】
OpenVPN提供了多种身份验证方式，用以确认参与连接双方的身份，包括：预享私钥，第三方证书以及用户名／密码组合。预享密钥最为简单，但同时它只能用于创建点对点的VPN；
基于PKI的第三方证书提供了最完善的功能，但是需要额外的精力去维护一个PKI证书体系。
OpenVPN2.0后引入了用户名／口令组合的身份验证方式，它可以省略客户端证书，但是仍有一份服务器证书需要被用作加密。

【网络】
OpenVPN所有的通信都基于一个单一的IP端口，默认且推荐使用UDP协议通讯，同时TCP也被支持。
OpenVPN连接能通过大多数的代理服务器，并且能够在NAT的环境中很好地工作。
服务端具有向客户端“推送”某些网络配置信息的功能，这些信息包括：IP地址、路由设置等。
OpenVPN提供了两种虚拟网络接口：通用Tun/Tap驱动，通过它们，可以创建三层IP隧道，或者虚拟二层以太网，后者可以传送任何类型的二层以太网络数据。
传送的数据可通过LZO算法压缩。IANA（Internet Assigned Numbers Authority）指定给OpenVPN的官方端口为1194。
OpenVPN 2.0以后版本每个进程可以同时管理数个并发的隧道。
OpenVPN使用通用网络协议（TCP与UDP）的特点使它成为IPsec等协议的理想替代，尤其是在ISP（Internet service provider）过滤某些特定VPN协议的情况下。

【安全】
OpenVPN与生俱来便具备了许多安全特性：它在用户空间运行，无须对内核及网络协议栈作修改；初始完毕后以chroot方式运行，放弃root权限；使用mlockall以防止敏感数据交换到磁盘。
OpenVPN通过PKCS#11支持硬件加密标识，如智能卡。


【工作原理】
OpenVPN的大致工作原理就是在服务器端和客户端之间搭建一个独立于当前网络环境的加密通道，
将服务器端和多个客户端组建成一个独立的虚拟局域网，从而实现服务器端和客户端、客户端和客户端之间的相互通信。

【安装】
由于Windows自身的限制，Windows版本的OpenVPN只有具备管理员权限的用户才能成功安装。
当前最新版本的OpenVPN 2.3.0 只能在Windows XP及以上版本的操作系统上安装。
在OpenVPN中，服务器端和客户端使用的是同一个安装文件，安装方法也是一样的，只是配置方法不一样。
其主要区别是，在安装目录的config文件夹下，服务器端配置的文件叫做server.ovpn，客户端配置的文件叫做client.ovpn，当然，配置文件中的内容也不相同。
OpenVPN通过不同的设置来决定该程序是充当服务器端还是客户端。
安装软件时，将OpenSSL Utilities 和OpenVPN RSA Certificate Management Scripts选中，一路默认。
提示安装Tap-Windows时，选中安装

【在服务器端创建加密证书和私钥】
（1）修改”OpenVPN安装目录\easy-rsa\vars.bat.sample“文件中的变量HOME至安装路径，
（2）根据实际情况，修改”OpenVPN安装目录\easy-rsa\vars.bat.sample“文件中的变量如下，
KEY_COUNTRY		国家名称
KEY_PROVINCE	省份名称
KEY_CITY		城市名称
KEY_ORG			组织机构名称
KEY_EMAIL		邮件地址
（3）在作为服务器端的电脑A上打开DOS命令窗口，并进入到%OpenVPN的安装目录%\easy-rsa目录，执行
> init-config 初始化配置，将vars.bat.sample文件拷贝为vars。bat
> vars	设置相应的局部环境变量
> clean-all 相关设置与清理工作
（4）创建CA根证书
> build-ca
一路默认，最后y
（5）创建服务器端证书
> build-key-server server
一路默认，最后y
（6）创建迪菲.赫尔曼密钥
> build-dh
迪菲·赫尔曼密钥交换(Diffie–Hellman key exchange，简称「D–H」) 是一种安全协议。
它可以让双方在完全没有对方任何预先信息的条件下通过不安全信道创建起一个密钥。
这个密钥可以在后续的通讯中作为对称密钥来加密通讯内容。
(7)创建客户端证书
> build-key client
一路默认，最后y
创建多个不同的客户端证书，只需要重复此步骤即可。
切记，Common Name不要重复，这是OpenVPN用来区分不同客户端的关键所在。
（8）生成ta.key：openvpn --genkey --secret keys/ta.key (可选操作)
ta.key主要用于防御DoS、UDP淹没等恶意攻击。
命令中的第3个参数keys/ta.key表示生成的文件路径(含文件名)。

非常重要的提醒：以上命令都是在同一个DOS窗口中执行的，如果你以后需要打开新窗口来执行命令(比如创建新的客户端证书)：
你不需要再执行init-config命令，除非你再次改动了vars.bat.sample文件；
每一次打开新窗口时都需要先执行vars命令，后面才能执行其他命令。

【文件分布配置】
keys文件夹中对应的文件复制到OpenVPN服务器或客户端的安装目录的config文件夹下。

《服务器端config目录需要的文件包括：》
ca.crt
ca.key(核心CA证书和私钥)
dh1024.pem(如果最初的变量KEY_SIZE设为2048，这里就是dh2048.pem)
server.crt
server.key(名称server根据个人设置可能有所不同)
ta.key(名称也可自行设置，如果不需要防御攻击，可以不创建或复制此文件)

《客户端config目录需要的文件包括：》
ca.crt
client.crt
client.key(名称client根据个人设置可能有所不同)
ta.key(如果服务器端具备此文件，客户端也应具备)

【文件内容配置】
在OpenVPN的安装目录的sample-config文件夹中存放有3个示例模板文件：server.ovpn、client.ovpn、sample.ovpn。
复制server.ovpn到服务器的config目录，client.ovpn到客户端的config目录，并在此基础上进行修改。
在OpenVPN的配置文件中，前面带「#」或「;」的表示注释内容。
《server.ovpn》：桥接模式
local 192.168.0.2     #指定监听的本机IP(因为有些计算机具备多个IP地址)，该命令是可选的，默认监听所有IP地址。
port 1194             #指定监听的本机端口号
proto udp             #指定采用的传输协议，可以选择tcp或udp
;dev tun               #指定创建的通信隧道类型，可选tun或tap
dev tap
dev-node tap0
ca ca.crt             #指定CA证书的文件路径
cert server.crt       #指定服务器端的证书文件路径
key server.key    #指定服务器端的私钥文件路径
dh dh1024.pem         #指定迪菲赫尔曼参数的文件路径
;server 10.0.0.0 255.255.255.0   #指定虚拟局域网占用的IP地址段和子网掩码，此处配置的服务器自身占用10.0.0.1。
;ifconfig-pool-persist ipp.txt   #服务器自动给客户端分配IP后，客户端下次连接时，仍然采用上次的IP地址(第一次分配的IP保存在ipp.txt中，下一次分配其中保存的IP)。
server-bridge 192.168.8.4 255.255.255.0 192.168.8.128 192.168.8.254
push "route 192.168.8.4 255.255.255.0"
tls-auth ta.key 0     #开启TLS，使用ta.key防御攻击。服务器端的第二个参数值为0，客户端的为1。
keepalive 10 120      #每10秒ping一次，连接超时时间设为120秒。
comp-lzo              #开启VPN连接压缩，如果服务器端开启，客户端也必须开启
client-to-client      #允许客户端与客户端相连接，默认情况下客户端只能与服务器相连接
persist-key
persist-tun           #持久化选项可以尽量避免访问在重启时由于用户权限降低而无法访问的某些资源。
status openvpn-status.log    #指定记录OpenVPN状态的日志文件路径
verb 3                #指定日志文件的记录详细级别，可选0-9，等级越高日志内容越详细

将server.ovpn放到，服务端OpenVPN安装目录的config文件夹下。

tap模式也就是桥接模式，通过软件在系统中模拟出一个tap设备，该设备是一个二层设备，同时支持链路层协议。
tun模式也就是路由模式，通过软件在系统中模拟出一个tun路由，tun是ip层的点对点协议。

《client.ovpn》
client         #指定当前VPN是客户端
;dev tun        #必须与服务器端的保持一致
dev tap
dev-node tap0
proto udp      #必须与服务器端的保持一致
remote 192.168.0.2 1194      #指定连接的远程服务器的实际IP地址和端口号
resolv-retry infinite    #断线自动重新连接，在网络不稳定的情况下(例如：笔记本电脑无线网络)非常有用。
nobind         #不绑定特定的本地端口号
persist-key
persist-tun
ca ca.crt      #指定CA证书的文件路径
cert client.crt       #指定当前客户端的证书文件路径
key client.key    #指定当前客户端的私钥文件路径
ns-cert-type server      #指定采用服务器校验方式
tls-auth ta.key 1     #如果服务器设置了防御DoS等攻击的ta.key，则必须每个客户端开启；如果未设置，则注释掉这一行；
comp-lzo              #与服务器保持一致
verb 3                #指定日志文件的记录详细级别，可选0-9，等级越高日志内容越详细

将client.ovpn放到，客户端OpenVPN安装目录的config文件夹下。

【服务端创建VLAN与tap】
计算机-》管理-》设备管理器-》网络适配器-》选定小网网卡-》属性-》添加VLAN

双击C:\Program Files\OpenVPN\bin目录下的addtap.bat 文件手动添加tap，每执行一次生成一个tap
根据配置文件的dev-node的名称修改tap虚拟网卡的名称

【服务端生成及配置网桥】
对于Windowx XP或更高版本，从"控制面板->网络连接"中选中TAP-Win32网卡和以太网卡，点击鼠标右键，选择轿接。

设置以太网桥时，应当手动设置以太网桥的IP地址和子网掩码，
不能在配置文件中使用ifconfig命令，因为和TUN/TAP接口不一样，OpenVPN不能通过程序设置桥接接口的IP地址和子网掩码。

【客户端创建tap】
双击C:\Program Files\OpenVPN\bin目录下的addtap.bat 文件手动添加tap
根据配置文件的dev-node的名称修改tap虚拟网卡的名称

【启动OpenVPN服务端和客户端】
服务器端的Windows运行框中输入「services.msc」，进入windows服务界面，启动服务「OpenVPN Service」
也可手动点击OpenVPN图标，来手动启动服务

先启动服务器端，再启动客户端
启动完成后，右键图标，选择需要连接的文件，点击connect
紧接着，就会自动弹出如下窗口，显示连接信息
连接成功后，窗口自动关闭，会显示连接成功提示信息。

至此，OpenVPN已成功运行，即可正常使用；
当然，以上陈述仅限Windows 7系统参考使用，其也是OpenVPN的冰山一角。

【参与资料】
http://www.365mini.com/page/14.htm
https://www.ilanni.com/?p=9847
