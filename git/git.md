
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

https://try.github.io/				#在线练习

安装nodeJS
npm install git-it -git
