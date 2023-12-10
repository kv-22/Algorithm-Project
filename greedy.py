import numpy as np
from time import time

# to find the distance
def findMinRoute(tsp):
    sum = 0
    counter = 0
    i = 0
    j = 0
    mn = 999999999
    visitedRouteList = {}
    visitedRouteList[0] = 1
    route = [0] *len(tsp)
    while i < len(tsp) and j < len(tsp[i]): 
        if counter >= len(tsp[i]) - 1:
            break
        if j!=i and j not in visitedRouteList:
            if tsp[i][j] < mn:
                mn = tsp[i][j]
                route[counter] = j + 1
        j += 1
        if j == len(tsp[i]):
            sum += mn 
            mn = 999999999 
            visitedRouteList[route[counter] - 1] = 1 
            j = 0 
            i = route[counter] - 1 
            counter += 1
    
    i = route[counter - 1] - 1 
    for  j in range(0, len(tsp)): 
        if i != j and tsp[i][j] < mn: 
            mn = tsp[i][j]
            route[counter] = j + 1 
        
    sum += mn 
    print(sum)

# input for size from user
while True:
    n = int(input("Enter number of cities you want to run the algorithm for (between 2 and 312).\n>>")) # number of nodes/cities
    if 2 <= n <= 312:
        break

# load the distance matrix for the cities
data = np.loadtxt('312.txt', usecols=range(2), max_rows=n) # using numpy to read distances from txt and store in array
distance_matrix = np.zeros((len(data), len(data)))
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        distance = np.linalg.norm(data[i] - data[j])
        distance_matrix[i, j] = distance
        distance_matrix[j, i] = distance 
new_distance_matrix = distance_matrix.round().astype(int)

# calculating the execution time

print("Number of cities: ", n)
start_time = time()
print("Minimum distance: ", end='')
findMinRoute(new_distance_matrix) # function call
end_time = time()
time_taken = (end_time-start_time) * 1000 # convert to milliseconds
print("Time taken in milliseconds by greedy: ", time_taken)
