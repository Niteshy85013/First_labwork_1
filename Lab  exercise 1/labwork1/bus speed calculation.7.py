# you live 4 miles from university. the bus drives at 25mph but spends 2 minutes  at each of the
#  10 stops on the way. how long will the bus journey take? alternatively,you could run to university
#. you jog the first mile at 7mph.then run the next two at 15mph,before jogging the last at 7mph again
# will this be quicker or slower then the bus?

living_else_apart=4
drives_velocity=25
time_taken=((living_else_apart/drives_velocity)+60)

# 2 minutes in each stop
time_speed=20
total_time=time_taken+time_speed
print(f"total time taken by bus  is {total_time}")

jog_one=((1/7)+60)
jog_two=((2/15)+60)
jog_three=((1/7)+60)
total_walk_time=jog_one+jog_three
print(f"time taken by running is {total_walk_time}")

if (total_time>total_walk_time):
    print("Taking bus is slower than running")
else:
    print("Taking bus is quicker than running")



