
# 练习：T恤
def make_shirt(size, tag):
    size = int(size)
    print('Size is '+str(size)+',tag is '+tag)


make_shirt(15, 'hh')


# 练习：大号T恤
def make_shirt2(size, tag='I love python'):
    print('The size is '+size+',tag is '+tag)


make_shirt2('big')


# 练习：城市
def describe_city(city, country='Iceland'):
    print(city+' is in '+country)


describe_city('Reykjavik')
describe_city('beijing', 'china')
describe_city(city='shanghai', country='china')
