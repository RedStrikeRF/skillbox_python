number = input("Введите число,чтобы добавить его, либо end, чтобы закончить ввод: ")
N = []

# Тут нужно как-нибудь ввести список чисел, я выбрал способ, где числа вводятся до тех пор, пока не будет введено "end"
while number != "end":
    N.append(int(number))
    number = input("Введите число,чтобы добавить его, либо end, чтобы закончить ввод: ")

print(f"Изначальный список: {N}")
N.sort()
print(f"Отсортированный список: {N}")
