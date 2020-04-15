#应用场景：简化代码
#特点：参数可有可无 返回值有一个
#语法lambda 参数列表：表达式（返回值）  匿名函数
# # fn2=lambda :100
# print(fn2)#打印的是lambda的内存地址
# #100返回值需要调用
# print(fn2())

#lambda参数形式
#1，无参数
fn1=lambda :100
print(fn1())
#2，有参数
fn2 = lambda a:a
print(fn2('hello '))

#3，默认参数 如果前边默认值则后边参数也需要默认值 不传使用默认值 传新的数据使用新数据
fn3=lambda a,b=10,c=100:a+b+c
print(fn3(20))
#4，可变参数*args
#5，可变参数*kwargs
#lambda 两个数字比大小 谁大返回谁
fn4=lambda a,b:a if a>b else b
print(fn4(1000,500))
#列表数据按字典key的值排序
students=[{'name':'tom','age':'18'},{'name':'atom2','age':'20'}]
#按照name值升序排列
students.sort(key=lambda x:x['name'])
print(students)

#按name值降序排列
students.sort(key=lambda x:x['name'],reverse=True)
print(students)

students.sort(key=lambda x:x['age'],reverse=True)
print(students)
d = {"zhang":"China", "Jone":"America", "Natan":"Japan"}

for k in d:

    print(k)