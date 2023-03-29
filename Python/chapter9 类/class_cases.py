
# 练习：餐馆
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name+self.cuisine_type)

    def open_restaurant(self):
        print('open!')


restaurant_a = Restaurant('zhongcanguan', 'zhongcan')
restaurant_b = Restaurant('riliaoguan', 'riliao')
restaurant_a.describe_restaurant()
restaurant_b.describe_restaurant()


# 练习：用户
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name+' '+self.last_name)

    def greet_user(self):
        print(self.first_name+',hello')


zhangsan = User('zhang', 'san')
lisi = User('li', 'si')
zhangsan.describe_user()
lisi.greet_user()
