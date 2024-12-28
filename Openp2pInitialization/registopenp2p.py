import requests

# 定义注册账号和获取token的函数
def register_openp2p():
    # 访问注册页面
    register_url = 'https://console.openp2p.cn/register'
    response = requests.get(register_url)
    
    # 如果需要，可以在这里添加表单数据进行POST请求，模拟注册过程
    # 例如：
    payload = {'username': 'userName', 'password': 'passWord', 'confirmPassword':'confirmPassword','phone': 'phoneNumber','email': 'emailNumber'}
    response = requests.post(register_url, data=payload)
    
    # 检查是否注册成功，并获取token
    if response.status_code == 200:
        # 这里需要根据实际页面结构进行调整，以下仅为示例
        token_url = 'https://console.openp2p.cn/your/token/path'
        token_response = requests.get(token_url)
        if token_response.status_code == 200:
            token = token_response.json().get('token')
            return token
        else:
            print("获取Token失败。")
    else:
        print("注册失败。")

# 调用函数
token = register_openp2p()
if token:
    print(f"注册成功，获取的Token为：{token}")
else:
    print("注册或获取Token失败。")