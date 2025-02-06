# 将 up文件夹下的所有文件进行文本替换
import os

from loguru import logger


class Res:
    def __init__(self):
        self.res_path = os.path.join(os.getcwd(), 'up')
    def get_file_list(self):
        file_list = []
        for root, dirs, files in os.walk(self.res_path):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    def start(self):
        file_list = self.get_file_list()
        for file in file_list:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                # content = content.replace("thrive.cc", "thrive.site")
                content = content.replace("thrive_server", "server.thrive.site")
                content = content.replace("container_name: server.thrive.site", "container_name: thrive_server")
                content = content.replace("hostname: thrive_nginx", "hostname: nginx.thrive.site")
                f.close()
                try:
                    os.remove(file)
                except Exception as e:
                    logger.error(e)
                # 写入
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                    f.close()
                    logger.info(f"{file} 替换成功")

if __name__ == '__main__':
    res = Res()
    res.start()