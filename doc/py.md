# 使用帮助


## 使用Github
```shell
wget -O install.py https://github.com/liumou-site/ThriveX/raw/refs/heads/main/install.py
```

## 使用gitee
```shell
wget -O install.py https://gitee.com/liumou_site/ThriveX/raw/main/install.py
```

## 获取帮助

```shell
root@tb3:/data/git/ThriveX# python3 install.py -h
usage: ThriveXInstall [-h] [-d DIR] [-p PORT] [-u USER] [-P PASSWORD] [-H HOST] [-n NGINX] [-s] [-g] [-b] [-dev] [-update]

当前脚本版本: 1.0

options:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     指定数据库映射路径,默认: /data/ThriveX/mysqll
  -p PORT, --port PORT  指定数据库端口,默认: 3306
  -u USER, --user USER  指定数据库用户名,默认: ThriveX
  -P PASSWORD, --password PASSWORD
                        指定数据库密码,默认: ThriveX@123?
  -H HOST, --host HOST  指定数据库地址,默认: 10.178.178.10
  -n NGINX, --nginx NGINX
                        指定nginx端口,默认: 9007
  -s, --sql             安装sql数据库
  -g, --gitee           使用gitee下载docker-compose文件
  -b, --build           自行构建镜像
  -dev, --dev           使用开发版镜像运行
  -update, --update     更新对应版本镜像
root@tb3:/data/git/ThriveX# 
```


# 安装命令

## github-全球

```shell
python3 install.py
```

## gitee-国内推荐

```shell
python3 install.py -g
```

> 请使用`root`用户执行以上命令