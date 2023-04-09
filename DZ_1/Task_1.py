# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

numb = int(input("Введите трехзначное число: "))
if 100 <= numb <= 999:
    first_numb = numb // 100
    second_numb = (numb % 100) // 10
    third_numb = numb % 10
    print("Сумма цифр трехзначного числа равна = ", first_numb + second_numb + third_numb)
else:
    print("Введите корректное число")