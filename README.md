# 项目 III 部署配置文档

#### 1. 安装操作系统

------

> 安装 Windows 10 64位专业版， 主版本号 1803。

#### 2. 克隆项目到本地

-------------------------------------------------------

> 从[官网](https://git-scm.com/download/win)上下载最新版本的Git安装包，安装中使用默认配置，单击“下一步”，直到完成安装。
>
> 在命令行窗口中执行 git config --global core.autocrlf false 用于修改回车换行符的相关配置。
>
> 选择需要的项目文件夹在Git命令行中执行 git clone https://se.jisuanke.com/english-reading/Group3， 输入用户名和密码完成克隆。

#### 3. 下载安装依赖所需的包管理工具

----

> 从[官网](https://nodejs.org/en/)上下载最新版本的Node.js安装包，安装中始终单击“下一步”，直到完成安装。

#### 4. 配置本地环境

---

> 在项目文件夹中双击执行pre_boot.bat，用于安装程序运行所需的依赖。运行完毕后依次点击执行runfirst.bat和runsecond.bat，并保持打开，以运行本地端口服务器。

#### 5. 预览项目

--------

> 打开谷歌浏览器，在地址栏输入 localhost:8080，可以进行管理后台的预览。
>
> 在[官网](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html?t=18080816)上下载最新版本的小程序开发客户端，安装中始终单击“下一步”，直到完成安装。
>
> 在Windows环境下，官方的开发客户端中点击“新建”并选择前端目录frontend2，可以进行微信小程序的预览操作。
