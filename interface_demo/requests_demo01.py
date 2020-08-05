# coding=utf-8

import requests
import json

# url = 'http://httpbin.org/get'
#
# # 传递url参数
# params = {'name': 'Numb', 'author': 'Linkin Park'}
# # params 支持列表作为值
# # params = {'name': 'Good Time', 'author': ['Owl City', 'Carly Rae Jepsen']}
#
# # 请求头
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
#     # 还可以设置其他字段。
# }
#
# response = requests.get(url, params=params, headers=headers)
# print(response.url)
# print(response.text)

# # data 参数通常结合 POST 请求方式一起使用。如果我们需要用 POST 方式提交表单数据或者JSON数据，我们只需要传递一个字典给 data 参数。
# url = 'http://httpbin.org/post'
#
# data = {
#     'user': 'admin',
#     'pass': 'admin'
# }
#
# response = requests.post(url, data=data)
# print(response.text)

# # 提交json数据,在HTTP 请求中，JSON 数据是被当作字符串文本。所以，我们使用 data 参数的传递 JSON 数据时，需要将其转为为字符串。
#
# url = 'http://httpbin.org/post'
# data = {
#     'user': 'admin',
#     'pass': 'admin'
# }
# # response = requests.post(url, data=json.dumps(data))
# response = requests.post(url, json=data)
# print(response.text)

# # 使用cookie
# url = 'http://httpbin.org/cookies'
# # cookies = dict(domain='httpbin.org')
# cookies = {
#     'domain':'httpbin.org',
# }
# response = requests.get(url, cookies=cookies)
# print(response.text)

# 使用session

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'