
# 练习：使用OrderedDict
from random import randint
from collections import OrderedDict
houzhui = OrderedDict()
houzhui['python'] = '.py'
houzhui['java'] = '.java'
houzhui['php'] = '.php'

for language, houzhuiming in houzhui.items():
    print(language+'wenjian houzhui shi '+houzhuiming)


# 练习：骰子


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# 掷骰子10次
for times in range(1, 11):
    # 默认6面
    Die().roll_die()
print('====================')
for times in range(1, 11):
    # 默认10面
    Die(10).roll_die()
print('====================')
for times in range(1, 11):
    # 默认20面
    Die(20).roll_die()
print('====================')
