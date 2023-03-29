# 练习：存储人信息并打印
zhangsan = {
    'name': 'zhangsan',
    'age': 23,
    'city': 'London'
}
print(zhangsan['name']+str(zhangsan['age'])+zhangsan['city'])


# 练习：喜欢的数字
name = input('Please insert a name :')
number = {'zhao': 1,
          'qian': 2,
          'sun': 3}
if name == 'zhao':
    print('My favorite number is '+str(number['zhao']))
elif name == 'qian':
    print('My favorite number is '+str(number['qian']))
else:
    print('My favorite number is '+str(number['sun']))

# 词汇表
language = {
    'python': '.py',
    'Java': '.java'
}
print('python文件后缀名'+language['python']+'\n')
print('java文件的后缀名'+language['Java'])
