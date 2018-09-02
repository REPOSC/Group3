# 弗恩英语阅读应用  IfLight组部署文档

#### 1. 安装操作系统

------

> 安装 Windows 10 64位专业版，主版本号 1803。

#### 2. 克隆项目到本地

-------------------------------------------------------

> 从[官网](https://git-scm.com/download/win)上下载最新版本的Git安装包，安装中使用默认配置，单击“下一步”，直到完成安装。
>
> 在命令行窗口中执行`git config --global core.autocrlf false`用于修改回车换行符的相关配置。
>
> 在命令行内输入如下命令来初始化git账户：
>
> ​        初始化姓名：`git config --global user.name  +  “自己的名字”`
>
> ​        初始化邮箱：`git config --global user.email  +  “自己的邮箱”`
>
> 选择需要的项目文件夹在Git命令行中执行`git clone https://se.jisuanke.com/english-reading/Group3`， 输入用户名和密码完成克隆。

#### 3. 下载安装虚拟机所需软件

----

> 从[官网](https://www.vagrantup.com/downloads.html)上下载最新版本的Vagrant for Windows 64-bit安装包，安装中使用默认配置，单击“下一步”，直到完成安装。
>
> 从[官网](https://www.virtualbox.org/wiki/Downloads)上下载最新版本的VirtualBox for Windows安装包，安装中始终单击“下一步”，直到完成安装。
>
> 从[官网](https://nodejs.org/en/)上下载最新版本的Node.js安装包，安装中始终单击“下一步”，直到完成安装。

#### 4. 安装虚拟机及配置虚拟机环境

---

> 在项目文件夹中双击执行pre_boot.bat，用于安装Fedora系统，等待安装结束后进入Fedora虚拟机环境。
>
> 在虚拟机环境中输入`cd /vagrant`，然后执行共享目录中的boot.sh，即输入 `./boot.sh`。
>
> 执行完后在虚拟机环境中执行`python manage.py createsuperuser`，创建超级管理员一名，创建成功后执行`python manage.py runserver 0.0.0.0:8000`，启动后端服务器。

#### 5. 启动本地服务器

------

> 在项目文件夹中双击执行 pre_boot.bat，用于安装程序运行所需的依赖。运行完毕后依次点击执行 runfirst.bat 和 runsecond.bat，并保持打开，以运行本地端口服务器。

#### 6. 预览项目

------

> 打开谷歌浏览器，在地址栏输入 localhost:8080（如果端口被占用可以尝试8081端口），可以进行管理后台的预览。（如果关闭 runfirst.bat，可以在 frontend 文件夹内使用命令行运行 `npm run dev` 来启动服务器。）
>
> 在[官网](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html?t=18080816)上下载最新版本的小程序开发客户端，安装中始终单击“下一步”，直到完成安装。
>
> 在Windows环境下，官方的开发客户端中点击“新建”并选择前端目录frontend2，可以进行微信小程序的预览操作。（如果关闭 runsecond.bat，可以在 frontend2 文件夹内使用命令行运行 `npm run dev` 来启动服务器。）

#### 7.帮助文档及使用手册

> 我们撰写了分角色使用手册：《弗恩英语阅读小程序用户使用手册》和《弗恩英语阅读后台管理平台使用手册》，并且编写了api帮助文档。其中api帮助文档可以通过打开项目根目录的 `help` 文件夹下的`index.html`来阅读。