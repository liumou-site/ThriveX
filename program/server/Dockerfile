# 设置基础镜像
FROM openjdk:11.0-jre-buster

# 设置工作目录
WORKDIR /thrive

# 设置环境变量
ENV PORT=9003
## 设置数据库端口
ENV DB_PORT=3306
## 设置数据库主机
ENV DB_HOST=172.17.178.10
## 设置数据库名
ENV DB_NAME=ThriveX
## 拼接数据库连接信息
ENV DB_INFO=${DB_HOST}:${DB_PORT}/${DB_NAME}
## 数据库用户名,请改为你自己的数据库用户名
ENV DB_USERNAME=ThriveX
## 数据库密码,请改为你自己的密码
ENV DB_PASSWORD=ThriveX@123
## 邮箱服务器,请改成实际的邮箱服务器
ENV EMAIL_HOST=smtp.qq.com
## 邮箱端口,请改成实际的邮箱端口
ENV EMAIL_PORT=465
## 邮箱账号,请改成实际的邮箱账号
ENV EMAIL_USERNAME=33311118881@qq.com
## 邮箱授权码（xxxxxxxxxxxxx）
ENV EMAIL_PASSWORD=xxxxxxxxxxxxx

# 将jar包复制到工作目录中并拷贝给app.jar
COPY blog.jar /thrive/app.jar

# 创建容器成功做的事情,等价于：java -jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]