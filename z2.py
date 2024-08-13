first, second, third = map(int, input('Ввелите 3 целых числа:').split())
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

