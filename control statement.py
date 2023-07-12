"""#IF-ELSE STATEMENT
Num=int(input("Enter the Marks"))
print("The Marks is:",Num)
if Num%2==0:
    print("The Number is Even")
else:
    print("The Number is Odd")

    

#VOTING ELIGIBILITY
AGE=int(input("Enter the Age"))
if AGE>=18:
    print("You are eligible to Vote")
else:
    print("You are not eligible to Vote")

    

#CHECK POSITIVE NUMBER
Num=int(input("Enter the Number"))
if Num>0:
    print("The Number is Positive")
else:
    print("The Number is Negative")


#To Compare two numbers    
Num1=int(input("Enter the Number1"))
Num2=int(input("Enter the Number2"))
if Num1>Num2:
    print("The Number1 is greater than Number2")
else:
    print("The Number2 is greater than Number1")"""


#To find DIVISON on the basis of Marks Obtained

Marks=int(input("Enter the Number"))
Percent=Marks/5
print("Your Percentage =",(Percent))
if Percent>=95 and Percent<=100:
    print("You got 1st Divison")

elif Percent>=80 and Percent<95:
    print("You got 2nd Divison")
    
elif Percent>=60 and Percent<80:
    print("You got 3rd Divison")
    
else:
    print("You are FAIL")

    


    
