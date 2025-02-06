# 更新默认正式版镜像

```shell
sudo python3 install.py -update
```

## 效果
```shell
root@tb3:/data/git/ThriveX# python3 install.py -update
latest: Pulling from thrive/mysql
Digest: sha256:a31a35f55b815b510f3fa7ee5a16e75dd2643770126a4dae6af0fe3427ccc1af
Status: Image is up to date for registry.cn-hangzhou.aliyuncs.com/thrive/mysql:latest
registry.cn-hangzhou.aliyuncs.com/thrive/mysql:latest
latest: Pulling from thrive/nginx
fd674058ff8f: Already exists 
566e42bcee1c: Already exists 
2b99b9c5d9e5: Already exists 
bd98674871f5: Already exists 
1e109dd2a0d7: Already exists 
da8cc133ff82: Already exists 
c44f27309ea1: Already exists 
9a29f7e50a23: Already exists 
2f6717dc966f: Already exists 
bc2cdf9e6475: Already exists 
1a1816964dcc: Already exists 
Digest: sha256:a2dded33ace9dacc5285ad6aed9dcf2a558a70dcb1e1c02a53d2e1ec1ea5c008
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/thrive/nginx:latest
registry.cn-hangzhou.aliyuncs.com/thrive/nginx:latest
latest: Pulling from thrive/server
7e6a53d1988f: Already exists 
4fe4e1c58b4a: Already exists 
cc915d298757: Already exists 
0f795594794c: Already exists 
6cd61a4b7a06: Already exists 
62acc5f6f7aa: Already exists 
3464d75d5b00: Pull complete 
a02ad9e987ce: Pull complete 
Digest: sha256:a8812327cd0266c1c8b592435b757f2a86afb5c6f1ce89459b4e89bdc170d0ce
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/thrive/server:latest
registry.cn-hangzhou.aliyuncs.com/thrive/server:latest
latest: Pulling from thrive/admin
66a3d608f3fa: Already exists 
58290db888fa: Already exists 
5d777e0071f6: Already exists 
dbcfe8732ee6: Already exists 
37d775ecfbb9: Already exists 
e0350d1fd4dd: Already exists 
1f4aa363b71a: Already exists 
e74fff0a393a: Already exists 
65c8416b79b1: Pull complete 
Digest: sha256:c6130bf82dbd126931de752d72ca2c1a6650d14d54b57144839e295052a4495e
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/thrive/admin:latest
registry.cn-hangzhou.aliyuncs.com/thrive/admin:latest
latest: Pulling from thrive/blog
1f3e46996e29: Already exists 
280cf903519d: Already exists 
3e4c58ea8b08: Already exists 
f5c4456c2e24: Already exists 
cd6f37273b57: Pull complete 
2e77728a7a40: Pull complete 
4f4fb700ef54: Pull complete 
cbe71a041ab3: Pull complete 
b9aa00cb82b8: Pull complete 
69cc6c6f6ad4: Pull complete 
Digest: sha256:31e0b670a3a4a85c8413c890e4721ef8ce6b27ba8838878943619fbf107c0641
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/thrive/blog:latest
registry.cn-hangzhou.aliyuncs.com/thrive/blog:latest
root@tb3:/data/git/ThriveX# 
```



# 更新`dev`镜像
## 命令
```shell
sudo python3 install.py -dev -update
```

## 效果

```shell
root@tb3:/data/git/ThriveX# python3 install.py -dev -update
dev: Pulling from thrive/mysql
2c0a233485c3: Already exists 
fb027c65a85c: Already exists 
d87e05573c29: Already exists 
7d202bd608a9: Already exists 
930324cdd290: Already exists 
441e29354b23: Already exists 
4f0710d03b24: Already exists 
ead7d3dd9cc0: Already exists 
55d2712d2c86: Already exists 
4aaa23a8b413: Already exists 
84ba6b75f842: Already exists 
4f4fb700ef54: Already exists 
57abdfe5dd1b: Pull complete 
a740eb400cb3: Pull complete 
Digest: sha256:f78b5e810be32e25b5d48201d7ae96c536ba0e566af234be343c2bbea448adee
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/thrive/mysql:dev
registry.cn-hangzhou.aliyuncs.com/thrive/mysql:dev
dev: Pulling from thrive/nginx
Digest: sha256:726f1559eb97fa98a4ad4d7430d028c503cca549910f157b5cf3f1139fbe309b
Status: Image is up to date for registry.cn-hangzhou.aliyuncs.com/thrive/nginx:dev
registry.cn-hangzhou.aliyuncs.com/thrive/nginx:dev
dev: Pulling from thrive/server
7e6a53d1988f: Already exists 
4fe4e1c58b4a: Already exists 
cc915d298757: Already exists 
0f795594794c: Already exists 
6cd61a4b7a06: Already exists 
62acc5f6f7aa: Already exists 
37eaa6357683: Pull complete 
f6459336413f: Pull complete 
Digest: sha256:484bf0aa8baaabd0ce2464526cb6cd684dfd8f34ec7063faecee0171b8b45d6d
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/thrive/server:dev
registry.cn-hangzhou.aliyuncs.com/thrive/server:dev
dev: Pulling from thrive/admin
66a3d608f3fa: Already exists 
58290db888fa: Already exists 
5d777e0071f6: Already exists 
dbcfe8732ee6: Already exists 
37d775ecfbb9: Already exists 
e0350d1fd4dd: Already exists 
1f4aa363b71a: Already exists 
e74fff0a393a: Already exists 
9bb3af2e76f3: Pull complete 
Digest: sha256:550c7dfbd5016b6cea7378c7bc8897f7196b4f8600d480e262a824f022e48b39
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/thrive/admin:dev
registry.cn-hangzhou.aliyuncs.com/thrive/admin:dev
dev: Pulling from thrive/blog
Digest: sha256:f7bc637370ab30240dabf6ebb4ffec77ebb8164fdd9dcf11d33ce63c04069588
Status: Image is up to date for registry.cn-hangzhou.aliyuncs.com/thrive/blog:dev
registry.cn-hangzhou.aliyuncs.com/thrive/blog:dev
root@tb3:/data/git/ThriveX# 
```