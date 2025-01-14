# 设置基础镜像
FROM openjdk:11.0-jre-buster

# 设置工作目录
WORKDIR /thrive

# 设置环境变量
ENV PORT=9003
ENV DB_INFO=数据库信息（mysql:3306/ThriveX）
ENV DB_USERNAME=数据库用户名（root）
ENV DB_PASSWORD=数据库密码（yyds）
ENV EMAIL_HOST=邮箱服务器（smtp.qq.com）
ENV EMAIL_PORT=邮箱端口（465）
ENV EMAIL_USERNAME=邮箱账号（33311118881@qq.com）
ENV EMAIL_PASSWORD=邮箱授权码（xxxxxxxxxxxxx）

# 将jar包复制到工作目录中并拷贝给app.jar
COPY blog.jar /thrive/app.jar

# 创建容器成功做的事情,等价于：java -jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]