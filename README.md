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

进阶设置：隐藏服务器IP并绕过国内服务器备案机制（小白勿看）

在CentOS 7.6系统上配置Cloudflare Tunnel，需要先安装cloudflared，然后进行隧道的配置。以下是具体步骤：

1. 安装 cloudflared
下载 cloudflared 二进制文件：

wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64

移动文件到适当位置并赋予执行权限：

sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared

sudo chmod +x /usr/local/bin/cloudflared

2. 验证 Cloudflare 账户
3. 
登录 Cloudflare：

cloudflared login

这会打开一个浏览器窗口，让你登录到Cloudflare并授权该服务器的访问。

4. 创建和配置隧道

创建隧道：

cloudflared tunnel create my-tunnel

这个命令会生成一个唯一的隧道ID和证书文件。记住证书文件的路径。

配置隧道流量：

创建或编辑 config.yml 文件，通常位于 ~/.cloudflared/config.yml：

tunnel: <your-tunnel-id>

credentials-file: /path/to/your/credentials-file.json

ingress:
  - hostname: yourdomain.com
    service: http://127.0.0.1:12345
  - service: http_status:404

将 <your-tunnel-id> 替换为实际的隧道ID，将 /path/to/your/credentials-file.json 替换为生成的证书文件的路径，并将 yourdomain.com 替换为你的域名。

4. 启动隧道

运行隧道：

cloudflared tunnel run my-tunnel

6. 更新 DNS 记录

在 Cloudflare 控制面板中，创建 CNAME 记录：

类型: CNAME

名称: yourdomain.com（或你配置的子域名）

目标: <your-tunnel-id>.cfargotunnel.com

8. 配置为服务

为了确保隧道在系统重启后自动启动，可以将其配置为一个 systemd 服务：

创建 systemd 服务文件：


sudo nano /etc/systemd/system/cloudflared.service

在文件中添加以下内容：

ini

[Unit]
Description=cloudflared

After=network.target

[Service]

TimeoutStartSec=0

Type=simple

ExecStart=/usr/local/bin/cloudflared tunnel run my-tunnel

Restart=on-failure

User=root

Group=root

[Install]

WantedBy=multi-user.target

重新加载 systemd 并启动服务：

sudo systemctl daemon-reload

sudo systemctl enable cloudflared

sudo systemctl start cloudflared

完成以上步骤后，你应该可以通过托管的域名访问运行在你本地服务器上的服务（127.0.0.1:12345），并且无需备案。

