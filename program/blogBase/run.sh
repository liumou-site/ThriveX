#!/usr/bin/env bash
set -e
NEXT_PUBLIC_PROJECT_API="https://api.thrivex.cn"
NEXT_PUBLIC_CACHING_TIME=0
NEXT_PUBLIC_GAODE_KEY_CODE="c1"
NEXT_PUBLIC_GAODE_SECURITYJS_CODE="c2"

images="registry.cn-hangzhou.aliyuncs.com/thrive/blog:latest"


function SetEnv() {
  while true; do
    echo "请输入项目api地址"
    read -p "请输入：" NEXT_PUBLIC_PROJECT_API
    if [ -z "$NEXT_PUBLIC_PROJECT_API" ]; then
      echo "项目api地址不能为空"
      continue
    fi
    echo "确认项目api地址"
    read -p "请输入：" confirmNEXT_PUBLIC_PROJECT_API
    if [ "$NEXT_PUBLIC_PROJECT_API" != "$confirmNEXT_PUBLIC_PROJECT_API" ]; then
      echo "两次项目api地址不一致"
      continue
    fi
  done
}
function CheckInfo() {
    if [[ -z "$NEXT_PUBLIC_PROJECT_API" ]]; then
      echo "项目api地址不能为空"
      exit 1
    fi
    if [[ -z "$NEXT_PUBLIC_CACHING_TIME" ]]; then
      echo "缓存时间不能为空"
      exit 1
    fi
    if [[ -z "$NEXT_PUBLIC_GAODE_KEY_CODE" ]]; then
      echo "高德key不能为空"
      exit 1
    fi
}
function ReadEnv() {
    echo "从.env文件获取"
    if [[ ! -f "blog.env" ]]; then
      echo "未找到blog.env文件,已创建 blog.env文件,请填写配置信息后重新运行"
      echo "NEXT_PUBLIC_PROJECT_API=https://api.thrivex.cn" > blog.env
      echo "NEXT_PUBLIC_CACHING_TIME=0" >> blog.env
      echo "NEXT_PUBLIC_GAODE_KEY_CODE=c1" >> blog.env
      echo "NEXT_PUBLIC_GAODE_SECURITYJS_CODE=c2" >> blog.env
      exit 2
    fi
    source blog.env
}
function RunContainer() {
    if command -v docker >/dev/null 2>&1; then
        echo "开始运行"
    else
        echo "请安装docker"
        exit 1
    fi
    cmd="docker run -d --name thrive-blog -p 3000:3000 -e NEXT_PUBLIC_PROJECT_API=$NEXT_PUBLIC_PROJECT_API -e NEXT_PUBLIC_CACHING_TIME=$NEXT_PUBLIC_CACHING_TIME -e NEXT_PUBLIC_GAODE_KEY_CODE=$NEXT_PUBLIC_GAODE_KEY_CODE -e NEXT_PUBLIC_GAODE_SECURITYJS_CODE=$NEXT_PUBLIC_GAODE_SECURITYJS_CODE"
    cmd="$cmd --network thrive_network --ip=10.178.178.12 $images"
    if docker ps | grep -q "thrive-blog"; then
        echo "容器已存在,请先删除容器"
        exit 1
    fi
    eval "$cmd"
    if [ $? -eq 0 ]; then
        echo "容器启动成功,请持续观察容器状态"
        echo "访问地址: http://127.0.0.1:3000"
    else
        echo "容器启动失败"
        docker logs thrive-blog
        exit 1
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
  echo "请选择安装信息获取方法"
  echo "1. 从环境变量获取"
  echo "2. 从.env文件获取"
  echo "3. 手动输入"
  read -p "请输入选项：" option
  if [ $option -eq 1 ]; then
    echo "从环境变量获取"
    CheckInfo
  elif [ $option -eq 2 ]; then
    ReadEnv
  elif [ $option -eq 3 ]; then
    echo "手动输入"
    SetEnv
  else
    echo "无效选项"
    exit 1
  fi
  CheckInfo
  RunContainer
}