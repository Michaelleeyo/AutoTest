import os
dir_path = os.path.dirname(__file__)
file_path_1 = os.path.join(dir_path, 'guest.txt')
file_path_2 = os.path.join(dir_path, 'guest_book.txt')
file_path_3 = os.path.join(dir_path, 'love_programming.txt')

# 练习：访客
with open(file_path_1, 'w')as content_1:
    name = input('Enter your name:')
    content_1.write(name+'\n')

# 练习：访客名单
with open(file_path_2, 'w') as content_2:
    while True:
        guest = input('Enter your name:(q to exit)')
        if guest == 'q':
            break
        content_2.write(guest+' reached\n')
        print('Welcome!')

# 练习：写入喜欢编程的原因
with open(file_path_3, 'a')as content_3:
    reason = input('why you like programming:')
    content_3.write(reason+'\n')
