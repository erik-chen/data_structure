"""
    graph的表示法: adjacency matrix / adjacency list
"""
#  adjacency matrix
import numpy as np
adjacency_matrix = np.zeros((7, 7)).astype(float)
adjacency_matrix[0][0] = float('inf')
for i in range(1, 7):
    adjacency_matrix[0][i] = i
    adjacency_matrix[i][0] = i
adjacency_matrix[1][2] = adjacency_matrix[2][1] = 1
adjacency_matrix[1][3] = adjacency_matrix[3][1] = 1
adjacency_matrix[2][3] = adjacency_matrix[3][2] = 1
adjacency_matrix[2][4] = adjacency_matrix[4][2] = 1
adjacency_matrix[5][6] = adjacency_matrix[6][5] = 1
print('adjacency_matrix=\n', adjacency_matrix)

#  adjacency list
adjacency_list = [0]*7
adjacency_list[0] = 'NULL'
adjacency_list[1] = [1, 2, 3, 4]
adjacency_list[2] = [2, 1, 3]
adjacency_list[3] = [3, 1, 2]
adjacency_list[4] = [4, 1]
adjacency_list[5] = [5, 6]
adjacency_list[6] = [6, 5]
print('adjacency_list=\n', adjacency_list)
