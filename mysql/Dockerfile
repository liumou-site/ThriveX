# 使用基础 MySQL 镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/mysql:8.0
ENV VERSION 1.0
# 设置工作目录
WORKDIR /docker-entrypoint-initdb.d
ADD https://github.com/LiuYuYang01/ThriveX-Server/blob/master/ThriveX.sql /docker-entrypoint-initdb.d/ThriveX.sql
RUN chmod +x /docker-entrypoint-initdb.d/ThriveX.sql
RUN rm -f /ThriveX.sql
# 启动 MySQL 服务
#CMD ["/init.sh"]