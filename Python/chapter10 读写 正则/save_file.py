'''
处理 json.load()读取空文件报JSONDecodeError: Expecting value: line 1 column 1 (char 0)
可以在读取之前，先判断文件是否为空，if os.path.getsize(file_path) == 0
'''
import os
import json

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'favorite_number.json')

# 练习：喜欢的数字
# 存储用户名和他喜欢的数字，后续再次输出名字，能打出他喜欢的数字，否则录入信息
'''输入数字'''

# 空文件，首次写


def user_number():
    your_name = input('Enter your name:')
    favorite_number = input('Enter your favorite number:')
    saved_numbers = {}
    saved_numbers[your_name] = favorite_number
    with open(file_path, 'w') as numbers:
        json.dump(saved_numbers, numbers)
    return saved_numbers

# 非空文件，添加


def add_user_number():
    your_name = input('Enter your name:')
    favorite_number = input('Enter your favorite number:')
    with open(file_path, 'r') as to_add_number:
        to_add_numbers = json.load(to_add_number)
        to_add_numbers[your_name] = favorite_number
    with open(file_path, 'w') as added_number:
        json.dump(to_add_numbers, added_number)

# 打印数字，判断为空执行user_number()，非空存在打印喜欢数字，非空不存在录入信息


def print_number():
    if os.path.getsize(file_path) == 0:
        user_number()
        print('Come back later')
    else:
        with open(file_path, 'r') as read_numbers:
            read_number = json.load(read_numbers)
            insert_name = input('Enter your name:')
            if insert_name in read_number.keys():
                print(insert_name+',I know your favorite number is ' +
                      read_number[insert_name])
            else:
                print('You are not in the list ,input your info')
                add_user_number()
                print('come back soon')


print_number()
