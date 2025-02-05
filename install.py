# -*- coding: utf-8 -*-
import logging
import subprocess
import os
import sys
from argparse import ArgumentParser

# 预定义变量
mysql_path = "/data/ThriveX/mysql"
mysql_user = "ThriveX"
mysql_password = "ThriveX@123?"
mysql_host = "127.0.0.1"
mysql_port = "3306"

# 功能变量
install_set_sql = "1"
nginx_path = "/data/ThriveX/nginx"
pac = "apt"
url_compose_root = "https://github.com/liumou-site/ThriveX/blob/main"
compose_filename = "docker-compose.yaml"

# 创建一个自定义的日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个自定义的日志处理器，设置其输出格式
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d | %(funcName)s | %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
def install_lsof():
    # 检查是否已安装lsof
    if os.system("command -v lsof") == 0:
        logger.info("lsof 已安装")
        return
    if pac == "apt":
        try:
            run_command("apt update")
            run_command("apt install lsof -y")
        except subprocess.CalledProcessError:
            logger.error("安装lsof失败")
            sys.exit(1)
    elif pac == "yum":
        try:
            run_command("yum install lsof -y")
        except subprocess.CalledProcessError:
            logger.error("安装lsof失败")
            sys.exit(1)

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    return result.stdout

def download_compose_file():
    global url_compose_root, compose_filename
    url = f"{url_compose_root}/up/{compose_filename}"
    try:
        run_command(f"wget -O {compose_filename} {url}")
    except subprocess.CalledProcessError:
        logger.error(f"下载失败,请手动下载 {url}")
        sys.exit(1)

def set_mysql_password():
    global mysql_password
    while True:
        mysql_password = input("请输入数据库密码: ")
        if not mysql_password:
            logger.warning("密码不能为空")
            continue
        confirm_password = input("确认密码: ")
        if mysql_password != confirm_password:
            logger.warning("两次密码不一致")
            continue
        logger.info("密码设置成功")
        break

def set_nginx():
    global nginx_port
    if check_port_in_use(nginx_port):
        logger.warning(f"端口 {nginx_port} 已被占用,请修改端口")
        while True:
            nginx_port = input("请输入Nginx端口映射端口,默认: 9007: ")
            if not nginx_port:
                logger.debug("使用默认端口: 9007")
                nginx_port = "9007"
            if check_port_in_use(nginx_port):
                logger.warning(f"端口 {nginx_port} 已被占用,请修改端口")
            else:
                logger.info(f"端口 {nginx_port} 可用")
                break
    else:
        logger.info(f"端口 {nginx_port} 可用")

def check_port_in_use(port):
    install_lsof()
    result = os.system(f"lsof -i:{port}")
    return result == 0

def set_install_info():
    global mysql_path, mysql_user, mysql_password, mysql_host, mysql_port, install_set_sql
    logger.debug("开始设置安装信息")
    if install_set_sql == "1":
        mysql_path = input(f"[全新安装]请输入数据库映射路径(用于映射到容器内),默认: {mysql_path}: ")
        if not mysql_path:
            logger.debug(f"使用默认路径: {mysql_path}")
            mysql_path = "/data/ThriveX/mysql"
    mysql_user = input(f"请输入数据库用户名,默认: {mysql_user}: ")
    if not mysql_user:
        logger.debug(f"使用默认用户名: {mysql_user}")
        mysql_user = "ThriveX"
    set_mysql_password()
    mysql_host = input(f"请输入数据库主机,默认: {mysql_host}: ")
    if not mysql_host:
        logger.debug("使用默认主机")
        mysql_host = "10.178.178.10"
    mysql_port = input(f"请输入数据库映射端口,默认: {mysql_port}: ")
    if not mysql_port:
        logger.debug("使用默认端口")
        mysql_port = "3306"
def info():
    if args.sql:
        print(f"数据库映射路径: {mysql_path}")
    print(f"数据库用户名: {mysql_user}")
    print(f"数据库密码: {mysql_password}")
    print(f"数据库主机: {mysql_host}")
    print(f"数据库端口: {mysql_port}")
    print(f"Nginx端口: {nginx_port}")
    if nginx_port == 80:
        print("访问地址: http://127.0.0.1")
    else:
        print(f"访问地址: http://127.0.0.1:{nginx_port}")
    print("--------------------------------------")
def show():
    print("----------------信息确认----------------")
    info()
    confirm = input("是否继续安装?(y/n): ")
    if confirm.lower() != "y":
        print("取消安装")
        sys.exit(1)

def replace_config():
    global mysql_port, mysql_user, mysql_password, mysql_host, nginx_port, compose_filename
    if not os.path.isfile(compose_filename):
        logger.error("找不到docker-compose.yaml文件")
        sys.exit(1)
    if not mysql_port or not mysql_user or not mysql_password or not mysql_host:
        logger.error("数据库信息不能为空")
        sys.exit(1)
    with open(compose_filename, 'r') as file:
        content = file.read()
    content = content.replace("3306", mysql_port)
    content = content.replace("ThriveX", mysql_user)
    content = content.replace("ThriveX@123?", mysql_password)
    content = content.replace("10.178.178.10", mysql_host)
    set_nginx()
    logger.debug(f"{nginx_port}:80")
    content = content.replace('- ":80"', f'"{nginx_port}:80"')
    with open(compose_filename, 'w') as file:
        file.write(content)

def install_nosql():
    """
    安装NoSQL数据库服务。

    该函数通过下载配置文件并启动Docker容器来安装NoSQL数据库服务。
    它会全局设置docker-compose文件名，并通过替换配置文件中的占位符来配置服务。
    最后，它将启动服务并打印访问信息。
    """
    global compose_filename
    # 设置安装信息，可能包括从环境变量或配置文件中获取数据
    # set_install_info()
    # 显示安装信息
    show()
    # 指定docker-compose文件名用于NoSQL安装
    compose_filename = "docker-compose-nosql.yaml"
    # 下载docker-compose文件
    download_compose_file()
    # 记录安装开始日志
    logger.info("开始安装NoSQL")
    # 替换配置文件中的占位符为实际值
    replace_config()
    # 运行命令启动NoSQL服务容器
    run_command("docker-compose up -d")
    # 记录安装成功日志
    logger.info("安装成功")
    # 打印NoSQL服务的访问信息
    info()

def install_sql_dev():
    """
    安装SQL开发环境的函数。
    此函数负责执行SQL开发环境的安装过程，包括配置docker-compose文件、下载必要的文件、替换配置，
    以及运行Docker Compose命令来启动服务。
    """
    global compose_filename
    # 设置安装信息，可能包括一些预安装的配置或检查
    # set_install_info()
    # 显示安装信息或进度
    show()
    # 指定docker-compose文件名为开发环境的配置文件
    compose_filename = "docker-compose-dev.yaml"
    # 下载docker-compose配置文件
    download_compose_file()
    # 记录日志，开始安装
    logger.info("开始安装DevSQL")
    # 替换配置文件中的占位符为实际配置值
    replace_config()
    # 运行命令启动Docker Compose服务
    run_command("docker-compose up -d")
    # 安装完成后记录日志
    logger.info("安装成功")
    # 打印访问地址和数据库信息
    info()

def install_sql():
    global compose_filename
    # set_install_info()
    show()
    compose_filename = "docker-compose-sql.yaml"
    download_compose_file()
    logger.info("开始安装SQL")
    run_command(f"cp -rf up/{compose_filename} {compose_filename}")
    replace_config()
    run_command("docker-compose up -d")
    logger.info("安装成功")
    info()

def get_install_cmd():
    global pac
    if subprocess.run("command -v apt-get", shell=True, capture_output=True).returncode == 0:
        pac = "apt-get"
    elif subprocess.run("command -v yum", shell=True, capture_output=True).returncode == 0:
        pac = "yum"
    else:
        print("无法确定包管理工具,目前仅支持 apt-get 或 yum")
        sys.exit(1)

def check_install_info():
    global pac
    try:
        run_command("docker ps")
    except subprocess.CalledProcessError:
        logger.error("请先安装并启动docker服务")
        sys.exit(1)
    if not subprocess.run("command -v wget", shell=True, capture_output=True).returncode == 0:
        get_install_cmd()
        logger.info("wget 未安装，正在安装...")
        try:
            run_command(f"sudo {pac} install -y wget")
        except subprocess.CalledProcessError:
            logger.error("wget 安装失败，请手动安装")
            sys.exit(1)
    if not subprocess.run("command -v docker-compose", shell=True, capture_output=True).returncode == 0:
        get_install_cmd()
        logger.debug("docker-compose 未安装，正在安装...")
        try:
            run_command(f"sudo {pac} install -y docker-compose")
        except subprocess.CalledProcessError:
            logger.error("docker-compose 安装失败，请手动安装")
            sys.exit(1)
    if pac == "apt":
        if subprocess.run("dpkg -l | grep -v grep | grep docker-compose-plugin", shell=True, capture_output=True).returncode == 0:
            logger.info("docker-compose-plugin 已安装")
        else:
            logger.debug("docker-compose-plugin 未安装，正在安装...")
            try:
                run_command(f"sudo {pac} install -y docker-compose-plugin")
            except subprocess.CalledProcessError:
                logger.error("docker-compose-plugin 安装失败，请手动安装")
                sys.exit(1)
    else:
        if subprocess.run("rpm -qa | grep -v grep | grep docker-compose-plugin", shell=True, capture_output=True).returncode == 0:
            logger.info("docker-compose-plugin 已安装")
        else:
            logger.debug("docker-compose-plugin 未安装，正在安装...")
            try:
                run_command(f"sudo {pac} install -y docker-compose-plugin")
            except subprocess.CalledProcessError:
                logger.error("docker-compose-plugin 安装失败，请手动安装")
                sys.exit(1)

def main():
    check_install_info()
    print("请选择安装方式")
    print("1. 我需要全新安装数据库")
    print("2. 我有自己的数据库并有对应连接信息")
    print("3. 我需要自行构建镜像")
    option = input("请输入选项: ")
    if option == "1":
        install_sql()
    elif option == "2":
        install_nosql()
    elif option == "3":
        print("自行构建镜像")
    else:
        print("无效选项")
        sys.exit(1)

if __name__ == "__main__":
    arg = ArgumentParser(description='当前脚本版本: 1.0', prog="ThriveXInstall")
    h = f"指定数据库映射路径,默认: {mysql_path}l"
    arg.add_argument('-d', '--dir', type=str, help=h, default=mysql_path, required=False)
    arg.add_argument('-p', '--port', type=str, help="指定数据库端口,默认: 3306", default="3306", required=False)
    arg.add_argument('-u', '--user', type=str, help="指定数据库用户名,默认: ThriveX", default="ThriveX", required=False)
    arg.add_argument('-P', '--password', type=str, help="指定数据库密码,默认: ThriveX@123?", default="ThriveX@123?", required=False)
    arg.add_argument('-H', '--host', type=str, help="指定数据库地址,默认: 10.178.178.10", default="10.178.178.10", required=False)
    arg.add_argument('-n', '--nginx', type=str, help="指定nginx端口,默认: 9007", default=9007, required=False)
    arg.add_argument('-s', '--sql', action='store_true', help="安装sql数据库", default=False, required=False)
    arg.add_argument('-g', '--gitee', action='store_true', help="使用gitee下载docker-compose文件", default=False, required=False)
    arg.add_argument('-b', '--build', action='store_true', help="自行构建镜像", default=False, required=False)
    arg.add_argument('-dev', '--dev', action='store_true', help="使用开发版镜像运行", default=False, required=False)
    args = arg.parse_args()
    if args.gitee:
        url_compose_root = "https://gitee.com/liumou_site/ThriveX/raw/main"
    mysql_port=args.port
    mysql_user=args.user
    mysql_password=args.password
    mysql_host=args.host
    nginx_port=args.nginx
    mysql_path=args.dir
    if args.sql:
        install_sql()
    else:
        install_nosql()
    # if args.build:
    #     build_image()
