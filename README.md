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
> 在项目文件夹中双击执行pre_boot.bat，等待安装结束并进入Fedora虚拟机环境。

#### 4. 配置虚拟机环境

---

> 在虚拟机环境中输入cd /vagrant，然后以管理员身份执行共享目录中的boot.sh，即输入sudo ./boot.sh，保持联网状态完成基本的环境配置。
>
> 输入npm run dev可以暂时将网站搭建在本机服务器上。

#### 5. 安装微信小程序官方端用于预览

--------

> 在[官网](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html?t=18080816)上下载最新版本的小程序开发客户端，安装中始终单击“下一步”，直到完成安装。

#### 6. 配置代码风格检查工具Eslint

---

> 将克隆下来的仓库中的pre-commit文件复制到.git/hooks文件夹，下次进行代码提交时，就可以自动检查代码。

#### 7. 安装编辑器

---

> 在[官网](https://code.visualstudio.com/download)上下载最新版本的VS Code，安装中始终单击“下一步”，直到完成安装。



 


