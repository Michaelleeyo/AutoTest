def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number/2
    else:
        print(3*number+1)
        return 3*number+1


try:
    input_number = int(input('输入数字：'))
    while input_number != 1:
        input_number = int(collatz(input_number))
        continue
except:
    print('输入整型')
