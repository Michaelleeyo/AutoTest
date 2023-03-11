'''
sort(),sorted(),reverse(),len()
sorted()的反转是传入reverse=True
reverse只是将列表反转，不会输出结果，所有输出结果要再打印下列表
'''


place = ['beijing', 'shanghai', 'shenzhen', 'guangzhou']
print(place)
print('---not saved----')
print(sorted(place))
print(place)
print('---not saved reverse---')
print(sorted(place, reverse=True))
print(place)
print('---saved reverse---')
place.reverse()
print(place)
print('---saved sort---')
place.sort()
print(place)
