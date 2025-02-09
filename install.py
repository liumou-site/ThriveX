# -*- coding: utf-8 -*-
import logging
import re
import subprocess
import os
import sys
from argparse import ArgumentParser
import tomllib
from shutil import copy2

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
pwd=os.getcwd()

# 创建一个自定义的日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个自定义的日志处理器，设置其输出格式
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d | %(funcName)s | %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)

def create_demo(file):
	"""
	创建一个示例配置文件
	:param file:
	:return:
	"""
	txt = """[mysql]
name="ThriveX" # 数据库名称
host="mysql.thrive.site" # 数据库主机地址,不要使用 localhost
port=3306 # 数据库端口
user="thrive" # 数据库用户名
password="ThriveX@123?" # 数据库密码
install=true # 如果为true则安装数据库,如果为false则使用已有的数据库服务器,不再进行安装
root_password="ThriveX@123?" # 如果install为true,则需要填写root密码,否则忽略此参数
path="/data/ThriveX/mysql" # 数据库存储路径,如果设置install为true则需要设置此参数,否则忽略此参数

[email]
host="smtp.qq.com" # 邮件服务器地址
port=465 # 邮件服务器端口
user="liumou.site@qq.com" # 邮箱用户名
password="ThisIsTest" # 邮箱密码

[server]
backend="http://DomainName/api" # 设置后端服务器地址,必须 /api结尾

[api]
NEXT_PUBLIC_PROJECT_API="http://DomainName/api" # 设置前端项目的API地址
NEXT_PUBLIC_GAODE_KEY_CODE="Value_NEXT_PUBLIC_GAODE_KEY_CODE" # 设置高德地图的key
NEXT_PUBLIC_GAODE_SECURITYJS_CODE="Value_NEXT_PUBLIC_GAODE_SECURITYJS_CODE" # 高德地图秘钥
VITE_GAODE_WEB_API_KEY="Value_VITE_GAODE_WEB_API_KEY" # 高德地图web api秘钥

[baidu]
VITE_BAIDU_TONGJI_SITE_ID="Value_VITE_BAIDU_TONGJI_SITE_ID" # 百度统计的site_id
VITE_BAIDU_TONGJI_ACCESS_TOKEN="Value_VITE_BAIDU_TONGJI_ACCESS_TOKEN" # 百度统计的access_token

[ai]
VITE_AI_APIPassword="Value_VITE_AI_APIPassword" # 讯飞AI的API密码
"""
	try:
		with open(file, 'w', encoding='utf-8') as f:
			f.write(txt)
			f.close()
	except Exception as e:
		logger.error(f"创建文件失败: {e}")
		sys.exit(1)
	logger.info(f"创建模板文件成功: {file}")



def get_user_input(prompt, default=None, validation=None):
	"""
	获取用户输入，并根据条件进行验证。

	参数:
	prompt (str): 提示用户的输入信息。
	default (any, optional): 如果用户没有提供输入，则返回的默认值。默认为None。
	validation (callable, optional): 一个用于验证用户输入的函数。如果提供，该函数应接受一个参数并返回一个布尔值。
									 默认为None，表示不进行验证。

	返回:
	any: 用户的输入或默认值。
	"""
	while True:
		# 显示提示信息并获取用户输入
		user_input = input(prompt)
		# 如果用户没有输入且存在默认值，则返回默认值
		if not user_input and default is not None:
			return default
		# 如果用户输入不通过验证，则记录警告日志并重新循环
		if validation and not validation(user_input):
			logging.warning("输入无效，请重试。")
			continue
		# 输入通过验证，返回用户输入
		return user_input

def read_toml(filename):
	try:
		with open(filename, 'r', encoding='utf-8') as file:
			content = file.read()
	except FileNotFoundError:
		logger.error(f"文件 {filename} 不存在")
		sys.exit(1)
	except Exception as e:
		logger.error(f"读取文件 {filename} 时出错: {e}")
		sys.exit(1)
	# 解析 TOML 文件内容
	try:
		return tomllib.loads(content)
	except Exception as e:
		logger.error(f"解析文件 {filename} 时出错: {e}")
		sys.exit(1)

def install_lsof():
	"""
	安装lsof工具。
	先检查是否已安装lsof，如果未安装，则根据系统的包管理器类型（apt或yum）来安装lsof。
	"""
	# 检查是否已安装lsof
	if os.system("command -v lsof") == 0:
		logger.info("lsof 已安装")
		return
	# 根据包管理器类型安装lsof
	if pac == "apt":
		try:
			# 更新软件包列表
			os.system("apt update")
			# 安装lsof
			os.system("apt install lsof -y")
		except subprocess.CalledProcessError:
			logger.error("安装lsof失败")
			sys.exit(1)
	elif pac == "yum":
		try:
			# 安装lsof
			os.system("yum install lsof -y")
		except subprocess.CalledProcessError:
			logger.error("安装lsof失败")
			sys.exit(1)
	else:
		logger.error("未知的包管理器类型")
		sys.exit(1)
def install_pac(name):
	cmd = f"{pac} install {name} -y"
	try:
		os.system(cmd)
	except subprocess.CalledProcessError:
		logger.error(f"安装[ {name} ]失败")
		sys.exit(1)
def install_docker():
	pac_list = ["docker-compose-plugin", "docker-compose"]
	for p in pac_list:
		# 如果是apt则使用dpkg查看
		if pac == "apt":
			cmd = f"dpkg -l | grep {p}"
		elif pac == "yum":
			cmd = f"rpm -qa | grep {p}"
		else:
			logger.error("未知的包管理器类型")
			sys.exit(1)
		if os.system(cmd) == 0:
			logger.info(f"{p} 已安装")
			continue
		else:
			logger.error(f"{p} 未安装")
			install_pac(p)
	pac_list = ["docker.io", "docker-ce", "docker-engine"]
	for p in pac_list:
		if pac == "apt":
			cmd = f"dpkg -l | grep ii | grep {p}"
		elif pac == "yum":
			cmd = f"rpm -qa | grep {p}"
		else:
			logger.error("未知的包管理器类型,仅支持apt和yum")
			sys.exit(1)
		if os.system(cmd) == 0:
			logger.info(f"{p} 已安装")
			continue
	logger.error("docker未安装,正在安装docker")
	os.environ["DOWNLOAD_URL"] = "https://mirrors.tuna.tsinghua.edu.cn/docker-ce"
	if os.system("command -v curl") == 0:
		if os.system("curl -fsSL https://raw.githubusercontent.com/docker/docker-install/master/install.sh | sh") != 0:
			logger.error("安装Docker-ce失败")
			sys.exit(1)
	else:
		if os.system("command -v wget") == 0:
			if os.system("wget -O- https://raw.githubusercontent.com/docker/docker-install/master/install.sh | sh") != 0:
				logger.error("安装Docker-ce失败")
				sys.exit(1)
		else:
			install_pac("curl")
			if os.system("curl -fsSL https://raw.githubusercontent.com/docker/docker-install/master/install.sh | sh") != 0:
				logger.error("安装Docker-ce失败")
				sys.exit(1)


class BuildInstall:
	def __init__(self):
		self.VITE_AI_APIPassword = None
		self.VITE_BAIDU_TONGJI_ACCESS_TOKEN = None
		self.VITE_BAIDU_TONGJI_SITE_ID = None
		self.email_port = None
		self.email_host = None
		self.backend = None
		# 数据库主机地址，初始值为None，表示尚未设置数据库主机
		self.db_host = None
		# 数据库端口，初始值为3306，这是MySQL数据库的默认端口
		self.db_port = 3306
		# 数据库用户名，初始值为None，表示尚未设置数据库用户名
		self.db_user = None
		# 数据库密码，初始值为None，表示尚未设置数据库密码
		self.db_password = None
		# 数据库名称，初始值为None，表示尚未设置数据库名称
		self.db_name = None
		# 数据库路径
		self.db_path = None
		# 电子邮件用户名，初始值为None，表示尚未设置用于发送邮件的邮箱用户名
		self.email_user = None
		# 电子邮件密码，初始值为None，表示尚未设置用于发送邮件的邮箱密码
		self.email_password = None

		self.NEXT_PUBLIC_PROJECT_API = None
		self.NEXT_PUBLIC_GAODE_KEY_CODE = None
		self.NEXT_PUBLIC_GAODE_SECURITYJS_CODE = None
		self.VITE_GAODE_WEB_API_KEY = None
		# 设置源文件
		self.src = "docker/docker-compose.yaml"
		self.dst = "./docker-compose.yml"
		# 安装选项
		self.install_mysql = False

	def get_user_input(self):
		"""
		获取数据库和邮箱配置。

		本函数通过检查环境变量和用户输入来获取数据库和邮箱的配置信息。
		它按需请求数据库地址、端口、用户名、密码、数据库名称以及邮箱地址和密码。
		"""
		# 检查数据库地址配置，优先使用环境变量配置
		if not self.db_host:
			if os.getenv("THRIVEX_DB_HOST"):
				self.db_host = os.getenv("THRIVEX_DB_HOST")
			else:
				self.db_host = get_user_input("请输入数据库地址: ")

		# 检查数据库端口配置，优先使用环境变量配置，并进行数字验证
		if not self.db_port:
			if os.getenv("THRIVEX_DB_PORT"):
				self.db_port = os.getenv("THRIVEX_DB_PORT")
			else:
				self.db_port = get_user_input("请输入数据库端口，默认: 3306: ", default=3306, validation=lambda x: re.match(r"^[0-9]+$", x))

		# 检查数据库用户名配置，优先使用环境变量配置
		if not self.db_user:
			if os.getenv("THRIVEX_DB_USER"):
				self.db_user = os.getenv("THRIVEX_DB_USER")
			else:
				self.db_user = get_user_input("请输入数据库用户名，默认: thrive: ", default="thrive")

		# 请求数据库密码输入，确保密码中不包含竖线字符
		if not self.db_password:
			self.db_password = get_user_input("请输入数据库密码: ", validation=lambda x: "|" not in x)

		# 检查数据库名称配置，优先使用环境变量配置
		if not self.db_name:
			if os.getenv("THRIVEX_DB_NAME"):
				self.db_name = os.getenv("THRIVEX_DB_NAME")
			else:
				self.db_name = get_user_input("请输入数据库名称，默认: ThriveX: ", default="ThriveX")
		if not self.db_path:
			if os.getenv("THRIVEX_DB_PATH"):
				self.db_path = os.getenv("THRIVEX_DB_PATH")
			else:
				self.db_path = get_user_input("请输入数据库路径: ", default="/var/lib/mysql")
		# 检查邮箱地址配置，优先使用环境变量配置，并进行竖线字符验证
		if not self.email_user:
			if os.getenv("THRIVEX_EMAIL"):
				self.email_user = os.getenv("THRIVEX_EMAIL")
			else:
				self.email_user = get_user_input("请输入你的邮箱地址，默认: 123456789@qq.com: ", default="123456789@qq.com", validation=lambda x: "|" not in x)

		# 检查邮箱密码配置，优先使用环境变量配置，并进行竖线字符验证
		if not self.email_password:
			if os.getenv("THRIVEX_EMAIL_PASSWORD"):
				self.email_password = os.getenv("THRIVEX_EMAIL_PASSWORD")
			else:
				self.email_password = get_user_input("请输入你的邮箱密码，默认: 123456789: ", default="123456", validation=lambda x: "|" not in x)
	def show(self):
		"""
		显示当前的数据库和邮箱配置。

		该方法打印出数据库地址、端口、用户名、密码、数据库名称以及邮箱地址和密码。
		用户需要按回车键继续，或按Ctrl+C取消。
		"""
		print("--------------------------------------------------------------")
		print("----------------数据库配置----------------")
		print(f"数据库地址: {self.db_host}")
		print(f"数据库端口: {self.db_port}")
		print(f"数据库用户名: {self.db_user}")
		print(f"数据库密码: {self.db_password}")
		print(f"数据库名称: {self.db_name}")
		if self.install_mysql:
			print("安装数据库: 是")
			print(f"数据库路径: {self.db_path}")
		print("----------------邮箱配置----------------")
		print(f"邮箱地址: {self.email_user}")
		print(f"邮箱密码: {self.email_password}")
		print(f"邮箱端口: {self.email_port}")
		print(f"邮箱主机: {self.email_host}")
		print("----------------后端URL----------------")
		print(f"后端URL: {self.backend}")
		print("----------------其他配置----------------")
		print(f"AI大模型秘钥: {self.VITE_AI_APIPassword}")
		print(f"百度统计秘钥: {self.VITE_BAIDU_TONGJI_ACCESS_TOKEN}")
		print(f"百度统计站点ID: {self.VITE_BAIDU_TONGJI_SITE_ID}")
		print(f"高德地图key: {self.NEXT_PUBLIC_GAODE_KEY_CODE}")
		print(f"高德地图坐标秘钥: {self.VITE_GAODE_WEB_API_KEY}")
		print(f"高德地图秘钥: {self.NEXT_PUBLIC_GAODE_SECURITYJS_CODE}")
		print("--------------------------------------------------------------")
		input("按回车键继续,按Ctrl+C取消...\n")
		print("正在安装,请耐心等待...")
	def set_env(self):
		"""
		设置环境变量，用于配置数据库和电子邮件相关信息。

		本函数将实例变量中的数据库和电子邮件信息设置为环境变量，
		以便其他部分的代码可以访问这些配置信息。
		"""
		# 设置数据库主机环境变量
		os.environ["THRIVEX_DB_HOST"] = self.db_host
		# 设置数据库端口环境变量，确保端口为字符串形式
		os.environ["THRIVEX_DB_PORT"] = str(self.db_port)
		# 设置数据库用户名环境变量
		os.environ["THRIVEX_DB_USER"] = self.db_user
		# 设置数据库密码环境变量
		os.environ["THRIVEX_DB_PASSWORD"] = self.db_password
		# 设置数据库名称环境变量
		os.environ["THRIVEX_DB_NAME"] = self.db_name
		# 设置电子邮件用户名环境变量
		os.environ["THRIVEX_EMAIL"] = self.email_user
		# 设置电子邮件密码环境变量
		os.environ["THRIVEX_EMAIL_PASSWORD"] = self.email_password
	def replace_in_file(self, pattern, replacement):
		"""
		在文件中替换所有匹配的模式。

		尝试打开目标文件，并读取其内容。使用正则表达式在文件内容中查找所有匹配模式的字符串，
		并用指定的替换字符串替换它们。然后，将修改后的内容写回目标文件。

		参数:
		pattern (str): 需要被替换的字符串模式。
		replacement (str): 替换字符串。

		返回:
		无返回值。
		"""
		try:
			# 打开目标文件以读取内容
			with open(self.dst, 'r', encoding='utf-8') as file:
				content = file.read()
				file.close()
		except Exception as e:
			# 如果读取文件时发生错误，则记录错误并退出程序
			logging.error(f"读取文件失败: {e}")
			sys.exit(1)

		# 使用正则表达式替换所有匹配模式的字符串
		content = re.sub(pattern, replacement, content)

		try:
			# 打开目标文件以写入修改后的内容
			with open(self.dst, 'w', encoding='utf-8') as file:
				file.write(content)
				file.close()
		except Exception as e:
			# 如果写入文件时发生错误，则记录错误并退出程序
			logger.error(f"写入文件失败: {e}")
			sys.exit(1)
	def get_docker_status(self):
		"""
		检查 Docker 的安装和运行状态。

		此方法首先检查 Docker 是否已安装，如果未安装，则尝试自动安装。
		如果 Docker 仍然未安装成功，程序将记录错误信息并退出。
		如果 Docker 已安装但未运行，将尝试启动 Docker 服务。
		如果 Docker 服务无法启动，程序将记录错误信息并退出。
		如果 Docker 服务正在运行，将记录相应的信息。
		"""
		# 检查 Docker 是否已安装
		if os.system("command -v docker") != 0:
			install_docker()

		# 再次检查 Docker 是否已安装
		if os.system("command -v docker") != 0:
			logger.error("Docker 未安装，请安装 Docker 后重试。")
			sys.exit(1)

		# 检查 Docker 服务是否在运行
		if os.system("docker ps > /dev/null 2>&1") != 0:
			# 尝试启动 Docker 服务
			if os.system("systemctl start docker") != 0:
				logger.error("Docker 无法启动，请解决后重试。")
				sys.exit(1)

		# Docker 服务正在运行
		logger.info("Docker 正在运行")
	def copy(self):
		"""
		根据是否需要安装MySQL，选择不同的配置文件进行复制操作。
		如果安装MySQL，则使用包含MySQL配置的docker-compose-build-sql.yaml；
		否则，使用不包含MySQL配置的docker-compose-build-nosql.yaml。
		"""
		if self.install_mysql:
			self.src = "up/docker-compose-build-sql.yaml"
		else:
			self.src = "up/docker-compose-build-nosql.yaml"

		# 将源文件路径转换为绝对路径，确保文件路径的正确性
		self.src = os.path.abspath(self.src)

		# 检查源文件是否为文件且存在
		if os.path.isfile(self.src):
			try:
				# 使用copy2函数复制文件，以保留文件的元数据（如修改时间等）
				copy2(self.src, self.dst)
			except Exception as e:
				# 复制文件时发生异常，记录错误日志并退出程序
				logger.error(f"复制文件失败: {e}")
				sys.exit(1)
		else:
			# 源文件不存在，记录错误日志并退出程序
			logger.error(f"未找到 {self.src} 文件")
			sys.exit(1)
	def replace(self):
		"""
		执行配置信息的替换操作。

		本方法旨在替换文件中预定义的占位符，例如数据库主机、端口、名称、用户、密码，
		电子邮件用户和密码，以及后端URL。这些占位符被实际的配置信息所替换。
		"""
		# 替换数据库主机名
		self.replace_in_file(r"DbHost", self.db_host)
		# 替换数据库端口号
		self.replace_in_file(r"Port3306", str(self.db_port))
		# 替换数据库名称
		self.replace_in_file(r"DbNameThriveX", self.db_name)
		# 替换数据库用户名
		self.replace_in_file(r"DbUserThrive", self.db_user)
		# 替换数据库密码
		self.replace_in_file(r"DB_PASSWORD_ThriveX@123\?", self.db_password)
		# 替换电子邮件用户名
		self.replace_in_file(r"123456789@qq.com", self.email_user)
		# 替换电子邮件密码
		self.replace_in_file(r"123456789Password", self.email_password)
		# 替换后端URL
		self.replace_in_file(r"BackendUrl", f"http://{self.db_host}:3000")
		# 替换 api参数
		## baidu
		self.replace_in_file(r"VITE_BAIDU_TONGJI_SITE_ID_VALUE", self.VITE_BAIDU_TONGJI_SITE_ID)
		self.replace_in_file(r"VITE_BAIDU_TONGJI_ACCESS_TOKEN_VALUE", self.VITE_BAIDU_TONGJI_ACCESS_TOKEN)
		## 替换后端 api接口地址
		self.replace_in_file(r"VITE_PROJECT_API_VALUE", self.backend)
		self.replace_in_file(r"NEXT_PUBLIC_PROJECT_API_VALUE", self.backend)
		## gaode
		self.replace_in_file(r"NEXT_PUBLIC_GAODE_KEY_CODE_VALUE", self.NEXT_PUBLIC_GAODE_KEY_CODE)
		self.replace_in_file(r"NEXT_PUBLIC_GAODE_SECURITYJS_CODE_VALUE", self.NEXT_PUBLIC_GAODE_SECURITYJS_CODE)
		## ai
		self.replace_in_file(r"VITE_AI_APIPassword_VALUE", self.VITE_AI_APIPassword)
	def build(self):
		"""
		构建Thrive服务。

		本函数使用Docker Compose构建并启动Thrive服务。它通过调用`docker compose -p thrive up -d --build`命令来实现，
		该命令会构建镜像并以前台模式启动服务。如果构建过程中出现错误，会记录错误日志并退出程序。

		Raises:
			SystemExit: 如果构建失败或出现异常，程序将退出。
		"""
		if os.system("docker compose -p thrive up -d --build") != 0:
			logger.error("构建 Thrive 服务失败，请检查错误日志。")
			sys.exit(1)
		logger.info("Thrive 服务构建成功")
	def analysis(self):
		if not args.toml:
			return
		if not os.path.isfile(args.toml):
			logger.warning(f"文件不存在: {args.toml}")
			create_demo(args.toml)
			sys.exit(1)
		if not args.toml.endswith(".toml"):
			logger.warning(f"请输入正确的toml文件: {args.toml}")
			sys.exit(1)
		info = read_toml(args.toml)
		sec_list = ["mysql", "email", "server", "api", "baidu", "ai"]
		for sec in sec_list:
			if not info[sec]:
				logger.warning(f"找不到配置项，请检查配置文件: {sec}")
				sys.exit(1)
		try:
			self.db_host = info["mysql"]["host"]
			self.db_port = info["mysql"]["port"]
			self.db_user = info["mysql"]["user"]
			self.db_password = info["mysql"]["password"]
			self.db_name = info["mysql"]["name"]
			self.db_path = info["mysql"]["path"]
		except Exception as e:
			logger.warning(f"数据库配置参数不完整,错误: {e}")
			sys.exit(2)
		try:
			self.email_user = info["email"]["user"]
			self.email_password = info["email"]["password"]
			self.email_host = info["email"]["host"]
			self.email_port = info["email"]["port"]
		except Exception as e:
			logger.warning(f"邮件配置参数不完整,错误: {e}")
			sys.exit(2)
		try:
			self.backend = info["server"]["backend"]
		except Exception as e:
			logger.warning(f"后端[ server ]配置参数不完整,错误: {e}")
			sys.exit(2)
		# 获取api
		try:
			self.VITE_GAODE_WEB_API_KEY = info["api"]["VITE_GAODE_WEB_API_KEY"]
			self.NEXT_PUBLIC_GAODE_KEY_CODE = info["api"]["NEXT_PUBLIC_GAODE_KEY_CODE"]
			self.NEXT_PUBLIC_PROJECT_API = info["api"]["NEXT_PUBLIC_PROJECT_API"]
			self.NEXT_PUBLIC_GAODE_SECURITYJS_CODE = info["api"]["NEXT_PUBLIC_GAODE_SECURITYJS_CODE"]
		except Exception as e:
			logger.warning(f"[ api ]配置参数不完整,错误: {e}")
			sys.exit(2)
		# 获取baidu
		try:
			self.VITE_BAIDU_TONGJI_SITE_ID = info["baidu"]["VITE_BAIDU_TONGJI_SITE_ID"]
			self.VITE_BAIDU_TONGJI_ACCESS_TOKEN = info["baidu"]["VITE_BAIDU_TONGJI_ACCESS_TOKEN"]
		except Exception as e:
			logger.warning(f"[ baidu ]配置参数不完整,错误: {e}")
			sys.exit(2)
		# 获取ai
		try:
			self.VITE_AI_APIPassword = info["ai"]["VITE_AI_APIPassword"]
		except Exception as e:
			logger.warning(f"[ ai ]配置参数不完整,错误: {e}")
			sys.exit(2)

	def check_args(self):
		"""
		检查数据库配置和邮箱设置等参数的合法性
		"""
		# 将数据库端口转换为整数，如果转换失败则记录错误并退出程序
		try:
			mysql_port_ = int(self.db_port)
		except ValueError:
			logger.error("数据库端口号非法，请输入1-65535之间的数字")
			sys.exit(1)
		# 检查数据库端口是否在有效范围内
		if mysql_port_ < 1 or mysql_port_ > 65535:
			logger.error("数据库端口号非法，请输入1-65535之间的数字")
			sys.exit(1)
		## 检查用户名是否合法
		if not re.match(r'^[a-zA-Z0-9_-]{1,16}$', self.db_user):
			logger.error("数据库用户名非法，请输入1-16位字母、数字、下划线或减号")
			sys.exit(1)
		## 检查密码长度是否合法
		if len(self.db_password) < 8 or len(self.db_password) > 16:
			logger.error("数据库密码长度非法，请输入8-16位字符")
			sys.exit(1)
		## 检查数据库主机格式是否是标准IP或者标准域名
		if not re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$', self.db_host):
			if not re.match(
					r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$',
					self.db_host):
				logger.error("数据库主机格式非法，请输入标准IP或者标准域名")
				sys.exit(1)
		## 检查邮箱格式
		if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', self.email_user):
			logger.error("邮箱地址非法，请输入正确的邮箱地址")
			sys.exit(1)
		## 检查邮箱密码长度是否合法
		if len(self.email_password) < 8 or len(self.email_password) > 16:
			logger.error("邮箱密码长度非法，请输入8-16位字符")
			sys.exit(1)
		## 检查后端URL是否合法,确保 http开头且以/api结尾
		if not re.match(r'^http[s]?://(?:[a-zA-Z0-9$-_@.&+!*(),]|%[0-9a-fA-F]{2})+',
						self.backend) or not self.backend.endswith('/api'):
			logger.debug(self.backend)
			logger.error("后端URL格式非法，请输入正确的URL: http开头且以/api结尾")
			sys.exit(1)
	def path_check(self):
		blog = os.path.join(pwd, "program/blog/Dockerfile")
		if not os.path.isfile(blog):
			logger.error(f"文件不存在: {blog}")
			sys.exit(1)
		admin = os.path.join(pwd, "program/admin/Dockerfile")
		if not os.path.isfile(admin):
			logger.error(f"文件不存在: {admin}")
			sys.exit(1)

	def start(self):
		"""
		启动程序，执行一系列初始化和配置步骤。
		本函数按顺序执行多个步骤，包括获取Docker状态、复制文件或目录、获取用户输入、
		显示信息、设置环境变量、替换特定内容，最后进行构建。
		"""
		self.path_check() # 检查文件是否存在
		self.analysis()  # 解析配置文件
		self.get_docker_status()  # 获取Docker状态，确保Docker环境正常运行
		self.copy()  # 复制必要的文件或目录，准备环境
		self.get_user_input()  # 获取用户输入，可能用于配置或后续操作
		self.check_args() # 检查参数合法性，确保输入的参数符合要求
		self.show()  # 显示相关信息，可能是环境信息或用户输入的确认信息
		self.set_env()  # 设置环境变量，根据用户输入或其他逻辑配置环境
		self.replace()  # 替换特定内容，可能是文件中的占位符或配置项
		self.build()  # 执行构建操作，可能是编译代码或构建镜像等
		os.system("docker ps -a")



def pull():
	"""
	根据不同的环境（开发或生产），拉取相应的Docker镜像版本。

	本函数不接受参数，但依赖于全局变量args，其中args.dev指示是否为开发环境。
	在开发环境下，拉取dev版本的镜像；在生产环境下，则拉取latest版本的镜像。
	"""
	if args.dev:
		# 在开发环境下，拉取以下服务的dev版本镜像：mysql, nginx, server, admin, blog
		for i in ["mysql", "nginx", "server", "admin", "blog"]:
			os.system(f"docker pull registry.cn-hangzhou.aliyuncs.com/thrive/{i}:dev")
	else:
		# 在非开发环境下，拉取以下服务的latest版本镜像：mysql, nginx, server, admin, blog
		for i in ["mysql", "nginx", "server", "admin", "blog"]:
			os.system(f"docker pull registry.cn-hangzhou.aliyuncs.com/thrive/{i}:latest")
	exit(0)
def clean():
	"""
	清理Docker容器和镜像，并删除相关文件。
	该函数会删除Docker容器和镜像，并删除相关文件。
	"""
	cmd = "docker rmi -f `docker images | awk '{print $2,$3}'|grep none | awk '{print $2}'`"
	os.system(cmd)
	sys.exit(0)





if __name__ == "__main__":
	arg = ArgumentParser(description='当前脚本版本: 1.0', prog="ThriveXInstall")
	h = f"指定数据库映射路径,默认: {mysql_path}l"
	arg.add_argument('-d', '--dir', type=str, help=h, default=mysql_path, required=False)
	# 数据库信息
	arg.add_argument('-p', '--port', type=int, help="指定数据库端口,默认: 3306", default=3306, required=False)
	arg.add_argument('-u', '--user', type=str, help="指定数据库用户名,默认: ThriveX", default="ThriveX", required=False)
	arg.add_argument('-P', '--password', type=str, help="指定数据库密码,默认: ThriveX@123?", default="ThriveX@123?", required=False)
	arg.add_argument('-H', '--host', type=str, help="指定数据库地址,默认: 10.178.178.10", default="10.178.178.10", required=False)
	# 中间件信息
	arg.add_argument('-n', '--nginx', type=str, help="[临时弃用]指定nginx端口,默认: 9007", default=9007, required=False)
	# 设置邮箱信息
	arg.add_argument('-e', '--email', default=None, help='邮箱地址', dest='email')
	arg.add_argument('-ep', '--email_password', default=None, help='邮箱密码', dest='email_password')
	# 设置后端URL
	arg.add_argument('-b', '--backend', type=str, help="指定后端URL,必须 /api结尾且外部浏览器可以访问", required=False, default=None)
	# 功能选项
	arg.add_argument('-t', '--toml', type=str, help="指定安装信息配置文件路径,当使用此选项时,将忽略其他选项, 例如: -t install.toml", required=False, default=None)
	arg.add_argument('-s', '--sql', action='store_true', help="安装sql数据库", default=False, required=False)
	arg.add_argument('-g', '--gitee', action='store_true', help="使用gitee下载docker-compose文件", default=False, required=False)
	# arg.add_argument('-build', '--build', action='store_true', help="自行构建镜像", default=False, required=False)
	arg.add_argument('-dev', '--dev', action='store_true', help="使用开发版镜像运行", default=False, required=False)
	arg.add_argument('-update', '--update', action='store_true', help="更新对应版本镜像", default=False, required=False)
	arg.add_argument('-c', '--clean', action='store_true', help="清除none标签的镜像", default=False, required=False)
	args = arg.parse_args()
	if args.gitee:
		url_compose_root = "https://gitee.com/liumou_site/ThriveX/raw/main"
	mysql_port=args.port
	mysql_user=args.user
	mysql_password=args.password
	mysql_host=args.host
	nginx_port=args.nginx
	mysql_path=args.dir
	# email
	email_user = args.email
	email_password = args.email_password
	# 后端URL
	BackendUrl = args.backend
	if args.clean:
		clean()
	if args.update:
		pull()
	# if args.build:
	build = BuildInstall()
	build.db_port = mysql_port
	build.user = mysql_user
	build.db_password = mysql_password
	build.db_host = mysql_host
	build.email_user = args.email
	build.email_password = args.email_password
	build.backend = args.backend
	build.install_mysql = args.sql
	build.start()
