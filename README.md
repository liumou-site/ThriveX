# ThriveX

## 安装

第一步、拉取代码：

```
git clone https://gitee.com/liu_yu_yang666/ThriveX
```

```
root@new:/wwwroot# git clone https://gitee.com/liu_yu_yang666/ThriveX.git
Cloning into 'ThriveX'...
remote: Enumerating objects: 37, done.
remote: Counting objects: 100% (37/37), done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 37 (delta 5), reused 37 (delta 5), pack-reused 0
Receiving objects: 100% (37/37), 66.16 MiB | 2.39 MiB/s, done.
Resolving deltas: 100% (5/5), done.
root@new:/wwwroot# 
```



第二步、进入项目

```
cd ThriveX
```

```
root@new:/wwwroot# cd ThriveX
root@new:/wwwroot/ThriveX# ls
README.md  compose.yaml  mysql  nginx  program
root@new:/wwwroot/ThriveX# 
```



第三步、配置环境变量
如：数据库、Nginx等配置



第四步、执行命令

```
docker compose -p thrive up -d --build
```

```
root@new:/wwwroot/ThriveX# docker compose -p thrive up -d --build
WARN[0000] /wwwroot/ThriveX/compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 0.0s (0/1)                                            docker:default
[+] Running 0/1
[+] Building 1.0s (7/8)                                            docker:default 
 => [server internal] load .dockerignore                                     0.0s
 ✔ Service server  Built                                                     1.1s 
 ⠏ Service blog    Building                                                 35.0s 
[+] Building 36.1s (30/35)                                         docker:default
[+] Building 156.3s (39/39) FINISHED                                                                                                                                                                   docker:default
 => [server internal] load build definition from Dockerfile                                                                                                                                                      0.0s
 => => transferring dockerfile: 315B                                                                                                                                                                             0.0s
 => [server internal] load metadata for docker.io/library/openjdk:11.0-jre-buster                                                                                                                                0.2s
 => [server internal] load .dockerignore                                                                                                                                                                         0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [server 1/3] FROM docker.io/library/openjdk:11.0-jre-buster@sha256:569ba9252ddd693a29d39e81b3123481f308eb6d529827a40c93710444e421b0                                                                          0.0s
 => [server internal] load build context                                                                                                                                                                         0.3s
 => => transferring context: 76.58MB                                                                                                                                                                             0.3s
 => CACHED [server 2/3] WORKDIR /thrive                                                                                                                                                                          0.0s
 => [server 3/3] COPY blog.jar /thrive/app.jar                                                                                                                                                                   0.4s
 => [server] exporting to image                                                                                                                                                                                  0.1s
 => => exporting layers                                                                                                                                                                                          0.1s
 => => writing image sha256:3f8bddfc90d800ba603d7b9d28cb28392ac49037ad19b17da914f47238f24bb2                                                                                                                     0.0s
 => => naming to docker.io/library/thrive-server                                                                                                                                                                 0.0s
 => [server] resolving provenance for metadata file                                                                                                                                                              0.0s
 => [admin internal] load build definition from Dockerfile                                                                                                                                                       0.0s
 => => transferring dockerfile: 810B                                                                                                                                                                             0.0s
 => [blog internal] load build definition from Dockerfile                                                                                                                                                        0.0s
 => => transferring dockerfile: 654B                                                                                                                                                                             0.0s
 => [admin internal] load metadata for docker.io/library/nginx:alpine                                                                                                                                            0.1s
 => [admin internal] load metadata for docker.io/library/node:20-alpine                                                                                                                                          2.2s
 => [admin internal] load .dockerignore                                                                                                                                                                          0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [blog internal] load .dockerignore                                                                                                                                                                           0.0s 
 => => transferring context: 2B                                                                                                                                                                                  0.0s 
 => [admin stage-1 1/2] FROM docker.io/library/nginx:alpine@sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4                                                                              0.0s 
 => [blog builder 1/9] FROM docker.io/library/node:20-alpine@sha256:24fb6aa7020d9a20b00d6da6d1714187c45ed00d1eb4adb01395843c338b9372                                                                             0.0s
 => [admin internal] load build context                                                                                                                                                                          0.0s
 => => transferring context: 810B                                                                                                                                                                                0.0s
 => [blog internal] load build context                                                                                                                                                                           0.0s
 => => transferring context: 654B                                                                                                                                                                                0.0s
 => CACHED [admin builder 2/9] RUN apk add --no-cache git                                                                                                                                                        0.0s
 => CACHED [blog 3/9] RUN git clone https://gitee.com/liu_yu_yang666/ThriveX-Blog.git /thrive                                                                                                                    0.0s
 => CACHED [blog 4/9] WORKDIR /thrive                                                                                                                                                                            0.0s
 => CACHED [admin builder 3/9] RUN git clone https://gitee.com/liu_yu_yang666/ThriveX-Admin.git /thrive                                                                                                          0.0s
 => CACHED [admin builder 4/9] WORKDIR /thrive                                                                                                                                                                   0.0s
 => CACHED [admin builder 5/9] COPY package*.json ./                                                                                                                                                             0.0s
 => CACHED [admin builder 6/9] RUN npm config set registry https://registry.npmmirror.com                                                                                                                        0.0s
 => CACHED [admin builder 7/9] RUN npm install                                                                                                                                                                   0.0s 
 => [blog 5/9] COPY package*.json .                                                                                                                                                                              0.0s 
 => [admin builder 8/9] COPY . .                                                                                                                                                                                 0.0s 
 => [blog 6/9] RUN npm config set registry https://registry.npmmirror.com                                                                                                                                        0.6s
 => [admin builder 9/9] RUN npm run build                                                                                                                                                                       35.3s
 => [blog 7/9] RUN npm install                                                                                                                                                                                  81.0s
 => CACHED [admin stage-1 2/2] COPY --from=builder /thrive/dist /usr/share/nginx/html                                                                                                                            0.0s
 => [admin] exporting to image                                                                                                                                                                                   0.0s
 => => exporting layers                                                                                                                                                                                          0.0s
 => => writing image sha256:17dec6bb92c292531b08f1b7e424cad8b128407d451e73750c5cb1e8734e2007                                                                                                                     0.0s
 => => naming to docker.io/library/thrive-admin                                                                                                                                                                  0.0s
 => [admin] resolving provenance for metadata file                                                                                                                                                               0.0s 
 => [blog 8/9] COPY . .                                                                                                                                                                                          0.0s 
 => [blog 9/9] RUN npm run build                                                                                                                                                                                67.7s 
 => [blog] exporting to image                                                                                                                                                                                    3.5s 
[+] Running 10/10layers                                                                                                                                                                                          3.5s 
 ✔ Service server                 Built                                                                                                                                                                          1.1s 
 ✔ Service blog                   Built                                                                                                                                                                        155.2s 
 ✔ Service admin                  Built                                                                                                                                                                         38.2s 
 ✔ Network thrive_thrive_network  Created                                                                                                                                                                        0.1s 
 ✔ Container mysql                Started                                                                                                                                                                        0.4s 
 ✔ Container server               Started                                                                                                                                                                        0.6s 
 ✔ Container mysql_backup         Started                                                                                                                                                                        0.6s 
 ✔ Container admin                Started                                                                                                                                                                        1.1s 
 ✔ Container nginx                Started                                                                                                                                                                        1.2s 
 ✔ Container blog                 Started                                                 
```



查看当前项目状态

```
root@new:/wwwroot/ThriveX# docker ps
CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS         PORTS                                                           NAMES
8f08e6c938c4   thrive-server         "java -jar app.jar"      6 seconds ago   Up 5 seconds   0.0.0.0:9003->9003/tcp, :::9003->9003/tcp                       server
1c3720311a6c   thrive-admin          "/docker-entrypoint.…"   2 minutes ago   Up 5 seconds   0.0.0.0:9002->80/tcp, [::]:9002->80/tcp                         admin
0d231d6c74bd   thrive-blog           "docker-entrypoint.s…"   2 minutes ago   Up 5 seconds   0.0.0.0:9001->9001/tcp, :::9001->9001/tcp                       blog
50a50547a599   nginx:latest          "/docker-entrypoint.…"   2 minutes ago   Up 5 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp                               nginx
c82000f6fcc2   mysql:8.0             "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   3306/tcp, 33060/tcp                                             mysql_backup
292cf0b978ad   mysql:8.0             "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   33060/tcp, 0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp          mysql
```




## 卸载

```
docker compose -p thrive down
```