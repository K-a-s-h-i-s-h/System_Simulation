import math
from decimal import Decimal, getcontext
getcontext().prec = 3
# READING THE INPUTS OF BOMBER AND FIGHTER
XB, YB = input("What is X-Coordinate and Y-Coordinate of Bomber: ").split()
XF, YF = input("What is X-Coordinate and Y-Coordinate of Fighter: ").split()
xb = int(XB)
yb = int(YB)
xf = int(XF)
yf = int(YF)
initial_time, final_time = input("Set initial time and final time: ").split()
starting_time = int(initial_time)
ending_time = int(final_time)
target_range = int(input("Target range: "))+1
velocity_of_fighter = input("Set velocity of fighter: ")
arrayXB = [xb]
arrayYB = [yb]
arrayXF = [xf]
arrayYF = [yf]
for t in range(1, ending_time-starting_time+1):
    xb_at_t, yb_at_t = input("What is X-Coordinate and Y-Coordinate of Bomber at time = " + str(t+starting_time) + ":").split()
    arrayXB.insert(t, int(xb_at_t))
    arrayYB.insert(t, int(yb_at_t))
initial_distance = math.sqrt(((yb-yf)**2) + ((xb-xf)**2))
distances = [initial_distance]
new_x_of_fighter = 0
new_y_of_fighter = 0
current_distance = initial_distance
targeted_time = 0
t = starting_time
while current_distance >= target_range:
    if t <= ending_time:
        new_x_of_fighter = arrayXF[t] + ((int(velocity_of_fighter)) * (arrayXB[t] - arrayXF[t])) / (distances[t])
        new_y_of_fighter = arrayYF[t] + ((int(velocity_of_fighter)) * (arrayYB[t] - arrayYF[t])) / (distances[t])
        arrayXF.insert(t+1, new_x_of_fighter)
        arrayYF.insert(t+1, new_y_of_fighter)
        current_distance = math.sqrt(((arrayYB[t+1] - arrayYF[t+1]) ** 2) + ((arrayXB[t+1] - arrayXF[t+1]) ** 2))
        distances.insert(t+1, current_distance)
        t = t + 1
        targeted_time = t + 1
    else:
        print("TARGET IS ESCAPED")
        break
else:
    if targeted_time <= int(final_time):
        print("Target has been attacked at",current_distance,"and in",targeted_time,"time unit.")
    else:
        print("TARGET IS ESCAPED")
print(arrayXF, arrayYF, distances, f"{initial_distance:.4f}", f"{new_x_of_fighter:.4f}", f"{new_y_of_fighter:.4f}", current_distance)
print(arrayXF[0], arrayYF[0])
