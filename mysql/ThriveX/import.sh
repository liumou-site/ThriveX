#!/usr/bin/bash
echo "Starting import.sh"
# 使用普通用户导入数据
f="/ThriveX/ThriveX.sql"
mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE} < ${f}
if [ $? -eq 0 ]; then
  echo "数据导入成功"
else
  echo "数据导入失败"
  exit 1
fi
echo "数据导入完成"