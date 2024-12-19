import json
import os
import uuid
import subprocess
from enum import Enum

class TYPE(Enum):
    ADD = 1  # 添加隧道
    DEL = 2  # 删除隧道
    LIST = 3  # 查看隧道列表
    START = 4  # 启动

# 全局变量
myuuid = str(uuid.uuid4())
appn = 0

# 生成初始配置
def sconfig(myuuid):
    config = {
        "LogLevel": 1,
        "network": {
            "TCPPort": 50448,
            "UDPPort2": 27183,
            "UDPPort1": 27182,
            "ServerPort": 27183,
            "ServerHost": "api.openp2p.cn",
            "ShareBandwidth": 10,
            "User": "gldoffice",
            "Node": myuuid,
            "Token": 11602319472897248650
        },
        "apps": []
    }
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

# 添加隧道
def add_tunnel():
    global appn
    protocol = input("请输入隧道类型（tcp/udp）：")
    peer_node = input("请输入对方UUID：")
    dst_port = int(input("请输入对方端口："))
    src_port = int(input("请输入本地接收端口："))

    if protocol not in ['tcp', 'udp']:
        print("错误的指令")
        return

    config = load_config()
    config['apps'].append({
        "AppName": "***",
        "Protocol": protocol,
        "SrcPort": src_port,
        "PeerNode": peer_node,
        "DstPort": dst_port,
        "DstHost": "localhost",
        "PeerUser": "",
        "Enabled": 1
    })
    appn += 1
    save_config(config)
    print("新建隧道成功")

# 删除隧道
def clear_tunnel():
    n = int(input("请输入要删除的隧道序号：")) - 1
    config = load_config()
    if n < len(config['apps']):
        del config['apps'][n]
        save_config(config)
        print("删除隧道成功")
    else:
        print("隧道序号错误")

# 加载配置
def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 保存配置
def save_config(config):
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

# 显示隧道列表
def list_tunnels():
    config = load_config()
    if config['apps']:
        for i, app in enumerate(config['apps']):
            print(f"*******隧道序号：{i+1}*******")
            print(f"类型: {app['Protocol']}")
            print(f"对方uuid: {app['PeerNode']}")
            print(f"对方端口: {app['DstPort']}")
            print(f"本地端口: {app['SrcPort']}")
            print("***************************")
    else:
        print("无隧道")

# 启动程序
def start():
    print(f"注意你的uuid是：{myuuid}")
    subprocess.run(['./bin/openp2p.exe'])

# 主函数
def main():
    print("*初始化完毕*")
    print("Openp2pLauncher 0.6.2")
    print("-被连接需要把你的uuid和端口发给对方")
    print("-本程序基于openp2p")
    print("*********************************************")
    sconfig(myuuid)

    while True:
        print("\n\033[34;1m******指令语法******\033[0m\n")
        print("添加隧道：add <tcp/udp> <uuid> <对方端口> <本地接收端口>")
        print("删除隧道：del <序号>")
        print("隧道列表：list")
        print("开始运行隧道/程序：start")
        print("*******************\033[0m")

        types = input()
        print(types)

        if types.startswith('add'):
            add_tunnel()
        elif types.startswith('del'):
            clear_tunnel()
        elif types == 'list':
            list_tunnels()
        elif types == 'start':
            start()
        else:
            print("错误的指令")

if __name__ == "__main__":
    main()