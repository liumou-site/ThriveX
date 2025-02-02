# 使用基础 MySQL 镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/mysql:8.0

# 设置工作目录
WORKDIR /docker-entrypoint-initdb.d

# 设置环境变量
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes

# 复制 SQL 文件到容器中
COPY data/ThriveX.sql /docker-entrypoint-initdb.d/

# 创建一个初始化脚本
RUN echo "CREATE DATABASE IF NOT EXISTS ThriveX CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;" > init.sql
RUN echo "GRANT ALL PRIVILEGES ON ThriveX.* TO 'root'@'%';" >> init.sql

# 将初始化脚本复制到 /docker-entrypoint-initdb.d 目录
COPY init.sql /docker-entrypoint-initdb.d/

# 启动 MySQL 服务
CMD ["--default-authentication-plugin=mysql_native_password"]