'''def sum(x,y):
    return x+y
a= int(input("enter the first number:"))
b= int(input("enter the second number:"))
c=sum(2,3)'''


'''def add():
    a=int(input("enter the first num:"))
    b=int(input("enter the second num: "))
    print(f"the sum of  {a} and {b} is {a+b}")
add()
'''

'''def sub(a,b):
    a = int(input("enter the first num:"))
    b = int(input("enter the second num: "))
    print(f"the sub of {a} and {b } is {a-b}")
sub(5,2)'''


'''def  mul(a,b):
    print(f"the mul of {a} and {b} is {a*b}")

    return a*b
a=int(input("enter the first  num:"))
b=int(input("enter the  second num:"))
c=mul(a,b)
print(c)'''



'''def div(a,b):
    print(f"the div  of  {a} and {b} is {a / b}")
    return a/b
a=int(input("enter the first num:"))
b=int(input("enter the second num:"))
c= div(a,b)
print(c)'''


def mul_table(num):

    for i in range (1,11):
        product=num*1
        print(f"{num}*{i}={product}")
num=int(input("enter the num:"))
mul_table(num)




