# Задание 4. Уровень - гросмейстер.
# Условие: Известно, что на доске 8×8 можно расставить 8 ферзей так, ч
# тобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга.

# Входные данные: программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.

# Выходные данные : eсли ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

# Пример:
# Ввод:                                        # Вывод:
# 1 7
# 2 4
# 4 8 
# 3 2
# 8 5
# 7 3
# 6 1 
# 5 6                                          NO


a,a1=map(int,input().split())
b,b1=map(int,input().split())
c,c1=map(int,input().split())
d,d1=map(int,input().split())
e,e1=map(int,input().split())
f,f1=map(int,input().split())
g,g1=map(int,input().split())
h,h1=map(int,input().split())

if a + b + c + d + e + f + g + h == a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1:
    print ("NO")
elif a == a1 or b == b1 or c == c1 or d == d1 or e == e1 or f == f1 or g == g1 or h == h1:
    print ("YES")
else:
    print("YES")
