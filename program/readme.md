# 手动运行容器


手动运行之前,需要获取相关平台API信息,请参考[API获取](https://docs.liuyuyang.net/docs/%E9%A1%B9%E7%9B%AE%E9%83%A8%E7%BD%B2/API/%E9%AB%98%E5%BE%B7%E5%9C%B0%E5%9B%BE.html)

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
docker run -d --name=thrive_mysql --hostname=thrive_mysql -v /data/ThriveX/mysql:/var/lib/mysql --restart=always --network=thrive_network \
--ip=10.178.178.10 -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=ThriveX@123? \
-e MYSQL_DATABASE=ThriveX \
-e MYSQL_USER=thrive \
-e MYSQL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/mysql
```

效果

```shell
root@tb3:~# docker run -d --name=thrive_mysql --hostname=thrive_mysql -v /data/ThriveX/mysql:/var/lib/mysql --restart=always --network=thrive_network --ip=10.178.178.10 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=ThriveX@123? -e MYSQL_DATABASE=ThriveX -e MYSQL_USER=thrive -e MYSQL_PASSWORD=ThriveX@123? registry.cn-hangzhou.aliyuncs.com/thrive/mysql
5af0a89e3858fa303ee4b0527d7f49f45f605b7ce842f9e2d0d8c9fe3a8d7b87
root@tb3:~# 
```

## 启动 server 后端

```shell
docker run -d --name=thrive_server --hostname=thrive_server --restart=always --network=thrive_network --ip=10.178.178.14 \
-p 9003:9003 registry.cn-hangzhou.aliyuncs.com/thrive/server
```

默认变量值:

* `DB_INFO=thrive_mysql:3306/ThriveX`: 如果不清楚用途,建议默认，除非使用外部数据库
* `DB_USERNAME=thrive`: 建议默认
* `DB_PASSWORD`: 必须使用自己的数据库密码
* `EMAIL_HOST=smtp.qq.com` : 建议默认
* `EMAIL_PASSWORD=xxxxxxxxxxxxx` : 必须使用自己的邮箱和密码
* `EMAIL_USERNAME=123456@qq.com` : 必须使用自己的邮箱和密码
* `EMAIL_PORT=465`: 建议默认

效果

```shell
root@tb3:~# docker run -d --name=thrive_server --hostname=thrive_server --restart=always --network=thrive_network --ip=10.178.178.14 \
-p 9003:9003 registry.cn-hangzhou.aliyuncs.com/thrive/server
3661bdcc5721ed925753cd72f392d9dccbc1ec2a9e3399fb322a0e8733ed3b9c
root@tb3:~# 
```


## 启动 admin 前端

```shell
docker run -tid --name=thrive_admin --hostname=thrive_admin --restart=always --network=thrive_network \
--ip=10.178.178.13 -p 9002:80 \
-e VITE_BAIDU_TONGJI_SITE_ID="ID" \
-e VITE_BAIDU_TONGJI_ACCESS_TOKEN="TOKEN" \
-e VITE_AI_APIPassword="AI" \
-e VITE_GAODE_WEB_API="API" \
registry.cn-hangzhou.aliyuncs.com/thrive/admin
```
默认变量值: 

* `VITE_PROJECT_API=http://thrive_server:9003/api`

* `VITE_AI_MODEL=lite`


### 变量值替换(如需使用相关功能则必须设置)

* `VITE_BAIDU_TONGJI_SITE_ID`: 百度统计站点ID

* `VITE_BAIDU_TONGJI_ACCESS_TOKEN`: 百度统计AccessToken

* `VITE_AI_APIPassword`: 智能AI密码

* `VITE_AI_MODEL`: 智能AI模型

* `VITE_GAODE_WEB_API`: 高德Web服务API


效果

```shell
root@tb3:~# docker run -tid --name=thrive_admin --hostname=thrive_admin --restart=always --network=thrive_network \
--ip=10.178.178.13 -p 9002:80 \
-e VITE_BAIDU_TONGJI_SITE_ID="ID" \
-e VITE_BAIDU_TONGJI_ACCESS_TOKEN="TOKEN" \
-e VITE_AI_APIPassword="AI" \
-e VITE_GAODE_WEB_API="API" \
registry.cn-hangzhou.aliyuncs.com/thrive/admin
9ef7ba2c6b93a17b3ed54088ac0e5b03ea5744c04a11759ab6e4ae6ba024e5bb
root@tb3:~# 
```
变量默认值:

* `VITE_PROJECT_API=http://thrive_server:9003/api`
* `VITE_AI_MODEL=lite`

变量值替换:

* `VITE_BAIDU_TONGJI_SITE_ID=ID`
* `VITE_BAIDU_TONGJI_ACCESS_TOKEN=TOKEN`
* `VITE_AI_APIPassword=AI`
* `VITE_GAODE_WEB_API=API`

## 启动 blog 前端

```shell
docker run -d --name=thrive_blog --hostname=thrive_blog --restart=always --network=thrive_network \
--ip=10.178.178.12 -p 9001:9001 \
-e NEXT_PUBLIC_GAODE_KEY_CODE="code" \
-e NEXT_PUBLIC_GAODE_SECURITYJS_CODE="code" registry.cn-hangzhou.aliyuncs.com/thrive/blog
```

默认变量值:

* `NEXT_PUBLIC_CACHING_TIME=0`: 博客缓存时间,单位秒,默认为0,表示不缓存,如果为-1,表示缓存一天,如果为-2,表示缓存一个月,如果为-3,表示缓存一年,如果为-4,表示缓存永久
* `NEXT_PUBLIC_PROJECT_API="http://thrive_server:9003/api"`: 项目API地址(建议默认)


### 变量值替换

`NEXT_PUBLIC_GAODE_KEY_CODE`: 高德Web服务API Key

`NEXT_PUBLIC_GAODE_SECURITYJS_CODE`: 高德Web服务API SecurityJS


效果

```shell
root@tb3:~# docker run -d --name=thrive_blog --hostname=thrive_blog --restart=always --network=thrive_network \
--ip=10.178.178.12 -p 9001:9001 \
-e NEXT_PUBLIC_GAODE_KEY_CODE="code" \
-e NEXT_PUBLIC_GAODE_SECURITYJS_CODE="code" registry.cn-hangzhou.aliyuncs.com/thrive/blog
38ecc899ad39831f326a22af038123a35855477ee633ed0f0c7c42ca979fb247
root@tb3:~# 
```