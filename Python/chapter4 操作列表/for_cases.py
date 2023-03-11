pizzas = ['a', 'b', 'c']
for pizza in pizzas:
    print(pizza)
    print('I like '+pizza)
print('I really like pizza')

pets = ['dog', 'cat', 'monkey']
for pet in pets:
    print('A '+pet+' would make a great pet')
print('Any of these animals would make a great pet!')

friend_pizzas = pizzas[:]
pizzas.append('d')
friend_pizzas.append('f')
print('My favorite pizzas are')
print(pizzas)
print("My friend's favorite pizzas are")
print(friend_pizzas)
