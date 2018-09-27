
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# == 判断相等时是区分大小写的
print('audi' == 'Audi')

# 判断两个值不相等 !=
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

#比较数字
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not correct answer. Please try again!")

print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#检查多个条件 and类比&& or类比||
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#检查某个值是否包含在列表中 in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#检查特定值是否不包含在列表中 not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#if-elif-else 语句
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) +".")

# 在if-elif中 可以省略else语句

#测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")

#检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#检查列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + '.')
    print("\nFinished making your pizza!")
else:
    print("Are you shre you want a plain pizza?")

#使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', ['pepperoni', 'pineapple', 'extra cheese']]
requested_toppings = ['mushrooms', 'frech fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print("\nFinished making your pizza!")





