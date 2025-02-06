# ThriveX

部署之前,需要获取相关平台API信息,请参考[API获取](https://docs.liuyuyang.net/docs/%E9%A1%B9%E7%9B%AE%E9%83%A8%E7%BD%B2/API/%E9%AB%98%E5%BE%B7%E5%9C%B0%E5%9B%BE.html)


# 依赖安装

> 在进行部署前,请确保服务器已安装`docker`和`docker-compose`、`git`、`docker-compose-plugin`

## 配置源

https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/

> 安装依赖之前,请先配置镜像源,否则无法安装`docker-ce`及`docker-compose-plugin`

## YUM

```shell
yum clean all&&yum makecache &&yum install docker-ce docker-compose git docker-compose-plugin -y
```

## APT

```shell
apt update && apt install docker-ce docker-compose git docker-compose-plugin -y
```


## 安装requests

```shell
pip3 install requests==2.31.0
```

> 请使用`root`用户执行以上命令

# 部署教程-一键

[脚本: 一键部署](doc/py.md)


# 部署教程-手动

> 基于阿里云基础镜像构建,无需配置镜像加速器

## 使用外部数据库

[文档: 我有自己的数据库](doc/nosql.md)

## 使用全量

[文档: 使用全新的数据库服务](doc/sql.md)


## 使用本地构建所有镜像

[文档: 我想自己构建-此方法对机器配置要求略高](build.md)


## 部署教程-手动运行容器

[部署教程-手动运行容器](program/readme.md)


# 更多

[一键更新镜像](doc/pull.md)

[开发版手动部署](doc/upDev.md)

# 默认账号密码

```shell
admin
```

```shell
123456
```