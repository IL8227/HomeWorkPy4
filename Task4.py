# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint, random



a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
k = int(input('Введите значение степени: '))

polinom = f'{a} * x^{k} + {b} * x + {c}'
print(polinom)
 

with open('file_task4', 'w+') as f:
    f.write(polinom)


