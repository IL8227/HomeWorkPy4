# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# *Пример*

# - при       ->        [2, 4, 5, 9]



lst_1 = list(input('Введите числа: '))
print(lst_1)
lst_2 = []
for i in range(len(lst_1)):
    count = 1
    for s in range(len(lst_1)):
        if i == s:
            continue
        if lst_1[i] == lst_1[s]:
            count += 1
    if count == 1:
        lst_2.append(lst_1[i]) 
print(lst_2)       


 
    
    
    
        
