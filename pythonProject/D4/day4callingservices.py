import requests
import json

# url = "http://jsonplaceholder.typicode.com/posts?userId=4"
# res = requests.get(url)
# print(res.status_code)
# print(res.content.decode("utf-8"))
# content = res.content.decode("utf-8")
#
# print(type(content))
#
# jsoncontent = json.loads(content)
# print(type(jsoncontent))
#
# for post in jsoncontent:
#     print(post["title"])
# #section 48/ could use 47/49 so as more work
url = "http://jsonplaceholder.typicode.com/posts?userId=5"
ret = requests.get(url)
print(ret.status_code)
d = json.loads(ret.content.decode("utf-8"))
print(d)
print(ret.headers)

for post in d:
    print(post["title"])


#print(d["userId"])
#print(d["id"])
#print(d["title"])

# could use to show all currencies/stocks
#url, res, print, content,
#print(jsoncontent["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

