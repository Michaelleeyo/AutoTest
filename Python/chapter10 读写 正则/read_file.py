'''
注意readline()和readlines()，前者只会读文件第一行，后者读全部,且读取的结果为每行形成的列表
os.path.abspath(path) 将返回参数的绝对路径的字符串
os.path.isabs(path) 绝对路径返回True，相对路径返回False
os.path.relpath(path,start) 返回从start路径到path的相对路径的字符串，
如果没有start，就是用当前工作目录作为开始路径
os.path.dirname(path) 返回一个字符串，包含Path参数最后一个斜杠前的内容
os.path.basename(path) 返回一个字符串，包含Path参数最后一个斜杠后的内容
os.path.split() 获得这两个字符串的元组
PATH.split(os.path.sep) os.path.sep变量设置为正确的文件夹分割斜杠
os.path.getsize(path) 将返回Path文件的字节数
os.listdir(path) 将返回文件名字符串的列表，包含path参数中的每个文件(注：os)
os.getcwd() 方法用于返回当前工作目录
os.chdir() 方法用于改变当前工作目录到指定的路径
检查路径有效性：
os.path.exists(path),os.path.isfile(path),os.path.isdir(path)
'''
# 练习：Python学习笔记
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "learning_python.txt")
# 读取整个文件
with open(file_path, "r") as result_1:
    data_1 = result_1.read()
    print(data_1.rstrip())
print('====================')
# 逐行读取文件
with open(file_path, "r") as result_2:
    for line in result_2:
        print(line.rstrip())
print('===========================')
# 逐行存入列表
with open(file_path, 'r') as result_3:
    data_2 = result_3.readlines()
# print(data_2)
result_string = []
for line in data_2:
    result_string.append(line.rstrip())
print(result_string)
print('==========================')


# 练习：替换文件
data_3 = data_1.replace('Python', 'Java')
print(data_3.rstrip())
