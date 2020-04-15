import requests
base_url="https://www.zhihu.com"
param_data={'name':'hsmwm@163.com','password':'haoshimeng1234'}
header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
r=requests.get(base_url+'/signin',data=param_data,headers=header)
print(r.status_code)
print(r.url)
#打印返回文本信息
print(r.text)


