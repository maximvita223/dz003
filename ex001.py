# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
spisok = [1,2,3,2,3,2,4,4]
sum = 0
for i in range(1,len(spisok),2):
    sum+=spisok[i]
print('Сумма элементов на нечетных позициях =',sum)
        