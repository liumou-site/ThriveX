#!/usr/bin/env sh
set -e
if [ ! -f /admin/.env ];then
	echo "Not found .env file"
	exit 1
fi
sed -i "s@VITE_PROJECT_API=.*@VITE_PROJECT_API=${VITE_PROJECT_API}" /admin/.env
cd /admin
npm run dev