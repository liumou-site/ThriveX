# 使用官方的Node.js镜像作为基础镜像
FROM node:20-alpine AS builder

# 更新包列表并安装Git
RUN sed -i 's#https\?://dl-cdn.alpinelinux.org/alpine#https://mirrors.tuna.tsinghua.edu.cn/alpine#g' /etc/apk/repositories&&apk update&&apk add --no-cache git

# 克隆代码
RUN git clone https://gitee.com/liu_yu_yang666/ThriveX-Admin.git /thrive

# 设置工作目录
WORKDIR /thrive


# 配置 npm 镜像源
RUN npm config set registry https://registry.npmmirror.com

# 安装依赖
RUN npm install

# 设置环境变量
ENV VITE_PROJECT_API=http://你的后端域名/api
## 百度统计站点ID
ENV VITE_BAIDU_TONGJI_SITE_ID=""
## 百度统计秘钥
ENV VITE_BAIDU_TONGJI_ACCESS_TOKEN=""
## AI大模型秘钥
ENV VITE_AI_APIPassword=""
ENV VITE_AI_MODEL=lite
## 高德地图坐标秘钥
ENV VITE_GAODE_WEB_API=""

# 复制项目文件
COPY . .

# 构建项目
RUN npm run build

# 使用 Nginx 作为生产环境的基础镜像
FROM nginx:alpine

# 复制构建输出到 Nginx 的默认静态文件目录
COPY --from=builder /thrive/dist /usr/share/nginx/html

# 暴露端口
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
