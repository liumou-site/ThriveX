#!/usr/bin/env bash
set -e
if [ ! -d "program/admin" ]; then
    echo "找不到 program/admin 目录"
    exit 1
fi
# 预定义变量
mysqlPath="/data/ThriveX/mysql"
mysqlUser="ThriveX"
# 数据库密码
mysqlPassword="ThriveX@123?"
# 数据库主机
mysqlHost="127.0.0.1"
# 数据库端口
mysqlPort="3306"

# 功能变量
InstallSetSQL="1"
nginxPath="/data/ThriveX/nginx"


function SetMySQLPassword() {
    while true; do
        echo "请输入数据库密码"
        read -p "请输入：" mysqlPassword
        if [ -z "$mysqlPassword" ]; then
            echo "密码不能为空"
            continue
        fi
        echo "确认密码"
        read -p "请输入：" confirmPassword
        if [ "$mysqlPassword" != "$confirmPassword" ]; then
            echo "两次密码不一致"
            continue
        fi
        echo "密码设置成功"
        break
    done
}
function SetNginx() {
	echo "请输入Nginx端口映射端口,默认: 9007"
	read -p "请输入：" nginxPort
	if [ -z "$nginxPort" ]; then
		echo -e "使用默认端口: 9007"
		nginxPort="9007"
	fi
}

function SetInstallInfo() {
    echo "开始设置安装信息"
    if [[ $InstallSetSQL -eq "1" ]];then
        echo "[全新安装]请输入数据库映射路径(用于映射到容器内),默认: /data/ThriveX/mysql"
        read -p "请输入：" mysqlPath
        if [ -z "$mysqlPath" ]; then
            echo -e "使用默认路径: /data/ThriveX/mysql"
            mysqlPath="/data/ThriveX/mysql"
        fi
    fi
    echo "请输入数据库用户名,默认: ThriveX"
    read -p "请输入：" mysqlUser
    if [ -z "$mysqlUser" ]; then
        echo -e "使用默认用户名: ThriveX"
        mysqlUser="ThriveX"
    fi
    SetMySQLPassword
    echo "请输入数据库主机,默认: 10.178.178.10"
    read -p "请输入：" mysqlHost
    if [ -z "$mysqlHost" ]; then
        echo "使用默认主机"
        mysqlHost="10.178.178.10"
    fi
    echo "请输入数据库端口,默认: 3306"
    read -p "请输入：" mysqlPort
    if [ -z "$mysqlPort" ]; then
        echo "使用默认端口"
        mysqlPort="3306"
    fi
}
function Show() {
  echo "----------------信息确认----------------"
  if [[ $InstallSetSQL -eq "1" ]];then
    echo "数据库映射路径: $mysqlPath"
  fi
  echo "数据库用户名: $mysqlUser"
  echo "数据库密码: $mysqlPassword"
  echo "数据库主机: $mysqlHost"
  echo "数据库端口: $mysqlPort"
  echo "--------------------------------------"
  echo "是否继续安装?(y/n)"
  read -p "请输入：" confirm
  if [ "$confirm" != "y" ]; then
    echo "取消安装"
    exit 1
  fi

}
function replaceConfig() {
	if [[ -f docker-compose.yaml ]];then
			# 替换端口
			sed -i "s/3306/$mysqlPort/g" docker-compose.yaml
			sed -i "s/ThriveX/$mysqlUser/g" docker-compose.yaml
			sed -i "s/ThriveX@123?/$mysqlPassword/g" docker-compose.yaml
			# 替换主机
			sed -i "s/10.178.178.10/$mysqlHost/g" docker-compose.yaml
			# 替换nginx
			sed -i "s/80:80/$nginxPort:80/g" docker-compose.yaml
	else
		echo "找不到docker-compose.yaml文件"
		exit 1
	fi
}

function InstallNoSQL() {
  SetInstallInfo
  Show
  if [[ -f "up/docker-compose-nosql.yaml" ]];then
		echo "开始安装NoSQL"
		cp -rf up/docker-compose-nosql.yaml docker-compose.yaml
		replaceConfig
		docker-compose up -d
		if [ $? -eq 0 ]; then
				echo "安装成功"
				echo -e "访问地址: http://127.0.0.1:{$nginxPort}"
				echo "数据库地址: $mysqlHost:$mysqlPort"
				echo "数据库用户名: $mysqlUser"
				echo "数据库密码: $mysqlPassword"
				echo "数据库映射路径: $mysqlPath"
				echo "数据库映射路径: $mysql"
		else
			echo "找不到NoSQL安装文件"
			exit 1
		fi
	fi

}

function InstallSQL() {
  SetInstallInfo
  Show
	if [[ -f "up/docker-compose-sql.yaml" ]];then
			echo "开始安装SQL"
			cp -rf up/docker-compose-sql.yaml docker-compose.yaml
			replaceConfig
			docker-compose up -d
			if [ $? -eq 0 ]; then
					echo "安装成功"
					echo -e "访问地址: http://127.0.0.1:{$nginxPort}"
					echo "数据库地址: $mysqlHost:$mysqlPort"
					echo "数据库用户名: $mysqlUser"
					echo "数据库密码: $mysqlPassword"
					echo "数据库映射路径: $mysqlPath"
					echo "数据库映射路径: $mysql"
			else
				echo "找不到NoSQL安装文件"
				exit 1
			fi
	fi
}
function main() {
		# 检查docker是否安装
		docker ps > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "请先安装并启动docker服务"
			exit 1
		fi
    # 选择安装方式
    echo "请选择安装方式"
    echo "1. 我需要全新安装数据库"
    echo "2. 我有自己的数据库并有对应连接信息"
    echo "3. 我需要自行构建镜像"
    read -p "请输入选项：" option
    if [ $option -eq 1 ]; then
      InstallSQL
    elif [ $option -eq 2 ]; then
			InstallSetSQL="0"
      InstallNoSQL
    elif [ $option -eq 3 ]; then
      echo "自行构建镜像"
    else
      echo "无效选项"
      exit 1
    fi
}
main