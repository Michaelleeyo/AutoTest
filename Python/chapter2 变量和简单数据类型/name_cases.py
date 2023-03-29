'''
字符串处理：
字母小写 a.lower() a.islower() 
字母大写 a.upper() A.isupper()
首字母大写 a.title() a.istitle()
只包含字母，且非空 a.isalpha()
只包含字母和数字，且非空 a.isalnum()
只包含数字，非空 a.isdecimal()
只包含空格，制表符，换行符，非空 isspace()
字符串以xx开始，结束 startswith()、endswith()

join()方法在一个字符串上调用， 参数是一个字符串列表， 返回一个字符串
','.join('a','b')

split() 分割字符串
split('m') 字母m前后分割

rjust()和 ljust()字符串方法返回调用它们的字符串的填充版本， 通过插入空格来
对齐文本。 这两个方法的第一个参数是一个整数长度， 用于对齐字符串。
a.rjust(20) a.rjust(20,'*')  a.ljust(10) a.ljust(10,'-')
a.center(10) a.center(10,'=')

删除空格 a.strip()
删除左侧空格 a.lstrip()
删除右侧空格 a.rstrip()
换行符 \n
制表符 \t
倒斜杠 \\
输出原始字符串r print(r'that's good')

pyperclip模块 copy() paste()
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


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
