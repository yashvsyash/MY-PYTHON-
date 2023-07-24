#IMPORTING MODULE

"""import addmul
a=int(input("enter a number"))
b=int(input("enter a number"))

print(addmul.mul(a,b))
print(addmul.x)"""


#IMPORTING MODULE

"""from addmul import *
a=int(input("enter a number"))
b=int(input("enter a number"))

print(mul(a,b))
print(x)"""


#armstrong number
def armstrong(num,n,count,t):
    if t==0:
        if count==num:
            return True
        else:
            return False
    digit=t%10
    count=count+digit**n
    t=t/10
    return armstrong(num,n,count,t)
num=int(input("Enter a number:"))
count=0
n=len(str(num))
t=num
result=armstrong(num,n,count,t)
if result:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")



