# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
N = int(input("Введите число: "))
for y in range(1, N + 1):
    for x in range(1, y + 1):
        print(y, end=" ")
    print("\n")