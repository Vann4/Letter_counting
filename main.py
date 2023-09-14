#Задача, пользователь вводит строку состоящую из Р(решка) и О(орёл), подсчитать сколько Р введено подряд, если ни одной то вывести 0
user_string = input('Введите Р и О: ').lower().split('о')
user_string_count = 0
print()
for i in max(user_string):
    user_string_count += i.count('р')
print('Столько раз вы ввели Р(решку):',user_string_count)