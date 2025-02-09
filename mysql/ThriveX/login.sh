#!/usr/bin/bash
echo "Starting login.sh"
mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} -e "show databases;"
# 判断是否登录成功
if [ $? -eq 0 ]; then
  echo "登录成功"
else
	echo "登录失败,..."
fi
mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} -e "use ${MYSQL_DATABASE};show tables;"
mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD}