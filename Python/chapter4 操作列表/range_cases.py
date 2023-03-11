# 数到20
for value in range(1, 20):
    print(value)

# 1-100000的总和
hundredthound = list(range(1, 100000))
print(min(hundredthound))
print(max(hundredthound))
print(sum(hundredthound))

# 打印奇数
for value in list(range(1, 20, 2)):
    print(value)

# 3的倍数
thirdplus = [value for value in range(3, 30, 3)]
print(thirdplus)

# 立方
cube = [value**3 for value in range(1, 10)]
print(cube)
