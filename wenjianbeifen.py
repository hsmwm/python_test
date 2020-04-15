old_name=input("请输入要备份文件地址：")
#获取点的下标
index=old_name.rfind('.')
#点的下标需要大于0
if index>0:
        postfix=old_name[index:]
#组织备份后的新名字-切片
new_name=old_name[:index]+'[备份]'+postfix
old_f=open(old_name,'rb')
new_f=open(new_name,'wb')
while True:
    con=old_f.read(1024)
    if len(con==0):
        break
    new_f.write(con)
old_f.close()
new_f.close()