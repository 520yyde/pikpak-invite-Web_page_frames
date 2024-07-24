import requests
import time
import json

def main(key, code):
    url = 'http://47.109.38.135:44335/invite'
    data = {
        "key": key,
        "code": code
    }
    headers = {
        'Content-Type': 'application/json'
    }
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, headers=headers)
    print(f'邀请结果：{response.json()}')


if __name__ == "__main__":
    print("不要擅自改动脚本，不可并发!!!")
    print("卡密购买地址：http://47.109.38.135/")
    key = input("请输入你的卡密：")
    code = input("请输入你的邀请码：")
    print("邀请中，请耐心等待，大概半分钟")
    start_time = time.time()
    main(key, code)
    end_time = time.time()
    print(f'运行时间{end_time - start_time}')
