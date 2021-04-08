'''weight conveter :
 input the weight of a person in either kg or lbs.if person provides his/her weight in kg then
convert  it into  lbs else convert it in to kg.'''


user_weight=float(input("Enter your weight:\n"))
user_choice=input("choose if you want to convert it in to kg or lbs:\n")
if(user_choice=="kg"):
    print(f"the weight in lbs is {user_weight*2.205}")
elif(user_weight=="lbs"):
    print(F"the weight in kg is {user_weight*0.453}")
else:
    print("It is not reconogized")
