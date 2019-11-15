# Linux实验系统linuxer的安装

## 环境安装
### 安装jupyter notebook
安装pip3，再安装jupyter
#### 1）安装pip3
```bash
apt install python3-pip
```
#### 2）安装jupyter notebook
```bash
pip3 install jupyter
```
#### 3）安装bash kernel
```bash
pip3 install bash_kernel

python3 -m bash_kernel.install
```

## 客户端程序安装

### 实验系统下载

```bash
git clone ssh://git@vlab.cs.swust.edu.cn:2222/linuxCourse/linux2019/linuxer.git
```

下载后目录为linuxer，包含几个目录：

* bin/

客户端程序为linuxer.bash，服务器端程序为server.bash, server-students.bash和server-teachers.bash。

* doc/

安装文档

* etc/

客户端程序配置文件client.conf，服务器端程序配置文件server.conf，服务器端配置文件sudoers.d/

* labs/

实验资源，包括指导书和相关文件。例子中仅包含lab4/目录，也就是第4次实验的材料。

* lib/

客户端程序函数库cliet.lib，服务器端程序函数库server.lib。

* score/

服务器端保存的实验成绩，名称为lab1, lab2, lab3,....

* Makefile

以make工具简化客户端程序测试过程，主要的命令包括：

  * make

启动客户端程序。

  * make install

安装客户端程序。

  * make uninstall

卸载客户端程序。

  * make test

启动客户端程序。

  * make help

显示简短帮助（未实现）。

* README

实验系统介绍以及使用说明。

### 实验系统安装

```bash
cd linuxer

make install
```

### 客户端环境配置

* 文件批量上传工具wput安装

```bash
apt install wput
```

## 配置服务器端环境

#### 1）增加帐号
* 服务帐号linuxer

```bash
useradd -m -s /opt/linuxer/bin/server.bash linuxer
```

* 教师帐号teacher

```bash
useradd -m -G sudo -s /opt/linuxer/bin/server-teachers.bash teacher
```

#### 2）设置口令
* 服务帐号linuxer

```bash
passwd linuxer
```

* 教师帐号linuxer

```bash
passwd teacher
```

*注意:*需要记住这两个口令，客户端程序需要写入。

#### 3）设置权限

* 设置linuxer帐号可创建帐号

拷贝实验系统目录中的文件etc/sudoers.d/linuxer到/etc/sudoers.d/目录中。

```bash
cp etc/sudoers.d/linuxer /etc/sudoers.d/
```

etc/sudoers.d/linuxer文件用于配置sudo功能，实现授权特定用户以管理员身份执行某些命令，内容如下：

```
# Cmnd alias specification
Cmnd_Alias LINUXER=/usr/bin/passwd, /usr/sbin/groupadd, /usr/sbin/userdel, /usr/sbin/useradd, /bin/mkdir, /bin/chown, /bin/chmod
# User privilege specification
linuxer ALL=(ALL) NOPASSWD: LINUXER
```

#### 4）安装vsftpd

```bash
apt install vsftpd

systemctl enable vsftpd.service
```

配置vsftpd允许用户修改文件系统，修改/etc/vsftpd.conf文件，取消下面一行的注释：

`write_enable=YES`

允许用户上传文件，在`/etc/shells`文件中添加下面内容：

```
/opt/linuxer/bin/server.bash
/opt/linuxer/bin/server-students.bash
/opt/linuxer/bin/server-teachers.bash
```