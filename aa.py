#command+/ 选中注释
# def testA(a,b):
#     print(a+b)
# if __name__=='__main__':
#     testA(1,2)

# __all__=['testA']
# def testA():
#     print('A')
# def testB():
#     print('B' )


# #导入mypackage包下的模块1，使用这个模块下的info_print1
# #导入
# import mypackage.my_module
# #调用
# mypackage.my_module.info_print1()

from mypackage import *
my_module2.info_print2()
