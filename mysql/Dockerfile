# 使用基础 MySQL 镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/mysql:8.0

# 设置工作目录
WORKDIR /docker-entrypoint-initdb.d
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes

# 复制 .sql 文件到容器中
COPY data/ThriveX.sql /
# 启动数据库服务
RUN mysqld &
RUN mysql -u root -e "CREATE DATABASE ThriveX CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
RUN mysql ThriveX < /ThriveX.sql
RUN mysql -u root -e "GRANT ALL PRIVILEGES ON ThriveX.* TO 'root'@'%';"
# 执行导入的SQL 文件
CMD ["--default-authentication-plugin=mysql_native_password"]