import requests
import random
import string
def generate_random_string(length):
    # 生成随机字符串
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))
# 注册账号
def register_openp2p():
    # 访问注册页面
    register_url = 'https://console.openp2p.cn/register'
    # payload = {'username': 'userName', 'password': 'passWord', 'confirmPassword':'confirmPassword','phone': 'phoneNumber','email': 'emailNumber'}
    
    payload = {
        'username': generate_random_string(10),  # 生成10个字符的随机用户名
        'password': generate_random_string(10),  # 生成10个字符的随机密码
        'confirmPassword': generate_random_string(10),  # 确认密码
        'phone': '1' + generate_random_string(10),  # 生成11位随机电话号码
        'email': generate_random_string(10) + '@coolge.com'  # 生成随机电子邮箱
    }
    
    response = requests.post(register_url, data=payload)
    
     # 检查响应状态码
    if response.status_code == 200:
        print("注册请求已发送，等待服务器响应。")
    else:
        print(f"注册请求失败，状态码：{response.status_code}")


# 调用函数
register_openp2p()
