
# 练习：人
zhao = {
    'name': 'zhao',
    'age': 23,
    'city': 'London'
}
qian = {
    'name': 'qian',
    'age': 27,
    'city': 'London'
}
sun = {
    'name': 'sun',
    'age': 17,
    'city': 'London'
}
people = [zhao, qian, sun]
for person in people:
    print(person['name']+str(person['age'])+person['city'])


# 练习：宠物
dog = {
    'name': 'dog',
    'master': 'zhangsan'
}
cat = {
    'name': 'cat',
    'master': 'lisi'
}
mouse = {
    'name': 'mouse',
    'master': 'wangwu'
}
pets = [dog, cat, mouse]
for pet in pets:
    print(pet['master']+"'s "+pet['name'])


# 喜欢的地方
favorite_places = {
    'zhangsan': ['beijing', 'shanghai'],
    'lisi': ['guangzhou', 'shenzhen'],
    'wangwu': ['nanjing']
}
for name, places in favorite_places.items():
    if len(places) > 1:
        print(name+"'s favorite places are ")
        for place in places:
            print(place)
    else:
        print(name+"'s favorite place is "+places[0])


# 练习：喜欢的数字
favorite_numbers = {
    'zhao': [1, 4],
    'qian': [2, 0],
    'sun': [6, 8, 9]
}
for name, favorite_number in favorite_numbers.items():
    print(name+"'s favorite number are ")
    for number in favorite_number:
        print(number)


# 练习：城市
cities = {
    'beijing': {
        'country': 'China',
        'population': '2000w',
        'fact': 'capital'
    },
    'new york': {
        'country': 'USA',
        'population': '1000w',
        'fact': 'capital'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '3000w',
        'fact': 'capital'
    },
    'shanghai': {
        'country': 'China',
        'population': '2000w',
        'fact': 'not capital'
    }
}
for city, city_infos in cities.items():
    print(city+' belongs to '+city_infos['country'] +
          ', has ' + city_infos['population']
          + ' people'+' and is '+city_infos['fact'])
