#requests库内置了不同的方法来发送不同类型的http请求
import requests
base_url='http://httpbin.org'
#发送GET请求，用户获取信息，不影响服务器中的数据
r=requests.get(base_url + '/get')
print(r.status_code)
#发送POST请求，可能会修改服务器上的资源的请求
r=requests.post(base_url + '/post')
print(r.status_code)
'''
状态码   2**正确  
        3**域名地址变了
        4** 客户端权限问题
        5** 服务器宕机，服务关闭
'''
