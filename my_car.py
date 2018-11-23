
'''导入类'''

# 导入多个类
from Chapter9_Class import Car, ElectricCar
# from Chapter9_Class import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.describe_battery())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#导入整个模块
import Chapter9_Class
my_beetle = Chapter9_Class.Car('volkswagen', 'beetle', 2016)

#导入模块中的所有类 不推荐这种方式 使用是用module_name.class_name语法访问类
from Chapter9_Class import *

#python标准库
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
















