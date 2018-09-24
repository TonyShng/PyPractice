
'''
操作列表
'''
#循环遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + '.\n')
print("Thank you, everyone. That was a great magic show!")

#缩进


#range() 可以生成一系列的数字 输出不会包含第二个值
for value in range(1, 5):
    print(value)

#用list() 直接转为列表
numbers = list(range(1, 6))
print(numbers)

# 打印1~10内的所有偶数 最后一个参数表示间隔为2
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#列表为1~10的平方
squares = []
for value in range(1, 11):
    # square = value * value
    # squares.append(square)
    squares.append(value * value)
print(squares)

# 求最大值 最小值 和的函数
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
squares = [value **2 for value in range(1, 11)]
print(squares)

#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#遍历切片
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#复制列表 直接通过切片复制
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#这种方式是无法复制列表的 只是将指针指向那个列表 并没有复制
test_list = [1, 2, 3, 4, 5]
copy_list = test_list
test_list.append(6)
print(test_list)
print(copy_list)

# 元祖 不可变的列表成为元祖
dimensions = (200, 50)













