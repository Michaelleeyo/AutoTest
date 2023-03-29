
# 练习：熟食店
sandwich_orders = ['a', 'b', 'c']
done_sandwich = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print('I made you '+finished_sandwich+' sandwich')
    done_sandwich.append(finished_sandwich)

print('all done:')
for a in done_sandwich:
    print(a)


# 练习：卖完了
goods = ['a', 'b', 'a', 'c', 'd', 'a', 'b']
print('goods a sold out,left goods are')
while 'a' in goods:
    goods.remove('a')
for good in goods:
    print(good)


# 练习：梦想的度假胜地
dream_places = {}
promote_name = '\nYour name:'
promote_place = '\nIf you would visit one place in the world,where would you go ?'
promote_place += '\n(Enter quit to quit)\n'

while True:
    name = input(promote_name)
    if name == 'quit':
        break
    place = input(promote_place)
    if place == 'quit':
        break
    else:
        dream_places[name] = place

for name, place in dream_places.items():
    print(name+"'s dream place is "+place)
