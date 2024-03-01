num = input('Enter a number (decimal only): ')
# type your code here
dp = 0
a = num.find(".")
num2 = num[a+1::]
for x in num2:
    dp += 1




# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
