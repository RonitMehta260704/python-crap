print("the largest among the three")
num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))
if((num1>num2) and (num1>num3)):
    print("num1 is greater")
elif((num2>num1)and(num2>num3)):
    print("num2 is greater")
elif((num3>num1) and (num3>num2)):
    print("num3 is greater")
else:
    print("all numbers are eqaul")
