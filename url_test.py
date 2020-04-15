#一般在GET请求中使用查询字符串来进行参数的传递
import requests
base_url="http://httpbin.org"
param_data={'user':'wang','password':'123'}
r=requests.get(base_url+'/get')
print(r.status_code)
print(r.url)