import math
from bisect import insort

initial_grams_of_element_A = float(input("Enter the initial grams of element A: "))
initial_grams_of_element_B = float(input("Enter the initial grams of element B: "))
initial_grams_of_element_C = float(input("Enter the initial grams of element C: "))
k1_constant = float(input("Enter the k1 constant: "))
k2_constant = float(input("Enter the k2 constant: "))
time_period = int(input("Enter the time period (in minutes): "))
delta_time_period = float(input("Enter the delta time period (in minutes): "))
iterations = int(time_period / delta_time_period)
i = 0
arrayA = [initial_grams_of_element_A]
arrayB = [initial_grams_of_element_B]
arrayC = [initial_grams_of_element_C]
for i in range(1, iterations+1):
    A = arrayA[i-1] + ((k2_constant*arrayC[i-1])-(k1_constant*arrayA[i-1]*arrayB[i-1]))*delta_time_period
    B = arrayB[i-1] + ((k2_constant*arrayC[i-1])-(k1_constant*arrayA[i-1]*arrayB[i-1]))*delta_time_period
    C = arrayC[i-1] + 2*((k1_constant*arrayA[i-1]*arrayB[i-1]) - (k2_constant*arrayC[i-1]))*delta_time_period
    arrayA.insert(i, A)
    arrayB.insert(i, B)
    arrayC.insert(i, C)
print("|\tTIME\t|\tA\t|\tB\t|\tC\t|")
print("|\t0\t|\t"+str(round(arrayA[0], 2))+"\t|\t"+str(round(arrayB[0],2))+"\t|\t"+str(round(arrayC[0],2))+"\t|")
i = 0
time = delta_time_period
for i in range (1,iterations+1):
    print("|\t"+str(round(time, 2))+"\t|\t"+str(round(arrayA[i], 2))+"\t|\t"+str(round(arrayB[i],2))+"\t|\t"+str(round(arrayC[i],2))+"\t|")
    time = time + delta_time_period