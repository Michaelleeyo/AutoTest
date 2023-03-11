'''
字母小写 a.lower()
字母大写 a.upper()
首字母大写 a.title()
删除空格 a.strip()
删除左侧空格 a.lstrip()
删除右侧空格 a.rstrip()
换行符 \n
制表符 \t
'''

# 个性化消息，用户名存到变量，并向该用户显示一条信息。
name = "Eric"
print("Hello"+name+",would you like to learn some Python today")
# 将一个人名存储到变量中，以小写、大写和首字母显示
print(name.lower())
print(name.upper())
print(name.title())
# 名言
print(name+"once said,'Hello World!'")
# 名言2
famous_person = name
message = "Good Job"
print(famous_person+message)
# 剔除人名中的空白
myName = " zhang san "
print("zhang\tsan")
print("zhang san\n")
print(myName.lstrip())
print(myName.rstrip())
print(myName.strip())
