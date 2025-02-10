#!/usr/bin/bash
# 打印数据库配置
echo ${DB_INFO}
echo "Starting server..."
java -jar /server/server.jar --spring.datasource.url=${DB_INFO}