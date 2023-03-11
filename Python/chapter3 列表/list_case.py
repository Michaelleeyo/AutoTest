'''
一、添加元素的良种方法
1.append
list.append('a') 在末尾加
2.insert
list.insert(0,'a') 再指定位置加
二、移除删除列表中元素有三种方法
1.不需要使用元素
del list[0]
2.需要使用元素的时候可以用pop弹出
list.pop() 弹出最后一个值
list.pop(1) 弹出定义位置的值
3.remove只会删除找到的第一个，全部删除需要循环
list.remove('a')
'''

# 姓名存储列表，依次打印出来
name = ['zhangsan', 'lisi', 'wangwu']
print(name[0], name[1], name[-1])
# 每人说问候语
word = 'nihao'
print(name[0]+'\tsays\t'+word)
print(name[1]+'\tsays\t'+word)
print(name[-1]+'\tsays\t'+word)
# 每人说通勤方式
tongqin = ['motorcycle', 'bike', 'bus', 'car']
print("I would like to own a "+tongqin[0])
# 修改嘉宾名单
wufafuyue = name.pop(1)
print(wufafuyue+" can't arrive")
name.append('zhaoliu')
print(name)
# 添加嘉宾
print("---bigger table---")
name.insert(0, 'lihua')
name.insert(1, 'xiaoming')
name.append('zhaomeng')
print(name)
# 缩减名单
print("---less inviters---")
name.pop(0)
name.pop(1)
print(name)
