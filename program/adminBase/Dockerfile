# 使用官方的Node.js镜像作为基础镜像
FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/node-20-alpine AS builder
# 设置环境变量，存储构建时间（北京时间）
ENV BUILD_TIME=2025-2-6_18:05:23

# 使用 LABEL 指令将构建时间设置为镜像的标签
LABEL build_time="${BUILD_TIME}"
# 更新包列表并安装Git
RUN sed -i 's#https\?://dl-cdn.alpinelinux.org/alpine#https://mirrors.tuna.tsinghua.edu.cn/alpine#g' /etc/apk/repositories&&apk update&&apk add --no-cache git
# 设置主机DNS
COPY resolv.conf /etc/resolv.conf
# 克隆代码
RUN git clone https://gitee.com/liumou_site/Thrive-Admin.git /admin
# 设置工作目录
WORKDIR /admin


# 配置 npm 镜像源
RUN npm config set registry https://registry.npmmirror.com

# 安装依赖
RUN npm install

# 设置环境变量(必须改为自己的且外部浏览器可访问的后端地址)
ENV VITE_PROJECT_API=http://server.thrive.site:9003/api
## 百度统计站点ID
ENV VITE_BAIDU_TONGJI_SITE_ID=""
## 百度统计秘钥
ENV VITE_BAIDU_TONGJI_ACCESS_TOKEN=""
## AI大模型秘钥
ENV VITE_AI_APIPassword=""
ENV VITE_AI_MODEL=lite
## 高德地图坐标秘钥
ENV VITE_GAODE_WEB_API=""
# 构建项目
#RUN npm run build
COPY init.sh /admin/init.sh
RUN chmod +x /admin/init.sh
## 使用 Nginx 作为生产环境的基础镜像
#FROM registry.cn-hangzhou.aliyuncs.com/liuyi778/nginx:alpine
#
## 复制构建输出到 Nginx 的默认静态文件目录
#COPY --from=builder /admin/dist /usr/share/nginx/html
#
## 暴露端口
#EXPOSE 80

# 启动 Nginx
#CMD ["nginx", "-g", "daemon off;"]
CMD ["/admin/init.sh"]