num1 = int(input("Enter First Number => "))
num2 = int(input("Enter Second Number => "))
onum1 = num1
onum2 = num2
while(num1!=num2):
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1
lcm = onum1 * onum2/num1
print("GCD of",onum1,"num2",onum2,"=",num1)
print("LCM of",onum1,"num2",onum2,"=",int(lcm))
