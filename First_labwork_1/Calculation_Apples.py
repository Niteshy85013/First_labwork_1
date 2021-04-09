'''N students take K apple and distribute them among each student eventually the remaining part in the 
  basket. How many should each student get? how many apples will remain in the basket? the programs read 
  the number N and K.  '''

N=int(input("Enter the number of the student in the  class:"))
K=int(input("Enter the number of apples:"))
Apples_get=(K//N)
Remaining_apple=(K%N)
print(f"Each student get {Apples_get}, and the remaining apples are {Remaining_apple}:")







