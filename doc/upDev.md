```shell
root@tb3:/data/git/ThriveX# cp -rf up/docker-compose-dev.yaml docker-compose.yaml 
root@tb3:/data/git/ThriveX# docker-compose up -d
Recreating server ... done
Recreating mysql  ... done
Recreating nginx  ... done
Recreating admin  ... done
Recreating blog   ... done
root@tb3:/data/git/ThriveX# docker ps
CONTAINER ID   IMAGE                                                 COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
e9dcd77d7336   registry.cn-hangzhou.aliyuncs.com/thrive/mysql:dev    "docker-entrypoint.s…"   3 seconds ago   Up 2 seconds   33060/tcp, 0.0.0.0:3307->3306/tcp, :::3307->3306/tcp   thrive_mysql
57ca0266c7c8   registry.cn-hangzhou.aliyuncs.com/thrive/admin:dev    "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:9002->80/tcp, :::9002->80/tcp                  thrive_admin
cd19339a3887   registry.cn-hangzhou.aliyuncs.com/thrive/nginx:dev    "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:9007->80/tcp, :::9007->80/tcp                  thrive_nginx
9d8031a9607a   registry.cn-hangzhou.aliyuncs.com/thrive/blog:dev     "docker-entrypoint.s…"   4 seconds ago   Up 3 seconds   0.0.0.0:9001->9001/tcp, :::9001->9001/tcp              thrive_blog
05dd3347f755   registry.cn-hangzhou.aliyuncs.com/thrive/server:dev   "java -jar server.jar"   4 seconds ago   Up 4 seconds   0.0.0.0:9003->9003/tcp, :::9003->9003/tcp              thrive_server
root@tb3:/data/git/ThriveX# 
```