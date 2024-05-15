sales = eval(input('Enter sale value:'))
if sales >= 50000:
    comm = sales * 5 / 100
elif sales >= 40000 and sales < 50000:
    comm = sales * 2 / 100
else:
    comm = sales * 1 / 100
print("Sales:", sales)
print("Commission:", comm)