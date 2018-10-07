alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_point = alien_0['points']
print("You just earned " + str(new_point) + " points!")

#添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

#例子
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))

#删除键值对
del alien_0['speed']
print(alien_0)

#由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

#遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see you favorite language is " + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking th poll.")

# 遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#用set(集合)去除重复项
for language in set(favorite_languages.values()):
    print(language.title())


#嵌套
#字典列表
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15

for alien in aliens[:5]:
    print(alien)
print('...')
print("Total number of aliens:" + str(len(aliens)))

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}

print("You ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# 字典中嵌套字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
























