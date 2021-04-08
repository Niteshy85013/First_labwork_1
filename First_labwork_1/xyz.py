'''def sum(a,b=2):
    return a+b
d=int(input("enter the first number:"))
e=int(input("enter the second number:"))
print(sum(d,e))'''

'''def sum(*Nitesh):
    print(Nitesh)
sum(1,2)
sum(1,2,3,4,5,6,7,8,9)'''


def sum(**Kwargs):
    print(Kwargs)
    sum=0
    for i in Kwargs.values():
        sum=sum+i
        return sum

    print(sum(a=2,b=3,c=4))



