#!/usr/bin/env bash
set -e
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
#
pac="apt"
# 设置URL
url_compose_root="https://github.com/liumou-site/ThriveX/blob/main"
if [[ $1 == "gitee" ]];then
    url_compose_root="https://gitee.com/liumou_site/ThriveX/raw/main"
fi
compose_filename="docker-compose.yaml"
function downloadComposeFile() {
    wget -O docker-compose.yaml "${url_compose_root}/up/${compose_filename}"
    if [ $? -ne 0 ]; then
        echo "下载失败,请手动下载"
        echo "${url_compose_root}/up/${compose_filename}"
        exit 1
    fi
}

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
  while true; do
      echo "请输入Nginx端口映射端口,默认: 9007"
      read -p "请输入：" nginxPort
      if [ -z "$nginxPort" ]; then
        echo -e "使用默认端口: 9007"
        nginxPort="9007"
      fi
        # 检查本地是否已占用端口
      if [[ -n "$nginxPort" ]];then
        lsof -i:$nginxPort > /dev/null 2>&1
        if [ $? -eq 0 ]; then
          echo "端口 $nginxPort 已被占用,请修改端口"
          exit 1
        else
          echo "端口 $nginxPort 可用"
          break
        fi
      fi
  done
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
		echo "请输入数据库映射端口,默认: 3306"
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
			if [[ -z $mysqlPort || -z $mysqlUser || -z $mysqlPassword || $mysqlHost ]];then
        echo "数据库信息不能为空"
        exit 1
      fi
			sed -i "s/3306/$mysqlPort/g" docker-compose.yaml
			sed -i "s/ThriveX/$mysqlUser/g" docker-compose.yaml
			sed -i "s/ThriveX@123?/$mysqlPassword/g" docker-compose.yaml
			# 替换主机
			sed -i "s/10.178.178.10/$mysqlHost/g" docker-compose.yaml
			# 替换nginx
			if [[ -z "$nginxPort" ]];then
        SetNginx
      fi
			sed -i "s/80:80/$nginxPort:80/g" docker-compose.yaml
	else
		echo "找不到docker-compose.yaml文件"
		exit 1
	fi
}

function InstallNoSQL() {
	SetInstallInfo
	Show
	compose_filename="docker-compose-nosql.yaml"
	downloadComposeFile
  echo "开始安装NoSQL"
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
}

function InstallSQL() {
    SetInstallInfo
    Show
    compose_filename="docker-compose-sql.yaml"
    downloadComposeFile
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
}
function getInstallCmd() {
  if command -v apt-get &> /dev/null; then
    echo "apt-get"
  elif command -v yum &> /dev/null; then
    echo "yum"
    pac="yum"
  else
    echo "无法确定包管理工具,目前仅支持 apt-get 或 yum"
    exit 1
  fi
}
function checkInstallInfo() {
    # 检查docker是否安装
		docker ps > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "请先安装并启动docker服务"
			exit 1
		fi
    # 检查wget 是否安装
    if ! command -v wget &> /dev/null; then
        getInstallCmd
        echo "wget 未安装，正在安装..."
#        sudo ${pac} update
        sudo ${pac} install -y wget
        if [ $? -ne 0 ]; then
            echo "wget 安装失败，请手动安装"
            exit 1
        fi
    fi
    # 检查docker-compose 是否安装
    if ! command -v docker-compose &> /dev/null; then
        getInstallCmd
        echo "docker-compose 未安装，正在安装..."
#        sudo ${pac} update
        sudo ${pac} install -y docker-compose
        if [ $? -ne 0 ]; then
            echo "docker-compose 安装失败，请手动安装"
            exit 1
        fi
    fi
    # 检查docker-compose-plugin 是否安装
    if [[ ${pac} == "apt" ]];then
      dpkg -l | grep -v grep |grep docker-compose-plugin
      if [[ $? -eq 0 ]]; then
          echo "docker-compose-plugin 已安装"
          break
      fi
    else
      rpm -qa | grep -v grep | grep docker-compose-plugin
      if [[ $? -eq 0 ]]; then
          echo "docker-compose-plugin 已安装"
          break
      fi
    fi

    echo "docker-compose-plugin 未安装，正在安装..."
    sudo ${pac} install -y docker-compose-plugin
    if [ $? -ne 0 ]; then
        echo "docker-compose-plugin 安装失败，请手动安装"
        exit 1
    fi
}
function main() {
    checkInstallInfo
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