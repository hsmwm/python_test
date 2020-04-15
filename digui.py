#递归是编程思想
#应用场景：1，要便利一个文件夹下所有文件 2，算法课程
#递归特点：1，函数内部自己调用自己2，必须有出口
#回顾函数返回值，注意写法和返回位置:函数调用的位置
def return_num():
    return 100
#函数调用时可以
#result=return_num()
#print(result)

#应用3以内的累加和3+2+1
def sum_numbers(num):
    #2,出口
    if num==1:
        return 1
    #1,当前数据+当前数字-1的累加和
    return num+sum_numbers(num-1)
result=sum_numbers(3)
print(result)
#如果没有出口则报错，超出最大递归深度