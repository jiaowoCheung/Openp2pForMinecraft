import requests
import os
from subprocess import call

# openp2p.exe的下载地址
download_url = 'https://openp2p.cn/download/v1/latest/openp2p64-api.openp2p.cn-18227865175438169964-setup.exe'

# 定义下载文件的函数
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        return True
    return False

# 定义安装openp2p的函数
def install_openp2p():
    # 指定下载的文件名
    filename = 'openp2p.exe'
    
    # 下载文件
    if download_file(download_url, filename):
        print(f"{filename} 下载成功。")
        
        # 切换到文件所在的目录
        os.chdir(os.path.dirname(os.path.abspath(filename)))
        
        # 运行安装命令
        call(f'./{filename} install -node YOUR_NODE_NAME -token YOUR_TOKEN', shell=True)
        print("openp2p安装完成。")
    else:
        print(f"{filename} 下载失败。")

# 调用安装函数
install_openp2p()