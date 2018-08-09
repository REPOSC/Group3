# 项目 III 环境配置文档

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

#### 3. 创建并安装虚拟机

----

> 从[官网](https://www.vagrantup.com/downloads.html)上下载最新版本的Vagrant for Windows 64-bit安装包，安装中使用默认配置，单击“下一步”，直到完成安装。
>
> 从[官网](https://www.virtualbox.org/wiki/Downloads)上下载最新版本的VirtualBox for Windows安装包，安装中始终单击“下一步”，直到完成安装。
>
> 在项目文件夹中双击执行pre_boot.bat，用于安装Fedora系统和配置Eslint代码检查工具，等待安装结束并进入Fedora虚拟机环境。

#### 4. 配置虚拟机环境

---

> 在虚拟机环境中输入cd /vagrant，然后以管理员身份执行共享目录中的boot.sh，即输入sudo ./boot.sh，保持联网状态完成基本的环境配置。（如果中间出现了下载失败或者停滞的状况，可能是网络不好或者被墙了，尝试多次即可）
>
> 进入vagrant下的eng_project/frontend目录下，输入npm run dev可以暂时将网站搭建在本机服务器上。

#### 5. 安装微信小程序官方开发端用于预览

--------

> 在[官网](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html?t=18080816)上下载最新版本的小程序开发客户端，安装中始终单击“下一步”，直到完成安装。
>
> 在Windows环境下，官方的开发客户端中点击“新建”并选择共享文件夹下的前端目录frontend，可以进行预览操作。

#### 6. 安装编辑器

---

> 在[官网](https://code.visualstudio.com/download)上下载最新版本的VS Code，安装中始终单击“下一步”，直到完成安装。
