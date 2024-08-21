first = 3
second = 6
third = 9
if first == second == third:
    print(3)
elif first == second and first == third and second == third:
    print(2)
elif first != second and first != third and second != third:
    print(0)