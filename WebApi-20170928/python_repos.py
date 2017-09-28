# -*- coding:utf8 -*-
import requests

# 执行API调用并存储响应
#url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#url = 'https://api.github.com/'
url = 'https://cdn.jin10.com/assets/js/index.js?20170928'
r = requests.get(url)
print("Status code:", r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
# 处理结果
print(response_dict.keys())