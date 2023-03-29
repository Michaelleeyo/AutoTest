# 练习：电影票
while True:
    age = input('Please input age:')
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print('Free!')
        elif age > 12:
            print('$15')
        else:
            print('$12')
