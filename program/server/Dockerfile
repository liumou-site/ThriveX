# 设置基础镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/openjdk:11.0-jre-buster
# 设置环境变量，存储构建时间（北京时间）
ENV BUILD_TIME=2025-2-5-17:55:06

# 使用 LABEL 指令将构建时间设置为镜像的标签
LABEL build_time="${BUILD_TIME}"
LABEL VERSION=2.4.4
# 设置工作目录
WORKDIR /thrive

# 设置环境变量
ENV PORT=9003
## 设置数据库名
ENV DB_NAME=ThriveX
## 拼接数据库连接信息
ENV DB_INFO=thrive_mysql:3306/ThriveX
## 数据库用户名,请改为你自己的数据库用户名
ENV DB_USERNAME=thrive
## 数据库密码,请改为你自己的密码
ENV DB_PASSWORD=ThriveX@123?
## 邮箱服务器,请改成实际的邮箱服务器
ENV EMAIL_HOST=smtp.qq.com
## 邮箱端口,请改成实际的邮箱端口
ENV EMAIL_PORT=465
## 邮箱账号,请改成实际的邮箱账号
ENV EMAIL_USERNAME=33311118881@qq.com
## 邮箱授权码（xxxxxxxxxxxxx）
ENV EMAIL_PASSWORD=xxxxxxxxxxxxx
RUN sed -i "s@http.*\(com\|org\|cn\)@http://mirrors.cloud.tencent.com@g" /etc/apt/sources.list.d/debian.sources
# 将jar包复制到工作目录中并拷贝给app.jar
ADD https://github.com/LiuYuYang01/ThriveX-Server/releases/download/2.4.4/blog.jar /thrive/server.jar

# 创建容器成功做的事情,等价于：java -jar app.jar
ENTRYPOINT ["java", "-jar", "server.jar"]