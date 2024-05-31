num_1=eval(input('Enter first number:'))
num_2=eval(input('Enter second number:'))
num_3=eval(input('Enter third number:'))
if num_1 > num_2 and num_1 > num_3:
    print('The largest number is',num_1)
elif num_2 > num_1 and num_2 > num_3:
    print('The largest number is',num_2)
else:
    print('The largest number is',num_3)