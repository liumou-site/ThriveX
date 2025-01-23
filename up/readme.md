# 独立数据库搭建教程


## 拉取代码
```shell
git clone https://github.com/LiuYuYang01/ThriveX.git
```

## 进入项目
```shell
cd ThriveX/up
```
## 配置环境变量

编辑文件`up/docker-compose.yaml`

```shell
vim docker-compose.yaml
```


### 后端(server)部分

`EMAIL_PASSWORD`: 设置邮箱密码

`EMAIL_USERNAME`: 设置邮箱用户名

`NEXT_PUBLIC_GAODE_KEY_CODE`: 高德地图key

`NEXT_PUBLIC_GAODE_SECURITYJS_CODE`: 高德地图秘钥

`DB_PASSWORD`: 设置数据库密码

`DB_USERNAME`: 设置数据库用户名

`DB_HOST`: 设置数据库主机地址

#### 建议默认

`DB_PORT`: 设置数据库端口

`DB_NAME`: 设置数据库名



### 管理后台(admin)部分

`VITE_BAIDU_TONGJI_SITE_ID`: 百度统计站点ID

`VITE_BAIDU_TONGJI_ACCESS_TOKEN`: 百度统计秘钥

`VITE_AI_APIPassword`: AI大模型秘钥

`VITE_GAODE_WEB_API`: 高德地图坐标秘钥


# 启动

```shell
docker-compose up -d
```