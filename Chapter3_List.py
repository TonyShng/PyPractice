
'''
列表是由一系列按特定顺序排列的元素组成
'''

bicycles = ['trek', 'cannondale', 'redline', 'spacialized']

print(bicycles)

#访问列表元素
print(bicycles[0].title())

#索引从0开始不是从1开始
#返回最后一个元素
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

friends = ['Tony', 'Lee', 'Zoom', 'Happy']
print(friends[-2])

#修改 添加 删除元素
motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

motorcycle[0] = 'ducati'
print(motorcycle)

#在列表尾部添加元素
motorcycle.append('honda')
print(motorcycle)

#在列表中插入元素
motorcycle.insert(0, 'wuling')
print(motorcycle)

#删除元素
#del语句将值从列表中删除后就无法在访问它了
del motorcycle[0]
print(motorcycle)

#pop()方法也可列表元素,但是你能够接着使用它  将原数组中的元素删除 返回这个删除的元素
popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)

first_owned = motorcycle.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#remove()方法 根据元素的值进行删除 并且可以用一个变量进行接收
motorcycle.append('wuling')
print(motorcycle)
motorcycle.append('wuling')
print(motorcycle)
my_motorcycle = motorcycle.remove('wuling')
print(motorcycle)

'''
组织列表
'''
cars_one = ['bmw', 'audi', 'toyota', 'subaru']
cars_two = ['bmw', 'audi', 'toyota', 'subaru']
cars_one.sort()
print(cars_one)
#逆序
cars_two.sort(reverse=True)
print(cars_two)

#保留原来列表的顺序
cars_three = ['bmw', 'audi', 'toyota', 'subaru']
print(cars_three)
print(sorted(cars_three))
print(cars_three)
print(sorted(cars_three, reverse=True))

cars_three.reverse()
print(cars_three)

#确定列表的长度
print(len(cars_three))
















