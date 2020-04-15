#请求头的定制；如果想为请求添加HTTP头部，只需要简单传递一个dict给headers参数就可以
#避免被封，需要定制请求头
import requests
base_url="http://httpbin.org"
param_data={'user':'wang','password':'123'}
header={'User-Agent':'Mozilla/5.0'}
r=requests.post(base_url+'/post',data=param_data,headers=header)
print(r.status_code)
print(r.url)
#打印返回文本信息
print(r.text)