# 获取/更新镜像

## 开发版
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/thrive/mysql:dev
```

## 稳定版
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/thrive/mysql
```



# 运行容器

```shell
image=registry.cn-hangzhou.aliyuncs.com/thrive/mysql:dev # 如果需要使用开发版本,请执行这行
```

```shell
image=registry.cn-hangzhou.aliyuncs.com/thrive/mysql # 如果需要使用稳定版本,请执行这行
```

设置数据映射

```shell
src="/data/mysql" # 必须执行这行,可以修改映射路径
MYSQL_ROOT_PASSWORD=ThriveX@123? # 必须执行这行,可以修改数据库ROOT密码
MYSQL_DATABASE=ThriveX # 必须执行这行,可以修改数据库名
MYSQL_PASSWORD=ThriveX@123? # 必须执行这行,可以修改数据库密码
MYSQL_USER=thrive # 必须执行这行,可以修改数据库用户名
```

> 必须先执行上面的代码块,然后再执行下面的代码块

```shell
docker run -tid --name thrive_mysql -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \\
-e MYSQL_DATABASE=${MYSQL_DATABASE} \\
-e MYSQL_PASSWORD=${MYSQL_PASSWORD} \\
-e MYSQL_USER=${MYSQL_USER} \\
-v ${src}:/var/lib/mysql ${image}
```

