#Задача, пользователь вводит строку состоящую из Р(решка) и О(орёл), подсчитать сколько Р введено подряд, если ни одной то вывести 0
user_string = input('Введите Р и О: ').lower().split('о')
user_string_count = 0
user_string_count += max(user_string).count('р')
print('\nМаксимальное количество подряд выпавших Р(решек):',user_string_count)