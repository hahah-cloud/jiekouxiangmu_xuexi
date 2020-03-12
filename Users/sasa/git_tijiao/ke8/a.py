import json
import requests
#会话
s=requests.session()
#print(s.headers)
#print(s.cookies)
#1、登录
url1="http://49.235.92.12:9000/api/v1/login"
body={
    "username":"test",
    "password":"123456"
}
r=s.post(url1,body)
#print(r.json())
token=r.json()["token"]
print("取出来的token %s" %s ,token)
h={
    "Authorization":"Token %s" %token
}
print(h)
s.headers.update(h)
print(s.headers)

#2、获取个人信息
url2="http://49.235.92.12:9000/api/v1/userinfo"
r2=s.get(url2)
print(r2.text)

#3、修改个人信息
url3="http://49.235.92.12:9000/api/v1/userinfo"
body={
    "name":"test",
    "sex":"M",
    "age":20,
    "mail":"283340479@qq.com"
}
r3=s.post(url3,json=body)
print(r3.json())



