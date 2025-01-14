# 使用官方的Node.js镜像作为基础镜像
FROM node:20-alpine AS builder

# 更新包列表并安装Git
RUN apk add --no-cache git

# 克隆代码
RUN git clone https://gitee.com/liu_yu_yang666/ThriveX-Blog.git /thrive

# 设置工作目录
WORKDIR /thrive

# 复制package.json和package-lock.json
COPY package*.json .

# 配置 npm 镜像源
RUN npm config set registry https://registry.npmmirror.com

# 安装依赖
RUN npm install

# 设置环境变量
ENV NEXT_PUBLIC_CACHING_TIME=0
ENV NEXT_PUBLIC_PROJECT_API=http://你的后端域名/api
ENV NEXT_PUBLIC_GAODE_KEY_CODE=高德地图key
ENV NEXT_PUBLIC_GAODE_SECURITYJS_CODE=高德地图秘钥

# 复制所有文件到工作目录
COPY . .

# 构建Next.js应用
RUN npm run build

# 暴露应用运行的端口
EXPOSE 9001

# 启动Next.js应用
CMD ["npm", "start"]