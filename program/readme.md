# 手动运行容器

## 创建网络
```shell
docker network create --driver bridge --subnet=10.178.178.0/24 --gateway=10.178.178.1 thrive_network
```

## 启动数据库
```shell
docker run -d --name=thrive_mysql --restart=always --network=thrive_network --ip=10.178.178.10 -p 3306:3306 \\
-e MYSQL_ROOT_PASSWORD=ThriveX@123? \\
-e MYSQL_DATABASE=thrive \\
-e MYSQL_USER=thrive \\
-e MYSQL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/mysql
```

## 启动 server 后端

```shell
docker run -d --name=thrive_server --restart=always --network=thrive_network --ip=10.178.178.14 \\
-p 8080:8080 \\
-e DB_PORT=3306 \\
-e DB_HOST=172.178.178.10 \\
-e DB_NAME=thrive \\
-e DB_USERNAME=thrive \\
-e DB_PASSWORD=ThriveX@123? \\
-e DB_INFO="172.178.178.10:3306/thrive" \\
-e EMAIL_HOST=smtp.qq.com \\
-e EMAIL_PORT=465 \\
-e EMAIL_USERNAME=123456@qq.com \\
-e EMAIL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/server
```

> 请将数据库信息改为自己的数据库信息



## 启动 admin 前端
```shell
docker run -d --name=thrive_admin --restart=always --network=thrive_network --ip=10.178.178.13 -p 81:81 -e VUE_APP_BASE_API=http://thrive_backend:8080/api/v1/admin/ -e VUE_APP_TITLE=ThriveX -e VUE_APP_SITE_NAME=ThriveX -e VUE_APP_SITE_DESCRIPTION=ThriveX -e VUE_APP_SITE_KEYWORDS=ThriveX -eVUE_APP_SITE_AUTHOR=ThriveX -e VUE_APP_SITE_ICON=https://thrivex.oss-cn-beijing.aliyuncs.com/thrivex/thrivex -e VUE_APP_SITE_LOGO=https://thrivex.oss-cn-beijing.aliyuncs.com/thrivex/thrivex registry.cn-hangzhou.aliyuncs.com/thrive/admin
``` 



## 启动 web 前端
```shell
docker run -d --name=thrive_blog --restart=always --network=thrive_network --ip=10.178.178.12 -p 80:80 -e VUE_APP_BASE_API=http://thrive_backend:8080/api/v1/vue/ -e VUE_APP_TITLE=ThriveX -e VUE_APP_SITE_NAME=ThriveX -e VUE_APP_SITE_DESCRIPTION=ThriveX -e VUE_APP_SITE_KEYWORDS=ThriveX -e VUE_APP_SITE_AUTHOR=ThriveX -e VUE_APP_SITE_ICON=https://thrivex.oss-cn-beijing.aliyuncs.com/thrivex/thrivex   -e VUE_APP_SITE_LOGO=https://thrivex.oss-cn-beijing.aliyuncs.com/thrivex/thrivex registry.cn-hangzhou.aliyuncs.com/thrive/blog
```