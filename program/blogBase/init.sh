#!/usr/bin/env sh
set -e
set -x
echo "Starting init.sh"
f=/blog/.env
if [[ ! -f "$f" ]]; then
		echo -e "Found no .env file: ${f}"
		exit 2
fi
grep $NEXT_PUBLIC_PROJECT_API  $f
if [[ $? -ne 0 ]]; then
		sed -i "s/NEXT_PUBLIC_PROJECT_API=.*/NEXT_PUBLIC_PROJECT_API=${NEXT_PUBLIC_PROJECT_API}/g" $f
fi
cat $f
if [[ -z ${NEXT_PUBLIC_GAODE_KEY_CODE} ]];then
	echo "NEXT_PUBLIC_GAODE_KEY_CODE is empty"
fi
if [[ -z ${NEXT_PUBLIC_GAODE_SECURITYJS_CODE} ]];then
	echo "NEXT_PUBLIC_GAODE_SECURITYJS_CODE is empty"
fi
cd /blog
npm start