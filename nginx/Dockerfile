FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/nginx
LABEL authors="SER8"
# 覆盖nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
# 端口
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]