"""
Задача 4. Уровень  - да ты кодер.

 
Условие

На вход вашей программе в стандартном вводе даны два натуральных числа А и В. 
A >= 0 ; B >= 0;
Выведите в стандартный вывод их НОД (наибольший общий делитель). 


A = ...
B = ...
Рекомендация : не поленитесь, чекните, что такое функции и их синтаксис в Python.
Создайте функцию, которая подсчитывает NOD и возвращает результат. 

На проверке у меня 10 тестов. Если валится хотя бы на одном - задача не засчитана.
Пока тесты без времени. Но это пока).

Пример :
Ввод:                   Вывод:
25 27	                NOD:1
12 16	                NOD:4
13 13             	NOD:13

"""

a,b=map(int, input().split())
if a >= 0 and b >=0 :
  while b != 0:
    a,b = b, a%b
  print('NOD:',a)
else:
  print('Введенное число(а) меньше нуля')

    