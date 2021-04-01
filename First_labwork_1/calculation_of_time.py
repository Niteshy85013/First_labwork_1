'''The given integer N=The number of minutes that is passed since  midnight = how many minutes
and hours are displayed on the 24h digital clock ? the program should print the two hours
(between 0 and 23) and number of minutes between (0 and 59) for example  if N=150,then 150 minute
have passed since midnight i.e  now is  2:30 so, the the program should  print 2:30 '''

N=int(input("enter the minute passed since mid night:"))
hours=(N//60)
minutes=(N%60)
print(f"The hour is {hours}")
print(f"The minutes is {minutes}")
print(f"its {hours}:{minutes} now.")
