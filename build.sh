#!/usr/bin/env bash
set -e
set -x
# 判断当前用户是否具有 sudo 权限
if [ $(id -u) -ne 0 ]; then
    echo "当前用户无权限执行此脚本，请使用 sudo 命令执行"
    exit 1
fi
# 判断 program/admin
if [ ! -d "program/admin" ]; then
    echo "找不到 program/admin 目录"
    exit 1
fi
pushd program/admin

docker buildx build --load -t registry.cn-hangzhou.aliyuncs.com/thrive/admin:latest .
# 使用普通构建,不使用 buildx
#docker build -t registry.cn-hangzhou.aliyuncs.com/thrive/admin:latest .
if [ $? -eq 0 ]; then
    docker push registry.cn-hangzhou.aliyuncs.com/thrive/admin:latest
fi
