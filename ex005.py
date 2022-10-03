# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
fib1 = fib2 = 1
 
n = int(input())
spi = []
spi.append(1)
spi.append(2)

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    spi.append(fib2)
spi2 = str(spi[::-1])
spi1 = str(spi)
spi2=spi2.replace(' ', '-')
spi2 = spi2.replace('[','')
spi1 = spi1.replace('[','')
spi2 = spi2.replace(']','')
spi1 = spi1.replace(']','')
print(f'-{spi2}, -1, 0, {spi1}')