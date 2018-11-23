
class Dog():
    """一次小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被下命令蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over!")

#创建实例
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#调用方法
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
your_dog.sit()

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #给属性设置默认值

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """加满汽油"""
        pass

    def increment_odometer(self, mileage):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mileage


    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + ' miles on it.')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

'''给属性指定默认值'''
my_new_car.read_odometer()

'''修改属性的值'''
# 第一种 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#第二种 通过方法修改属性的值
my_new_car.update_odometer(24)
my_new_car.read_odometer()

#第三种 通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


######## 继承
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        初始化父类的属性，再初始化电动车特有的属性
        """
        super().__init__(make, model, year) #注意super后面的括号
        # self.battery_size = 70
        self.battery = Battery()


    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        # print("This car has a " + str(self.battery_size) + "-kWh battery.")
        print("This car has a " + str(self.battery.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need  a gas tank!")



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

#给子类定义属性和方法
my_tesla.describe_battery()

#重写父类的方法
my_tesla.fill_gas_tank()

#将实例用作属性
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#模拟实物

'''导入类'''
#my_car.py中

































