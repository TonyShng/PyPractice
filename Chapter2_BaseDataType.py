
'''
字符串
'''
message = 'hello world'
print(message)

message = "hello Python Crash Course world"
print(message)

#title()方法 让每个单词的首字母变成大写的 其他的字母为小写的
name = "ada lovelace"
print(name.title())

#low()方法 将所有字母变成小写的
text = "Test Name"
print(text.lower())

#拼接字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)
print("hello," + full_name.title() + "!")
message = "hello," + full_name.title() +"!"
print(message)

#制表符或者换行符来添加空白
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print("\tPython")

#去掉字符串中开头和结尾多余的空白
favorite_language = 'python '
print(favorite_language + '!')
print(favorite_language.rstrip() + '!')

favorite_language = ' python '
#去掉结尾的空白
print('!' + favorite_language.rstrip() + '!')
#去掉开头的空白
print('!' + favorite_language.lstrip() + '!')
#去掉两端的空白
print('!' + favorite_language.strip() + '!')

#语法错误
#这个时候如果里面有撇号 外面就不能使用单引号
message = "One of Python 's strengths is its diverse community"
print(message)

test_name = 'Tony'
print('Hello ' + test_name.title() + ',' + 'would you like to learn some Python today?')

print(test_name.lower(), test_name.upper(), test_name.title())


'''
数字
'''

#整数
print(2 + 3)

#浮点数 即带小数点的数字
print(0.1 + 0.2)

print(3/2)

# str() 避免类型错误
age = 23
message = "Happy " + str(age) + 'rd Birthday!'
print(message)

#Python之禅
import this



