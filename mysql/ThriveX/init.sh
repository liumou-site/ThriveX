#!/usr/bin/bash
set -e
echo "Starting init.sh"
sql="/ThriveX/ThriveX.sql"
if [[ -f ${sql} ]];then
	echo "开始导入数据库--init.sh"
  # 判断是否能否使用root登录
  mysql -u root -p$MYSQL_ROOT_PASSWORD -e "SELECT 1;"
  if [ $? -eq 0 ]; then
  		echo "使用root登录成功"
      mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
      if [[ -n "$MYSQL_USER" && -n "$MYSQL_PASSWORD" ]]; then
      		echo "创建用户"
      	  # 判断数据库是否存在
      	  mysql -u root -p$MYSQL_ROOT_PASSWORD -e "show databases;" | grep -q "$MYSQL_DATABASE"
      	  if [ $? -ne 0 ]; then
							echo "数据库不存在，创建数据库"
							mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
					fi
      		# 判断用户是否存在
      		mysql -u root -p$MYSQL_ROOT_PASSWORD -e "SELECT 1 FROM mysql.user WHERE user = '$MYSQL_USER' AND host = '%';" > /dev/null 2>&1
      		if [ $? -eq 0 ]; then
      				echo "用户已存在"
      		else
      				echo "用户不存在，创建用户"
      				mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE USER '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
							mysql -u root -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$MYSQL_USER'@'%';"
      		fi
					f="/ThriveX/import.sh"
					if [[ -f ${f} ]];then
							echo "开始导入数据库"
							${f}
					fi
      else
      	 	echo "未设置MYSQL_USER和MYSQL_PASSWORD,将直接使用root登录"
         	mysql -u root -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO 'root'@'%';"
      fi
      echo "刷新权限"
      mysql -u root -p$MYSQL_ROOT_PASSWORD -e "FLUSH PRIVILEGES;"

  else
      echo "无法使用root登录,请检查MYSQL_ROOT_PASSWORD"
  fi
else
  echo -e "未找到[ ${sql} ]文件,无需初始化数据库"
fi
echo "数据库初始化完成"