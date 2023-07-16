#
"""x=1
while x<=5:
    print("shiv")
    x+=1"""

#
"""n=int(input("ENTER A NUMBER"))
i=1
while i<=n:
    print(i,end=' ')
    i+=1"""


#
n=int(input("ENTER A NUMBER"))
a=-2
b=-1
count=1
while count<=n:
    fab=a+b
    a=b
    b=fab
    print(fab)
    count+=1
    

