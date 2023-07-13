#NESTED CONTROL STATEMENT

a=int(input("Enter value of a num"))
b=int(input("Enter value of b num"))
c=int(input("Enter value of c num"))

print("a =",a)
print("b =",b)
print("c =",c)

if a>b:
    if a>c:
        print("a is greatest")
    else :    
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else :    
        print("c is greatest")
        
#GREATEST NUMBER USING RELATIONAL OPERATOR
        
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else :
    print("c is greatest")


#CALCULATOR USING NESTED CONTROL STATEMENT

a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
OP=input("Enter the operator")


print("a =",a)
print("b =",b)


if OP=="+":
    print("The Addition of a & b =",a+b)
    
elif OP=="-":
    print("The Subtraction of a & b =",a-b)

elif OP=="*":
    print("The Multiplication of a & b =",a*b)

elif OP=="/":
    print("The Division of a & b =",a/b)

elif OP=="//":
    print("The Floor Division of a & b =",a//b)

elif OP=="%":
    print("The Modulus of a & b =",a//b)
    
    
else:
    print("YOU HAVE ENTERED AN INVALID OPERATOR")
    
    
