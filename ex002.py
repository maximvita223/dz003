# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

spisok = [1,4,5,6,8,9,5]

# for  i in range(0,len(spisok)):
#     print(spisok[i]*spisok[-i-1])
    
i = 0
while i < len(spisok)/2:
    print(spisok[i]*spisok[-i-1]) 
    i += 1 