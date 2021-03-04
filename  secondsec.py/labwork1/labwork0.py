# N student take k apples and distribute them among each student eventually.
# the emaining part remain in the basket.
# how many apples should each student get?
# how many apples will remain in the basket?the programs read the number N and K

n=int(input("enter the number of student in class:"))
k=int(input("enter the number of apples:"))
apples_get=(k//n)
remaining_apples=(k%n)
print(f"each  student get {apples_get} ")
print(f"the remaining apples are {remaining_apples}")




