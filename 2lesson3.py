my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = -1
while a < len(my_list):
    a = a + 1
    b = my_list[a]
    if b == 0:
        continue
    elif b >= 0:
        print(my_list[a])
    else: 
        break






