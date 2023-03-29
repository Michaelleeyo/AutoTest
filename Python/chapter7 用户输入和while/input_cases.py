# 练习：汽车租赁
message = input('Please input what you want:')
print('Let me see if i can find you a '+message)


# 练习：参观订位
number = input('Please input how many people:')
number = int(number)
if number > 8:
    print('not available')
else:
    print('available')


# 练习：10的倍数
number = input('Input a number:')
number = int(number)
if number % 10 == 0:
    print('The number is a multiple of ten')
else:
    print('The number is not a multiple of ten')
