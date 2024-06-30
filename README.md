可以部署在本地（windows）和云服务器（我用的是centos7系统）
在 CentOS 上安装 Python 3.11

sudo yum groupinstall "Development Tools"

sudo yum install wget openssl-devel bzip2-devel libffi-devel zlib-devel

cd /usr/local/src

sudo wget https://www.openssl.org/source/openssl-1.1.1k.tar.gz

sudo tar -zxf openssl-1.1.1k.tar.gz

cd openssl-1.1.1k

sudo ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl shared zlib

sudo make

sudo make install

配置系统使用新安装的 OpenSSL：

将系统的默认 OpenSSL 链接到新安装的版本。

sudo mv /usr/bin/openssl /usr/bin/openssl.bak

sudo ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl

echo "/usr/local/openssl/lib" | sudo tee -a /etc/ld.so.conf

sudo ldconfig -v

下载并安装 Python 3.11：

从官方源下载 Python 3.11 并进行编译安装。

cd /usr/local/src

sudo wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz

sudo tar xzf Python-3.11.0.tgz

cd Python-3.11.0

sudo ./configure --prefix=/usr/local/python3.11 --with-openssl=/usr/local/openssl

sudo make

sudo make install

配置系统使用新安装的 Python 3.11：

创建符号链接，使系统能够找到新安装的 Python 3.11。

sudo ln -s /usr/local/python3.11/bin/python3.11 /usr/bin/python3.11

sudo ln -s /usr/local/python3.11/bin/pip3.11 /usr/bin/pip3.11

验证安装：

确认 Python 3.11 和 OpenSSL 版本是否正确。

python3.11 --version

python3.11 -m pip --version

openssl version

安装完成之后就可以运行python了

将所有文件下载至服务器，cd至文件的目录，运行python3.11 api.py，然后在浏览器输入http://你的公网ip:12345就可以使用了

