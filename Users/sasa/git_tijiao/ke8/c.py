import requests
import re

s=requests.session()
print(s.cookies)

url="http://49.235.92.12:9000/admin/login/?next=/admin/"

r=s.get(url)#第一次请求登录页
print(s.cookies)
#print(r.text)

#name='csrfmiddlewaretoken' value='(.+?)'
csrfmiddlewaretoken=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
#print(csrfmiddlewaretoken[0])

body={
    "csrfmiddlewaretoken":csrfmiddlewaretoken[0],
    "username":"admin",
    "password":"yoyo123456",
    "next":"/admin/"
}
r1=s.post(url,data=body)
#print(r1.text)
assert "Site administration | Django site admin" in r1.text
print(s.cookies)
