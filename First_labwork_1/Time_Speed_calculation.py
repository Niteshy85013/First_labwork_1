'''if you lives 4 milesaway from university. The bus driver drives at 25mph but spends 2minute at each
ofthe 10 stops on the way . how  long will the bus journey take? alternatively,you could run to university
 you  jog the first mile at 7mph then run the next stop at 15mph ,before jogging the  last  at 7mph again
 will this be quicker  or slower than the bus.'''

Living_else_apart=4
drives_velocity=25
time_taken=((Living_else_apart/drives_velocity)+60)

# 2 minute in each stop;

Time_speed = 20
Total_time = time_taken+Time_speed
print(f"total time taken by the bus is {Total_time}")
jog_one = ((1/7)+60)
jog_two = ((2/15)+60)
jog_three = ((1/17)+60)
total_walk_time = jog_one+jog_three
print(f"Time taken by the running is {total_walk_time}")

if(Total_time >total_walk_time):
    print(f"Taking bus is slower than running.")
else:
    print(f"Taking bus is quicker than running.")
