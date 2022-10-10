# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.


from random import randint, random



a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
k = int(input('Введите значение степени: '))

polinom = f'{a} * x^{k} + {b} * x + {c}'
print(polinom)
 

with open('file_polinom_1', 'w+') as f:
    f.write(polinom)

a_2 = randint(0, 100)
b_2 = randint(0, 100)
c_2 = randint(0, 100)

polinom_2 = f'{a_2} * x^{k} + {b_2} * x + {c_2}'
print(polinom_2)
 

with open('file_polinom_2', 'w+') as h:
    h.write(polinom_2)


sum_polinom = f'{a + a_2} * x^{k} + {b + b_2} * x +{c + c_2}'


with open('sum_polinom', 'w+') as g:
    g.write(sum_polinom)