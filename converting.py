#this is to convert from a dataset consisting of latitude & longtitude to a distance matrix since most big datasets are of similar type
#code from bard but with few additions

import numpy as np

n=312
data = np.loadtxt('312.txt', usecols=range(2), max_rows=n)

# Calculate the distance matrix
distance_matrix = np.zeros((len(data), len(data)))
print(distance_matrix.shape)
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        distance = np.linalg.norm(data[i] - data[j])
        distance_matrix[i, j] = distance
        distance_matrix[j, i] = distance
print("matrix from coordinates with rounding")
print(distance_matrix.round().astype(int))
print("matrix from coordinates without rounding")
print(distance_matrix)
# there are some differences for number like row one last number is 45 but actual matrix they wrote 46, ig its because they said they used "least square fit" and i used round
# distance_matrix = distance_matrix.round().astype(int)