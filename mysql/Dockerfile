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
# 启动 MySQL 服务
CMD ["/init.sh"]