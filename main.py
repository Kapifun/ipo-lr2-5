octal_number = input("Введите число в восьмеричной системе счисления (5 разрядов): ") #запрашиваем у пользователя ввести число в восьмеричной системе счисления
#преобразование восьмеричного числа в десятичное
decimal_number = int(octal_number, 8)
#вывод результата
print("Число в десятичной системе счисления:", decimal_number)
