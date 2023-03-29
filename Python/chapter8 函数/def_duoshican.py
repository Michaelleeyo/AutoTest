'''
在Python中，函数定义可以使用*args和**kwargs作为形式参数，以接受任意数量的位置参数和关键字参数。它们的区别如下：

*args: 表示可变数量的位置参数。在函数内部，它们以元组的形式存在。

**kwargs: 表示可变数量的关键字参数。在函数内部，它们以字典的形式存在。
'''
# 练习：三明治


def make_sandwich(*peiliao):
    print(peiliao)


make_sandwich('huanggua')
make_sandwich('shengcai', 'niurou')
make_sandwich('jidan', 'huluobo', 'xihongshi')

# 练习：用户简介


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_object = build_profile(
    'zhang',
    'san',
    age='18',
    school='jialidun',
    married='no'
)
print(user_object)

# 练习：汽车


def make_cars(producers, model, **cars_info):
    cars = {}
    cars['producers'] = producers
    cars['model'] = model
    for key, value in cars_info.items():
        cars[key] = value
    return cars


car = make_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)
