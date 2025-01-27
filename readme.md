# ThriveX


# 依赖安装

> 在进行部署前,请确保服务器已安装`docker`和`docker-compose`、`git`、`docker-compose-plugin`

## YUM

```shell
yum clean all&&yum makecache &&yum install docker docker-compose git docker-compose-plugin -y
```

## APT

```shell
apt update && apt install docker docker-compose git docker-compose-plugin -y
```

> 请使用`root`用户执行以上命令

# 部署教程-一键

## github-全球
```shell
git clone https://github.com/ThriveX/ThriveX.git&&cd ThriveX/&&bash install.sh
```

## gitee-国内推荐

```shell
git clone https://gitee.com/liumou_site/ThriveX.git&&cd ThriveX/&&bash install.sh
```


# 部署教程-手动

## 依赖安装

> 在进行部署前,请确保服务器已安装`docker`和`docker-compose`、`git`、`docker-compose-plugin`

### YUM

```shell
yum clean all&&yum makecache &&yum install docker docker-compose git docker-compose-plugin -y
```

### APT

```shell
apt update && apt install docker docker-compose git docker-compose-plugin -y
```

> 请使用`root`用户执行以上命令

## 使用外部数据库

[文档: 我有自己的数据库](up/nosql.md)

> 镜像均已上传到`阿里云`,可直接拉取启动

## 使用全量

> 从阿里云镜像库直接拉取已打包好的所有镜像运行


[文档: 使用全新的数据库服务](up/sql.md)


## 使用本地构建所有镜像

[文档: 我想自己构建-此方法对机器配置要求略高](build.md)

> 基于阿里云基础镜像构建,无需配置镜像加速器


# 默认账号密码

```shell
admin
```

```shell
123456
```