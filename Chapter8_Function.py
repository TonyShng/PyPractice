
def greet_user(username):
    """显示问候语"""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

'''传递实参'''
#位置实参 1函数调用多次 2位置参数的顺序很重要
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')

# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')

#默认值 设置默认值的参数必须放在没有设置的后面
def describe_pet_1(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#等效的函数调用
describe_pet_1('willie')
describe_pet_1(pet_name='willie')
describe_pet_1('harry', 'hamster')
describe_pet_1(pet_name='harry', animal_type='hamster')
describe_pet_1(animal_type='hamster', pet_name='harry')

#避免实参错误

'''返回值'''
#返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#让实参变成可选的
def get_formatted_name_1(first_name, last_name, middle_name = ''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

musician = get_formatted_name_1('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_1('john', 'hooker', 'lee')
print(musician)

#返回字典
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#结合使用函数和while循环

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name =='q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

'''传递列表'''
def greet_users(names):
    """向列表中的每位用户都发出简单的问题"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#在函数中修改列表
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#模拟打印每个设计 直到没有未打印的设计为止
# 打印每个设计后 都将其移动到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_modes):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    :param unprinted_designs: 未打印的设计
    :param completed_modes: 已完成的设计
    :return: 返回结果
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    :param completed_models: 已完成的模型
    :return: 返回结果
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#禁止函数修改列表 像函数传递列表的副本而不是原件
copy_unprinted_designs = unprinted_designs[:]  #切片表示法[:] 创建列表的副本

'''传递任意数量的实参'''
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    # print(toppings)
    print("\nMaking a pizza with the following toppings:")
    for t in toppings:
        print("- " + t)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#结合使用位置实参和任意数量实参
def make_pee(size, *toppings):
    """概述要制作的派"""
    print("\nMaking a " + str(size) + "-inch pee with the following toppings:")
    for t in toppings:
        print("- " + t)

make_pee(16, 'pepperoni')

#任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)

'''将函数存储在模块中'''
#导入整个模块
# import pizza
# pizza.make_pizza(16, 'pepperoni', 'green peppers')

#导入特定的函数 通过逗号分割函数名
# from pizza import make_pizza, print_pizza
# make_pizza(16, 'pepperoni')
# print_pizza()

#使用as给函数指定别名
from pizza import make_pizza as mp

mp(16, 'pepperoni')

#使用as给模块指定别名
import pizza as p
p.print_pizza()

#导入模块中的所有函数
from pizza import *
print_pizza()






