#!/usr/bin/env bash
set -e
VITE_PROJECT_API="http://server.thrive.site:9003/api"
VITE_BAIDU_TONGJI_SITE_ID=0
VITE_BAIDU_TONGJI_ACCESS_TOKEN="c1"
VITE_AI_APIPassword="c2"
VITE_AI_MODEL="lite"
VITE_GAODE_WEB_API=""

images="registry.cn-hangzhou.aliyuncs.com/thrive/admin:latest"


function SetEnv() {
  while true; do
    echo "请输入项目api地址"
    read -p "请输入：" VITE_PROJECT_API
    if [ -z "$VITE_PROJECT_API" ]; then
      echo "项目api地址不能为空"
      continue
    fi
  done
}
function CheckInfo() {
    if [[ -z "$VITE_PROJECT_API" ]]; then
      echo "项目api地址不能为空: VITE_PROJECT_API"
      exit 1
    fi
    if [[ -z "$VITE_BAIDU_TONGJI_SITE_ID" ]]; then
      echo "百度统计站点id不能为空: VITE_BAIDU_TONGJI_SITE_ID"
      exit 1
    fi
    if [[ -z "${VITE_BAIDU_TONGJI_ACCESS_TOKEN}" ]]; then
      echo "百度统计token不能为空: VITE_BAIDU_TONGJI_ACCESS_TOKEN"
      exit 1
    fi
    if [[ -z "${VITE_AI_APIPassword}" ]]; then
      echo "AI密码不能为空: VITE_AI_APIPassword"
      exit 1
    fi
    if [[ -z "${VITE_AI_MODEL}" ]]; then
      echo "AI模型不能为空: VITE_AI_MODEL"
      exit 1
    fi
    if [[ -z "${VITE_GAODE_WEB_API}" ]]; then
      echo "高德web api不能为空: VITE_GAODE_WEB_API"
      exit 1
    fi
}
function ReadEnv() {
    echo "从.env文件获取"
    if [[ ! -f "admin.env" ]]; then
      echo "未找到admin.env文件,已创建 admin.env文件,请填写配置信息后重新运行"
      echo "VITE_PROJECT_API=http://server-thrive:9003/api" > admin.env
      echo "VITE_BAIDU_TONGJI_SITE_ID=0" >> admin.env
      echo "VITE_BAIDU_TONGJI_ACCESS_TOKEN=c1" >> admin.env
      echo "VITE_AI_APIPassword=c2" >> admin.env
      echo "VITE_AI_MODEL=lite" >> admin.env
      echo "VITE_GAODE_WEB_API=" >> admin.env
      exit 2
    fi
    source admin.env
}
function RunContainer() {
    if command -v docker >/dev/null 2>&1; then
        echo "开始运行"
    else
        echo "请安装docker"
        exit 1
    fi
    cmd="docker run -d --name thrive-admin -p 9002:80 -e VITE_PROJECT_API=$VITE_PROJECT_API -e VITE_BAIDU_TONGJI_SITE_ID=$VITE_BAIDU_TONGJI_SITE_ID -e VITE_BAIDU_TONGJI_ACCESS_TOKEN=$VITE_BAIDU_TONGJI_ACCESS_TOKEN"
    cmd="${cmd}  -e VITE_AI_APIPassword=$VITE_AI_APIPassword -e VITE_AI_MODEL=$VITE_AI_MODEL -e VITE_GAODE_WEB_API=$VITE_GAODE_WEB_API "
    cmd="${cmd}  --net=thrive_network --ip=10.178.178.13 ${images}"
    if docker ps | grep -q "thrive-admin"; then
        echo "容器已存在,请先删除容器"
        exit 1
    fi
    eval "$cmd"
    if [ $? -eq 0 ]; then
        echo "容器启动成功,请持续观察容器状态"
        echo "访问地址: http://127.0.0.1:9002"
    else
        echo "容器启动失败"
        docker logs thrive-admin
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