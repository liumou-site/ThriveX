# 使用帮助


## 获取帮助

```shell
root@Debian12:/data# cd ThriveX/
root@Debian12:/data/ThriveX# python3 install.py -h
usage: ThriveXInstall [-h] [-d DIR] [-p PORT] [-u USER] [-P PASSWORD] [-H HOST] [-n NGINX] [-e EMAIL] [-ep EMAIL_PASSWORD] [-b BACKEND] [-t TOML] [-s] [-g] [-dev] [-update] [-c]


options:
  -h, --help            show this help message and exit
  -d, --dir DIR         指定数据库映射路径,默认: /data/ThriveX/mysqll
  -p, --port PORT       指定数据库端口,默认: 3306
  -u, --user USER       指定数据库用户名,默认: ThriveX
  -P, --password PASSWORD
                        指定数据库密码,默认: ThriveX@123?
  -H, --host HOST       指定数据库地址,默认: 10.178.178.10
  -n, --nginx NGINX     [临时弃用]指定nginx端口,默认: 9007
  -e, --email EMAIL     邮箱地址
  -ep, --email_password EMAIL_PASSWORD
                        邮箱密码
  -b, --backend BACKEND
                        指定后端URL,必须 /api结尾且外部浏览器可以访问
  -t, --toml TOML       指定安装信息配置文件路径,当使用此选项时,将忽略其他选项, 例如: -t install.toml
  -s, --sql             安装sql数据库
  -g, --gitee           使用gitee下载docker-compose文件
  -dev, --dev           使用开发版镜像运行
  -update, --update     更新对应版本镜像
  -c, --clean           清除none标签的镜像

root@Debian12:/data/ThriveX# 
```


# 安装命令

## gitee-国内推荐

```shell
python3 install.py
```

> 请使用`root`用户执行以上命令