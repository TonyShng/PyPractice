# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")
#
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print("\nHello, " + name + "!")

# age = input("How old are you? ")
# print(age)
#
# #int()函数将字符串转为数值表示
# age = int(age)
# print(age>18)

# height = input("How tall are you, in inches? ")
# height = int(height)
#
# if height >= 36:
#     print("\nYou're tell enough to ride! ")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

"""
求模运算符 % 取余数
"""

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
#
# if number%2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")

"""
while循环
"""

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


"""
使用break
"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


"""
continue
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number%2 == 0:
        continue

    print(current_number)

"""
使用while循环来处理列表和字典
"""
# 首先创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证的用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

"""
删除包含特定值的所有列表元素
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

"""
使用用户输入来填充字典
"""
responses = {}

#设置一个标志 指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == 'no':
        polling_active = False

#调查结束 显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")




























