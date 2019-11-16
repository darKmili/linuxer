# Linux实验系统linuxer的安装

## 实验系统安装

### 源代码下载

```bash
git clone ssh://git@vlab.cs.swust.edu.cn:2222/linuxCourse/linux2019/linuxer.git
```

生成目录`linuxer/`，包含几个子目录和文件：

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

该文件用于使用make工具简化实验系统测试过程，主要的命令包括：

  1) make

启动客户端程序。

  2) make install

安装实验系统。

  3) make uninstall

卸载实验。

  4) make test

启动客户端程序。

  5) make help

显示简短帮助（未实现）。

* README

实验系统介绍。

### 实验系统安装

```bash
cd linuxer

make install
```

## 客户端环境配置

### 安装jupyter notebook

首先安装pip3，再安装jupyter

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
```

```bash
python3 -m bash_kernel.install
```

### 安装文件批量上传工具wput

```bash
apt install wput
```

## 服务器端环境配置

### 安装jupyter notebook

同客户端环境配置“安装jupyter notebook”部分。

### 安装SSHD

SSHD服务用于远程使用服务器端功能。

```bash
apt install openssh-server
```

### 安装vsftpd

vsftpd用于客户端上传文件。

```bash
apt install vsftpd
```

```bash
systemctl enable vsftpd.service
```

配置vsftpd允许用户修改文件系统，修改/etc/vsftpd.conf文件，取消下面一行的注释：

```bash
write_enable=YES
```

允许用户上传文件，在`/etc/shells`文件中添加下面内容：

```
/opt/linuxer/bin/server.bash
/opt/linuxer/bin/server-students.bash
/opt/linuxer/bin/server-teachers.bash
```

### 增加服务器端帐号

* 服务帐号linuxer

```bash
useradd -m -s /opt/linuxer/bin/server.bash linuxer
```

* 教师帐号teacher

```bash
useradd -m -G sudo -s /opt/linuxer/bin/server-teachers.bash teacher
```

### 设置口令

* 服务帐号linuxer

```bash
passwd linuxer
```

* 教师帐号linuxer

```bash
passwd teacher
```

*注意:*需要记住这两个口令，客户端程序使用过程中需要输入。

### 设置权限

* 设置linuxer帐号可创建帐号

拷贝实验系统目录中的文件`etc/sudoers.d/linuxer`到`/etc/sudoers.d/`目录中。

```bash
cp etc/sudoers.d/linuxer /etc/sudoers.d/
```

**注意：**`etc/sudoers.d/linuxer`文件用于配置sudo功能，用于实现授权特定用户以管理员身份执行某些命令，内容如下：

```
# Cmnd alias specification
Cmnd_Alias LINUXER=/usr/bin/passwd, /usr/sbin/groupadd, /usr/sbin/userdel, /usr/sbin/useradd, /bin/mkdir, /bin/chown, /bin/chmod
# User privilege specification
linuxer ALL=(ALL) NOPASSWD: LINUXER
```