# 使用基础 MySQL 镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/mysql:8.0

# 设置工作目录
WORKDIR /docker-entrypoint-initdb.d

# 复制 .sql 文件到容器中
COPY data/ThriveX.sql /docker-entrypoint-initdb.d/
#
## 设置字符集和排序规则
#CMD ["--character-set-server=utf8mb4", "--collation-server=utf8mb4_unicode_ci"]
