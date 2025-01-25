#!/usr/bin/env bash
docker build --load -t  nginx_test:latest .
if [ $? -ne 0 ]; then
    echo "构建失败"
    exit 1
fi
docker rm -f nginx_test
docker run -tid -P --name nginx_test nginx_test:latest
sleep 10
docker ps | grep nginx_test
if [ $? -ne 0 ]; then
    echo "运行失败"
    docker logs nginx_test
    docker rm -f nginx_test
    exit 1
fi
docker logs nginx_test
docker rm -f nginx_test
if [ $? -ne 0 ]; then
    echo "删除失败"
    exit 1
fi
echo "构建成功"