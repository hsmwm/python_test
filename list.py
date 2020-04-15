# #从'don't panic!'中获取'on tap'
# phrase="don't panic!"
# plist=list(phrase)#转换成list
# for i in range(4):#连续删除四次最后的单词
#     plist.pop()
# #print(plist)#don't pa
# plist.pop(0)#删除第一位 on't pa
# plist.remove("'")#ont pa
# plist.extend(([plist.pop(),plist.pop()]))#追加两个先a再p 做到交换pa
# #print(plist)
# plist.insert(2,plist.pop(3))#再索引2的前边插入3
# new_phrase=''.join(plist)#转换成字符串
# print(plist)#打印老的列表
# print(new_phrase)#打印新的字符串


# #从'don't panic!'中获取'on tap'
phrase="don't panic!"
plist=list(phrase)#转换成list
for i in range(4):#连续删除四次最后的单词
    plist.pop()
#print(plist)#don't pa
plist.pop(0)#删除第一位 on't pa
plist.remove("'")#ont pa
plist.extend(([plist.pop(),plist.pop()]))#追加两个先a再p 做到交换pa
#print(plist)
#plist.insert(2,plist.pop(3))#再索引2的前边插入3
plist.remove(' ')
plist.insert(2,' ')
new_phrase=''.join(plist)#转换成字符串
print(plist)#打印老的列表
print(new_phrase)#打印新的字符串