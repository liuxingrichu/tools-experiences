# 常用命令 #
	git init							#在当前目录新建一个git代码库
	git clone [url]						#下载一个项目和它的整个代码历史
	【注】url格式 https://github.com/[username]/reposName

	git add [file1] [file2]				#添加指定文件到暂存区
	git rm [file1] [file2]				#删除工作区文件，并且将这次删除放入暂存区
	git mv [file-origin] [file-renamed]	#改名文件，并且将这个改名放入暂存区
	git commit -m [message]				#提交暂存区到仓库
	git commit -m -a [message]			#直接从工作区提交到仓库
	【注】前提该文件已经有仓库中的历史版本

	git status							#显示变更信息
	git log								#显示当前分支的历史版本
	git log --oneline					#每个历史版本显示一行
	git remote add [shortname] [url]	#增加远程仓库，并且命名
	git push [remote] [branch]			#将本地的提交推送到远程仓库
	git pull [remote] [branch]			#将远程仓库的提交拉下到本地

	git reset		# 清除添加信息

# 在线练习 #
https://try.github.io/				

# 安装nodeJS #
npm install git-it -g

# 快捷键 #
Shift + Insert		#粘贴

### 暂存代码 ###
git stash 

git stash save 'xx'

### 异常场景 ###
1. 执行git push https://github.com/xxx.git master命令时，提示
fatal: AggregateException encountered.
	- 解决方法：
		- 方法一. 每次都输入用户名和密码
		- 方法二： git config --global credential.helper wincred

2. 解决本地仓库提交，身份认证
	1. git config --global user.email "liuxingrichu@163.com"
	2. git config --global user.name "liuxingrichu"


3. 解决每次远程提交需要输入账号和密码
	1. git config --global credential.helper store
	