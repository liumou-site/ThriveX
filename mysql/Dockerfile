# 使用基础 MySQL 镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/mysql:8.0

# 设置工作目录
WORKDIR /docker-entrypoint-initdb.d

# 设置环境变量
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes

# 复制 SQL 文件到容器中
COPY data/ThriveX.sql /
COPY init.sh /init.sh
RUN chmod +x /init.sh

# 创建一个初始化脚本
RUN echo "CREATE DATABASE IF NOT EXISTS ThriveX CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;" > /docker-entrypoint-initdb.d/init.sql
RUN echo "GRANT ALL PRIVILEGES ON ThriveX.* TO 'root'@'%';" >> /docker-entrypoint-initdb.d/init.sql

# 启动 MySQL 服务
CMD ["/init.sh"]