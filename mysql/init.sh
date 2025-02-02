#!/usr/bin/env bash
set -e
mysqld &
if [[ -f /ThriveX.sql ]];then
  echo "开始导入数据库"
  # 判断是否能否使用root登录
  mysql -u root -p$MYSQL_ROOT_PASSWORD -e "SELECT 1;" > /dev/null 2>&1
  if [ $? -eq 0 ]; then
      mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
      if [[ -n "$MYSQL_USER" && -n "$MYSQL_PASSWORD" ]]; then
          mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
          mysql -u root -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$MYSQL_USER'@'%';"
      else
         mysql -u root -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO 'root'@'%';"
      fi
      mysql -u root -p$MYSQL_ROOT_PASSWORD -e "FLUSH PRIVILEGES;"
      mysql -u root -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE < /ThriveX.sql
      echo "数据库初始化完成"
      rm -f /ThriveX.sql
  else
      echo "无法使用root登录,请检查MYSQL_ROOT_PASSWORD"
  fi
else
  echo "未找到ThriveX.sql文件,无需初始化数据库"
fi