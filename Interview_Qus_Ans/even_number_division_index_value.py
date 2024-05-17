num_lst = [x for x in range(50) if x % 2 != 0]
for index, number in enumerate(num_lst):
    try:
        result = number / index
    except ZeroDivisionError:
        result = "It can not be divided"
    print(f"{number} / {index} = {result}")