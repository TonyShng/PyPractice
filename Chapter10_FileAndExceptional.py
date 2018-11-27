'''从文件中读取数据'''

#读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    # print(contents)
    print(contents.rstrip()) #删除字符串末尾的空白

# 文件路径  相对路径  绝对路径 C:\Users\TonyShng\Desktop\pi_digits.txt

# 逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 使用文件的内容
pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# 包含一百万位的大型文件
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

# 圆周率中包含你的生日么
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday dose ont appear in first million digits of pi.")

'''写入文件'''
#写入空文件
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 写入多行 \n

# 附加到文件
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

'''异常'''
# 处理ZeroDivisionError异常

# print(5/0)

#使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 使用异常避免崩溃
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    # 这时候如果second_number == 0的话 就会崩溃
    try:
        answer = int(first_number) / int(second_number)
        # print(answer)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 处理FileNotFoundError异常
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " dose not exist."
    print(msg)

#　分析文本
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " dose not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split() # split()方法生成一个列表，包含文本的所有单词
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

# 使用多个文件 封装成一个方法
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " dose not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

'''存储数据'''
# 使用json.dump() 和json.load()
import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj) # json.dump() 接受两个实参： 要存储的数据以及可用于存储数据的文件对象

with open(filename) as f_obj:
    numbers = json.load(f_obj) # json.load() 加载f_obj中的信息，并将其存储到变量numbers中

print(numbers)

# 保存和读取用户生成的数据
username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "！")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back," + username + "!")


# 重构
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()








