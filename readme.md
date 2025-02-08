# ThriveX

部署之前,需要获取相关平台API信息,请参考[API获取](https://docs.liuyuyang.net/docs/%E9%A1%B9%E7%9B%AE%E9%83%A8%E7%BD%B2/API/%E9%AB%98%E5%BE%B7%E5%9C%B0%E5%9B%BE.html)


# 依赖安装

> 在进行部署前,请确保服务器已安装`git`

# 获取安装文件

```shell
git clone https://gitee.com/liumou_site/ThriveX
```

效果

```shell
root@Debian12:/data# git clone https://gitee.com/liumou_site/ThriveX
Cloning into 'ThriveX'...
remote: Enumerating objects: 474, done.
remote: Counting objects: 100% (474/474), done.
remote: Compressing objects: 100% (253/253), done.
remote: Total 474 (delta 241), reused 432 (delta 199), pack-reused 0
Receiving objects: 100% (474/474), 66.25 MiB | 5.24 MiB/s, done.
Resolving deltas: 100% (241/241), done.
root@Debian12:/data# 
```

# 部署教程-一键

[脚本: 一键部署](doc/py.md)


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

# 异常处理

## 安装requests

```shell
pip3 install requests==2.31.0
```