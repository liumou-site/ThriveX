# 使用基础 MySQL 镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/mysql:8.0
# 设置环境变量，存储构建时间（北京时间）
ENV BUILD_TIME=2025-2-6_17:51:30

# 使用 LABEL 指令将构建时间设置为镜像的标签
LABEL build_time="${BUILD_TIME}"
# 设置工作目录
WORKDIR /docker-entrypoint-initdb.d
ADD https://github.com/LiuYuYang01/ThriveX-Server/raw/refs/heads/master/ThriveX.sql /ThriveX.sql
COPY init.sh /init.sh
RUN chmod +x /ThriveX.sql && chmod +x /init.sh
# 启动 MySQL 服务
CMD ["/init.sh"]