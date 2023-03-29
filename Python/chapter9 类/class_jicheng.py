
# 练习：冰激凌小店
from class_cases import User
from class_cases import Restaurant


class IceCream(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['a', 'b', 'c']


IceCream('d', 'e').describe_restaurant()
print(IceCream('d', 'e').flavors)
print('===================================')


# 练习：管理员
# 练习：权限


class Privileges_Class():
    def __init__(self, privileges=['can add post', 'can delete post']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        #self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges_Class()


lao_liu = Admin('lao', 'liu')
lao_liu.privileges.show_privileges()
print('============================')


# 练习：升级
# 略
