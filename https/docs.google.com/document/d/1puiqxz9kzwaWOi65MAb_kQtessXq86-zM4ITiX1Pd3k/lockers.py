import random
from time import sleep
right = 0
i = 0

print("How many lockers and students are there?")
total_lockers = int(raw_input()) 
print("Cool! There are %d lockers and students" % total_lockers)
print("--------------")
sleep(1)
print("How many time do you want the program to run")
input = int(raw_input())
runs = (10 ** input)
print("Awesome! The program will run %d times" % runs)
sleep(0.1)

while i <= runs:
    i = i + 1

    population = range(1,(total_lockers + 1))


    lockers2 = random.sample(population, (total_lockers - 1))

    sumLocker = sum(lockers2)
    sumPopulation = sum(population)

    lastLocker = sumPopulation - sumLocker

    if (lastLocker == total_lockers):
        print("last student got his locker")
        right = right + 1

    else:
        print("last student got a different locker") 


accuracy = (float(right) / float(i)) * 100
accuracy = round(accuracy, 2)

print("-------------") 
print(str(accuracy) + "%")
