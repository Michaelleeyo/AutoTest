
# 练习：魔术师
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['zhao', 'qian', 'sun', 'li']
show_magicians(magicians)

# 练习：了不起的魔术师


def make_great(great_magicians, magicians):
    while magicians:
        great_magician = 'the Great '+magicians.pop()
        great_magicians.append(great_magician)


great_magicians = []
#make_great(great_magicians, magicians)
# show_magicians(great_magicians)

# 练习：不变的魔术师
make_great(great_magicians, magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
