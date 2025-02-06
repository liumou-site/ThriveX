# 手动运行容器

## 创建网络
```shell
docker network create --driver bridge --subnet=10.178.178.0/24 --gateway=10.178.178.1 thrive_network
```

效果

```shell
root@tb3:~# docker network create --driver bridge --subnet=10.178.178.0/24 --gateway=10.178.178.1 thrive_network
0673efdec2fff07da51583e3db166a4d326fcafd53ffbbd0d3020e91275fae31
root@tb3:~# 
```

## 启动数据库

```shell
docker run -d --name=thrive_mysql --hostname=thrive_mysql --restart=always --network=thrive_network \
--ip=10.178.178.10 -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=ThriveX@123? \
-e MYSQL_DATABASE=ThriveX \
-e MYSQL_USER=thrive \
-e MYSQL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/mysql
```

效果

```shell
root@tb3:~# docker run -d --name=thrive_mysql --hostname=thrive_mysql --restart=always --network=thrive_network \
--ip=10.178.178.10 -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=ThriveX@123? \
-e MYSQL_DATABASE=ThriveX \
-e MYSQL_USER=thrive \
-e MYSQL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/mysql
3cb9a6e8e2e6e41c402209a011134e43b5bd5b6a1c21ad6d2364f8d2e5f7907b
root@tb3:~# 
```

## 启动 server 后端

```shell
docker run -d --name=thrive_server --hostname=thrive_server --restart=always --network=thrive_network --ip=10.178.178.14 \
-p 9003:9003 \
-e DB_INFO="thrive_mysql:3306/ThriveX" \
-e DB_USERNAME=thrive \
-e DB_PASSWORD=ThriveX@123? \
-e EMAIL_HOST=smtp.qq.com \
-e EMAIL_PORT=465 \
-e EMAIL_USERNAME=123456@qq.com \
-e EMAIL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/server
```

> 请将数据库信息改为自己的数据库信息

效果
```shell
root@tb3:~# docker run -d --name=thrive_server --hostname=thrive_server --restart=always --network=thrive_network --ip=10.178.178.14 \
-p 8080:8080 \
-e DB_PORT=3306 \
-e DB_HOST=172.178.178.10 \
-e DB_NAME=thrive \
-e DB_USERNAME=thrive \
-e DB_PASSWORD=ThriveX@123? \
-e DB_INFO="thrive_mysql:3306/ThriveX" \
-e EMAIL_HOST=smtp.qq.com \
-e EMAIL_PORT=465 \
-e EMAIL_USERNAME=123456@qq.com \
-e EMAIL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/server
7204cd08ef1248debaf0a16f01960cacbb91bb9cd2fb65359f196d18e9f15658
root@tb3:~# 
```


## 启动 admin 前端

```shell
docker run -tid --name=thrive_admin --hostname=thrive_admin --restart=always --network=thrive_network \
--ip=10.178.178.13 -p 9002:80 \
-e VITE_PROJECT_API=http://thrive_server:9003/api \
-e VITE_BAIDU_TONGJI_SITE_ID="ID" \
-e VITE_BAIDU_TONGJI_ACCESS_TOKEN="TOKEN" \
-e VITE_AI_APIPassword="AI" \
-e VITE_AI_MODEL=lite \
-e VITE_GAODE_WEB_API="API" \
registry.cn-hangzhou.aliyuncs.com/thrive/admin
``` 

### 变量值替换

`VITE_BAIDU_TONGJI_SITE_ID`: 百度统计站点ID
`VITE_BAIDU_TONGJI_ACCESS_TOKEN`: 百度统计AccessToken
`VITE_AI_APIPassword`: 智能AI密码
`VITE_AI_MODEL`: 智能AI模型
`VITE_GAODE_WEB_API`: 高德Web服务API


效果

```shell
root@tb3:~# docker run -tid --name=thrive_admin --hostname=thrive_admin --restart=always --network=thrive_network \
--ip=10.178.178.13 -p 9002:80 \
-e VITE_PROJECT_API=http://thrive_server:9003/api \
-e VITE_BAIDU_TONGJI_SITE_ID="ID" \
-e VITE_BAIDU_TONGJI_ACCESS_TOKEN="TOKEN" \
-e VITE_AI_APIPassword="AI" \
-e VITE_AI_MODEL=lite \
-e VITE_GAODE_WEB_API="API" \
registry.cn-hangzhou.aliyuncs.com/thrive/admin
9a0a050105108db80b3f618f223df772129d00d488f72b4a0cc9542e0c3d6089
root@tb3:~# 
```

## 启动 blog 前端

```shell
docker run -d --name=thrive_blog --hostname=thrive_blog --restart=always --network=thrive_network \
--ip=10.178.178.12 -p 9001:9001 \
-e NEXT_PUBLIC_CACHING_TIME=0 \
-e NEXT_PUBLIC_PROJECT_API="http://thrive_server:9003/api" \
-e NEXT_PUBLIC_GAODE_KEY_CODE="code" \
-e NEXT_PUBLIC_GAODE_SECURITYJS_CODE="code" registry.cn-hangzhou.aliyuncs.com/thrive/blog
```

### 变量值替换
`NEXT_PUBLIC_CACHING_TIME`: 博客缓存时间,单位秒,默认为0,表示不缓存,如果为-1,表示缓存一天,如果为-2,表示缓存一个月,如果为-3,表示缓存一年,如果为-4,表示缓存永久,如果为-5,表示缓存一年,如果为-6,表示缓存两年,如果为-7,表示缓存三年,如果为-8,表示缓存四年,如果为-9,表示缓存五年,如果为-10,表示缓存六年,如果为-11,表示缓存七年,如果为-12,表示缓存八年,如果
`NEXT_PUBLIC_PROJECT_API`: 项目API地址(建议默认)
`NEXT_PUBLIC_GAODE_KEY_CODE`: 高德Web服务API Key
`NEXT_PUBLIC_GAODE_SECURITYJS_CODE`: 高德Web服务API SecurityJS


效果

```shell
root@tb3:~# docker run -d --name=thrive_blog --hostname=thrive_blog --restart=always --network=thrive_network \
--ip=10.178.178.12 -p 9001:9001 \
-e NEXT_PUBLIC_CACHING_TIME=0 \
-e NEXT_PUBLIC_PROJECT_API="http://thrive_server:9003/api" \
-e NEXT_PUBLIC_GAODE_KEY_CODE="code" \
-e NEXT_PUBLIC_GAODE_SECURITYJS_CODE="code" registry.cn-hangzhou.aliyuncs.com/thrive/blog
d4f9c2bf920dbb4fb7c10b6981419a706912acb42955e2389667659ef700f456
root@tb3:~# 
```