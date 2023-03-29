
# 练习：就餐人数
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Number is '+str(self.number_served))

    def open_restaurant(self):
        print('open!')

    def set_number_served(self, max):
        self.number_served = int(max)

    def increment_number_served(self, server):
        self.number_served += server


restaurant_a = Restaurant('zhongcanguan', 'zhongcan')

restaurant_a.set_number_served(300)
restaurant_a.describe_restaurant()
restaurant_a.increment_number_served(100)
restaurant_a.describe_restaurant()


# 尝试登录次叔
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('Login attempts is '+str(self.login_attempts))

    def greet_user(self):
        print(self.first_name+',hello')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


zhangsan = User('zhang', 'san')
zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()
zhangsan.describe_user()

zhangsan.reset_login_attempts()
zhangsan.describe_user()
