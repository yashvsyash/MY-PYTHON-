#
"""def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
x=fact(6)
print("Factorial of 4 is",x)"""



#
"""def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
n=int(input("ENTER A NUMBER"))
x=fact(n)
print("Factorial of 4 is",x)"""


#adding digits of a number using recursion
"""def dig(n):
    if n==0:
        return 0
    else:
        return n%10+dig(int(n/10))
y=int(input("ENTER A NUMBER"))
result=dig(y)
print(result)"""


#LAMBDA FUNCTION{SQUARE OF A NUMBER}
"""s=lambda a: a*a
x=s(4)
print(x)"""


#LAMBDA FUNCTION{SQUARE OF A NUMBER}

"""s=lambda a: a*a
n=int(input("ENTER A NUMBER"))
x=s(n)
print(x)"""


#LAMBDA FUNCTION {CUBE OF A NUMBER}
"""s=lambda a: a*a*a
n=int(input("ENTER A NUMBER"))
x=s(n)
print(x)"""


#LAMBDA FUNCTION {addition OF NUMBERs}
"""s=lambda a,b: a+b
m=int(input("ENTER A NUMBER"))
n=int(input("ENTER A NUMBER"))
x=s(m,n)
print(x)"""

#
"""items_cost=[99,10000,100,444,3444,4949]
gt_thousand=filter(lambda x:x>1000,items_cost)
x=list(gt_thousand)
print("ELIGIBLE FOR DISCOUNT",x)"""


#
"""withoutgst_cost=[100,200,300,400]
withgst_cost=map(lambda x:x+10,withoutgst_cost)
x=list(withgst_cost)
print("WITHOUT GST ITEM COST",withoutgst_cost)
print("WITh GST ITEM COST",x)"""


#
from functools import reduce
each_items_costs=[111,222,333,444]
total_cost=reduce(lambda x,y:x+y, each_items_costs)
print(total_cost)


