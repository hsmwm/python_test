#一般在POST请求中,一般参数都在请求体中（request body）进行传递
import requests
base_url="http://httpbin.org"
param_data={'user':'wang','password':'123'}
r=requests.post(base_url+'/post')
print(r.status_code)
print(r.url)
#打印返回文本信息
print(r.text)