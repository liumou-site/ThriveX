# ThriveX

# 一键部署教程

## 拉取代码
```shell
git clone https://github.com/LiuYuYang01/ThriveX.git
```

## 进入项目
```shell
cd ThriveX
```
## 配置环境变量
编辑文件`compose.yaml`

```shell
vim compose.yaml
```
```yaml
services:
  # 数据库
  mysql:
    container_name: mysql
    image: mysql:8.0
    hostname: mysql-thrive
    ports:
      - "3307:3306"
    networks:
      thrive_network:
        ipv4_address: 172.17.178.10
    environment:
      ## 设置数据库ROOT密码,强烈建议修改(首次启动有效)
      MYSQL_ROOT_PASSWORD: ThriveX@123?
      ## 设置数据库名,强烈建议修改(首次启动有效)
      MYSQL_DATABASE: thrive
      ## 设置数据库用户名,强烈建议修改(首次启动有效)
      MYSQL_USER: thrive
      ## 设置数据库密码,强烈建议修改(首次启动有效)
      MYSQL_PASSWORD: ThriveX@123?
    volumes:
      - ./mysql/mysql_data:/var/lib/mysql
      - ./mysql/data:/docker-entrypoint-initdb.d
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

  # 备份服务
  backup:
    image: mysql:8.0
    container_name: mysql_backup
    hostname: mysql_backup-thrive
    command: /bin/sh -c "while true; do mysqldump -h mysql -u root -pliuyuyang thrive > /backup/thrive_$(date +%F_%T).sql; sleep 10800; done"
    volumes:
      - ./mysql/backup:/backup
    networks:
      thrive_network:
        ipv4_address: 172.17.178.11
    environment:
      ## 设置数据库ROOT密码,强烈建议修改(首次启动有效)-必须和前面的数据库密码一致
      MYSQL_ROOT_PASSWORD: ThriveX@123?
      ## 设置数据库名,强烈建议修改(首次启动有效)-必须和前面的数据库密码一致
      MYSQL_DATABASE: thrive
      ## 设置数据库用户名,强烈建议修改(首次启动有效)-必须和前面的数据库密码一致
      MYSQL_USER: thrive
      ## 设置数据库密码,强烈建议修改(首次启动有效)-必须和前面的数据库密码一致
      MYSQL_PASSWORD: ThriveX@123?
    depends_on:
      - mysql

  # 前端项目
  blog:
    container_name: blog
    build: ./program/blog
    hostname: blog-thrive
    ports:
      - "9001:9001"
    networks:
      thrive_network:
        ipv4_address: 172.17.178.12
    environment:
      # 设置后端接口地址,http://你的后端域名/api
      NEXT_PUBLIC_PROJECT_API: http://server-thrive:9003/api
      # 高德地图key
      NEXT_PUBLIC_GAODE_KEY_CODE: ""
      # 高德地图秘钥
      NEXT_PUBLIC_GAODE_SECURITYJS_CODE: ""
    depends_on:
      - mysql
      - server

  # 控制端项目
  admin:
    container_name: admin
    build: ./program/admin
    hostname: admin-thrive
    ports:
      - "9002:80"
    networks:
      thrive_network:
        ipv4_address: 172.17.178.13
    environment:
      # 设置后端接口地址,http://你的后端域名/api
      VITE_PROJECT_API: http://server-thrive:9003/api
      # 百度统计站点ID
      VITE_BAIDU_TONGJI_SITE_ID: ""
      # 百度统计秘钥
      VITE_BAIDU_TONGJI_ACCESS_TOKEN: ""
      ## AI大模型秘钥
      VITE_AI_APIPassword: ""
      ## 高德地图坐标秘钥
      VITE_GAODE_WEB_API: ""
    depends_on:
      - mysql
      - server

  # 后端项目
  server:
    container_name: server
    build: ./program/server
    hostname: server-thrive
    ports:
      - "9003:9003"
    networks:
      thrive_network:
        ipv4_address: 172.17.178.14
    environment:
      ## 设置数据库主机地址
      DB_HOST: mysql-thrive
      ## 设置数据库名,强烈建议修改(首次启动有效)-必须和前面的数据库名一致
      DB_NAME: thrive
      ## 设置数据库用户名,强烈建议修改(首次启动有效)-必须和前面的数据库用户名一致
      DB_USERNAME: thrive
      ## 设置数据库密码,强烈建议修改(首次启动有效)-必须和前面的数据库用户名一致
      DB_PASSWORD: ThriveX@123?
      ## 设置数据库端口
      DB_PORT: 3306
      ## 设置邮箱配置
      EMAIL_HOST: smtp.qq.com
      ## 设置邮箱端口
      EMAIL_PORT: 465
      ## 设置邮箱用户名
      EMAIL_USERNAME: 123456789@qq.com
      ## 设置邮箱密码
      EMAIL_PASSWORD: 123456789
    depends_on:
      - mysql

  # 服务器
  nginx:
    image: nginx:latest
    container_name: nginx
    hostname: nginx-thrive
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    networks:
      thrive_network:
        ipv4_address: 172.17.178.15
    depends_on:
      - server

# 网络配置
networks:
  thrive_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.17.178.0/24
```

> 根据备注信息完成编辑即可开始构建

## 建议修改的变量

### 数据库容器部分

`MYSQL_PASSWORD`: 设置数据库密码

`MYSQL_USER` : 设置数据库用户名

`MYSQL_ROOT_PASSWORD`: 设置数据库ROOT密码

`DB_PASSWORD`: 设置数据库密码(必须和`MYSQL_PASSWORD`一致)

`DB_USERNAME`: 设置数据库用户名(必须和`MYSQL_USER`一致)

### 后端(server)部分

`EMAIL_PASSWORD`: 设置邮箱密码

`EMAIL_USERNAME`: 设置邮箱用户名

`NEXT_PUBLIC_GAODE_KEY_CODE`: 高德地图key

`NEXT_PUBLIC_GAODE_SECURITYJS_CODE`: 高德地图秘钥

### 管理后台(admin)部分

`VITE_BAIDU_TONGJI_SITE_ID`: 百度统计站点ID
`VITE_BAIDU_TONGJI_ACCESS_TOKEN`: 百度统计秘钥
`VITE_AI_APIPassword`: AI大模型秘钥
`VITE_GAODE_WEB_API`: 高德地图坐标秘钥



其他建议保持默认即可

## 执行命令
```shell
docker compose -p thrive up -d --build
```