
# 练习：加法运算
import os


def plus():
    while True:
        try:
            number_1 = input('Enter first number(q to exit):\n')
            if number_1 == 'q':
                break
            number_2 = input('Enter second number(q to exit):\n')
            if number_2 == 'q':
                break
            print(int(number_1)+int(number_2))
        except ValueError:
            print('please enter a int number')


# 练习：猫和狗
current_dir = os.path.dirname(__file__)
file_dog = os.path.join(current_dir, 'dog.txt')
file_cat = os.path.join(current_dir, 'cat.txt')
try:
    with open(file_dog) as dog_file:
        print(dog_file.read().rstrip())
    with open(file_cat) as cat_file:
        lines = cat_file.readlines()
        for line in lines:
            print(line.rstrip())
except FileNotFoundError:
    print('File not found')

plus()
