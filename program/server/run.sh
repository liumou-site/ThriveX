#!/usr/bin/env bash
# 用于单独运行服务
set -e
images="registry.cn-hangzhou.aliyuncs.com/thrive/server:latest"
# 设置环境变量
DB_HOST=""
DB_PORT=""
DB_USER=""
DB_PASSWORD=""
DB_NAME=""
function InputInfo() {
    CheckEnv
}
function CheckEnv() {
    if [[ -z "$DB_HOST" ]]; then
        echo "请输入数据库地址"
        read -p "请输入：" DB_HOST
    fi
    if [[ -z "$DB_PORT" ]]; then
        echo "请输入数据库端口"
        read -p "请输入：" DB_PORT
    fi
    if [[ -z "$DB_USER" ]]; then
        echo "请输入数据库用户名"
        read -p "请输入：" DB_USER
    fi
    if [[ -z "$DB_PASSWORD" ]]; then
        echo "请输入数据库密码"
        read -p "请输入：" DB_PASSWORD
    fi
    if [[ -z "$DB_NAME" ]]; then
        echo "请输入数据库名称"
        read -p "请输入：" DB_NAME
    fi
}
function CheckInfoQuit() {
    if [[ -z "$DB_HOST" || -z "$DB_PORT" || -z "$DB_USER" || -z "$DB_PASSWORD" || -z "$DB_NAME" ]]; then
        echo "请输入完整的配置信息"
        exit 1
    fi
}
function ReadEnv() {
    if [[ -f "thriveX.env" ]]; then
        source .env
    else
        echo "未找到thriveX.env文件,已创建 thriveX.env文件,请填写配置信息"
        echo "DB_HOST=127.0.0.1" > thriveX.env
        echo "DB_PORT=3306" >>thriveX.env
        echo "DB_USER=root" >>thriveX.env
        echo "DB_PASSWORD=root" >>thriveX.env
        echo "DB_NAME=thriveX" >>thriveX.env
        exit 1
    fi
}
function RunContainer() {
    if command -v docker >/dev/null 2>&1; then
        echo "开始运行"
    else
        echo "请安装docker"
        exit 1
    fi
    # 判断是否有容器存在
    if [[ $(docker ps -a | grep thrive-server) ]]; then
        echo "容器已存在,请删除后重试"
        exit 1
    fi
    cmd="docker run --name thrive-server -d -p 9007:9007 -e DB_HOST=$DB_HOST -e DB_PORT=$DB_PORT -e DB_USER=$DB_USER -e DB_PASSWORD=$DB_PASSWORD -e DB_NAME=$DB_NAME "
    cmd="${cmd} --net=thrive_network --ip=10.178.178.14 ${images}"
    echo "运行命令: $cmd"
    $cmd
    if [ $? -eq 0 ]; then
        echo "容器创建成功,请持续关注容器运行状态"
    else
        echo "运行失败"
    fi
}
function createDockerNetwork() {
    docker network ls | grep -q "thrive_network" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "创建thrive_network网络"
        docker network create thrive_network --subnet=10.178.178.0/24 --gateway=10.178.178.1 > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "网络创建成功"
        else
            echo "网络创建失败"
            echo "docker network create thrive_network --subnet=10.178.178.0/24 --gateway=10.178.178.1"
            exit 1
        fi
    fi
}
function main() {
    createDockerNetwork
    echo "请选择配置信息获取方式"
    echo "1. 从环境变量中获取"
    echo "2. 从thriveX.env文件中获取"
    echo "3. 手动输入"
    read -p "请输入选项：" option
    if [ $option -eq 1 ]; then
        CheckEnv
    elif [ $option -eq 2 ]; then
        ReadEnv
    elif [ $option -eq 3 ]; then
        InputInfo
    else
        echo "无效选项"
        exit 1
    fi
    CheckInfoQuit
    RunContainer
}