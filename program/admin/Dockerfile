# 使用官方的Node.js镜像作为基础镜像
FROM registry.cn-hangzhou.aliyuncs.com/thrive/admin AS builder
# 设置环境变量，存储构建时间（北京时间）
ENV BUILD_TIME=2025-2-6_18:05:23

# 使用 LABEL 指令将构建时间设置为镜像的标签
LABEL build_time="${BUILD_TIME}"
# 设置工作目录
WORKDIR /admin

# 更新Git仓库
RUN git pull&&npm install

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
CMD ["/admin/init.sh"]