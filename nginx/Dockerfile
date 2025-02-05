FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/nginx
LABEL authors="SER8"
# 设置环境变量，存储构建时间（北京时间）
ENV BUILD_TIME=2025年2月5日16:27:27

# 使用 LABEL 指令将构建时间设置为镜像的标签
LABEL build_time="${BUILD_TIME}"
# 覆盖nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.conf /etc/nginx/conf.d/app.conf
# 覆盖.conf
#COPY conf.d/index.conf /etc/nginx/conf.d/default.conf
#COPY conf.d/admin.conf /etc/nginx/conf.d/admin.conf
#COPY conf.d/api.conf /etc/nginx/conf.d/api.conf
COPY conf.d/proxy_headers.conf /etc/nginx/proxy_headers.conf
# 添加 404 页面
COPY 404.html /usr/share/nginx/html/404.html
# 端口
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]