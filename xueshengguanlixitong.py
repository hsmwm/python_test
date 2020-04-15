#定义功能界面函数
def info_print():
    print("请选择功能--------")
    print("1，添加")
    print("2，删除")
    print("3，修改")
    print("4，查询")
    print("5，显示所有学员")
    print("6，退出")
    print("-" * 20)
#存储所有学院信息
info =[]
#添加学员信息的函数
def add_info():
    """添加学员信息"""
    #1，用户输入学号，姓名，手机号
    new_id=input('输入学号:')
    new_name=input('输入姓名:')
    new_tel=input('输入手机号:')
    #2.1判断是否能添加学员；如果姓名存在报错提示
    global info
    #判断用户输入到姓名，如果和列表中字典name对应到值相等，则重复
    for i in info :
        if new_name== i['name']:
            print('该姓名已经存在!')
            return #没有返回值则退出当前函数

    #2.2如果学员姓名不存在添加到空字典中
    info_dict={}
    #字典新增数据
    info_dict['id']=new_id
    info_dict['name']=new_name
    info_dict['tel']=new_tel
    print(info_dict)
    #列表追加字典
    info.append(info_dict)

#删除学员函数
def del_info():
    '''删除学员'''
    #1，用户输入要删除到学员的姓名
    del_name=input('请输入删除学员姓名：')
    global info
    #2，判断学员是否存在：如果输入姓名存在则删除否则报错提示
    for i in info:
        if del_name == i['name']:
            #列表删除数据， remove
            info.remove(i)
            print('删除成功!')
            break
    else:
        print('该学员不存在!')

#修改学员信息函数
def modify_name():
    '''修改学员手机号'''
#输入用户姓名
    modify_name=input('请输入要修改的学员姓名:')
    global info

#检查用户是否存在
    for i in info:
        # 存在用户修改手机号
        if modify_name==i['name']:
            i['tel']=input('请输入新的手机号码：')
            break
    else:#如果不存在则报错
        print('要修改的用户不存在!')
    print(info)
#根据姓名查询学员信息
def search_info():
    '''查询学员'''
    #输入学员姓名
    search_name=input('请输入查询学生name!')
    global info
    for i in info:
        #存在显示
        if search_name==i['name']:
            print('以下内容是您要查询的学员信息--')
            print(f"学员姓名为{i['name']},id是{i['id']},tel是{i['tel']}")
            break
    else:#表示循环正常结束后
        #不存在报错
        print('查无此人!')
    print(info)
def all_info() :
    '''显示所有学员信息'''
    print('学号\t姓名\t手机号')#打印提示字
    for i in info:
        #\t美观
        print(f"学员姓名为{i['name']}\tid是{i['id']}\ttel是{i['tel']}")

#退出系统

#系统功能需要循环使用直到用户输入6才退出循环
while True:
    #1显示功能界面
    info_print()
    #2用户输入功能序号
    user_num= int(input('请输入功能序号'))
    #3按照用户输入序号执行不同功能。1
    #如果用户输入1，执行添加，如果是2怎删除
    if user_num==1:
        add_info()
    elif user_num==2:
        del_info()
    elif user_num==3:
        modify_name()
    elif user_num==4:
        search_info()
    elif user_num==5:
        all_info()
    elif user_num==6:
        #程序想结束，退出while true就可以 break即可
        tike=input('确定要退吗 yes or no')
        if tike=='yes':
            break
    else:
        print('输入的功能序号有误')