# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = int(input("Введите номер билета в виде шестизначного числа: "))
reminder = number
first = 0
second = 0
while reminder > 999:
    first += reminder%10
    reminder//=10
else:
    while reminder > 0:
        second +=reminder%10
        reminder//= 10
if first == second:
    print("Ура! У вас счастливый билет!")
else:
    print("Ваш билет несчастливый, потому что счастливым будет целый день!")
