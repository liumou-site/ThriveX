FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/nginx
LABEL authors="SER8"
# 覆盖nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
# 覆盖.conf
COPY conf.d/index.conf /etc/nginx/conf.d/default.conf
COPY conf.d/admin.conf /etc/nginx/conf.d/admin.conf
COPY conf.d/api.conf /etc/nginx/conf.d/api.conf
# 端口
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]