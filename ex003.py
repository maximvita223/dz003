# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

spisok = [1.4, 1.2, 3.2, 5, 10.03]
max = spisok[0]-int(spisok[0])
min = spisok[0]-int(spisok[0])
for i in range(1,len(spisok)):
    if max<spisok[i]-int(spisok[i]):
        max = spisok[i]-int(spisok[i])
        # print(max)
    elif min > spisok[i]-int(spisok[i])and spisok[i]-int(spisok[i])!=0 :
        min = spisok[i]-int(spisok[i])
        # print(min)
preff = (max-min)*100
print(int(preff)/100)
# print(max-min)