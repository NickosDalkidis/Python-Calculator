print("Welcome to the calculator")
ans=input("Press 1 for English or press 2 for greek")
if ans==1: 
    num1=input("Please Enter a number")
    num2=input("Please Enter Another Number")
    result= float(num1)+float(num2)
    result2=float(num1)*float(num2)
    result3=float(num1)-float(num2)
    βαση=float(input("Enter the base number"))
    εκθετης=float(input("Enter the exponent"))
    result4=βαση**εκθετης
    num3=float(input("Please enter the number you want to be divised"))
    num4=float(input("Please enter the number want to divise the previous number with"))
    result5=num3//num4
    print("Addition")
    print(result)
    print("Multiplication")
    print (result2)
    print("Subtraction")
    print(result3)
    print ("raise to power")
    print (result4)
    print("Division")
    print (result5)
else: 
        num1=input("Παρακαλώ εισαγετε εναν αριθμο")
        num2=input("Παρακαλω εισαγετε εναν αλλο αριθμο")
        result= float(num1)+float(num2)
        result2=float(num1)*float(num2)
        result3=float(num1)-float(num2)
          βαση=float(input("Εισαγετε την βαση "))
        εκθετης=float(input("))
        result4=βαση**εκθετης
        num3=float(input("Please enter the number you want to be divised"))
        num4=float(input("Please enter the number want to divise the previous number with"))
        result5=num3//num4
        print("Addition")
        print(result)
        print("Multiplication")
        print (result2)
        print("Subtraction")
        print(result3)
        print ("raise to power")
        print (result4)
        print("Division")
        print (result5)
