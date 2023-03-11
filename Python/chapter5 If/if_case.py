alien_color = 'green'
if alien_color == 'green':
    print('you get 5 points')
elif alien_color == 'pink':
    print('you get 10 points')
else:
    print('you got 15 points')


favorite_fruit = ['apple', 'banana', 'lemon']
if 'apple' in favorite_fruit:
    print('You really like apple!')
else:
    print("You don't like apple")


# 练习：特殊方式跟管理员打招呼
# customs = ['admin', 'zhangsan', 'lisi', 'wangwu', 'zhaogao']
customs = []
# 判断用户是否为空
if customs:
    for custom in customs:
        if custom == 'admin':
            print("Hello,admin,would you like to see a status report")
        else:
            print('Hello '+custom+',thank you for logging in again')
else:
    print('We need to find some users!')


# 练习：检查用户名
current_users = ['Zhao', 'Qian', 'Sun', 'Li', 'Zhou']
new_users = ['zhang', 'li', 'wang', 'sun', 'Wu']
# 用于不区分大小写
users_lower = [value.lower() for value in current_users]
for new_user in new_users:
    if new_user.lower() in users_lower:
        print(new_user+',Already Existed')
    else:
        print(new_user+',Not Found')


# 练习：序数
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number)+'th')
