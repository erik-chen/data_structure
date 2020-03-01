def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    import numpy as np
    matrix = np.array(matrix)
    m, n = np.shape(matrix)
    print(n)
    if m > n:
        matrix = matrix.T
    y = [int((n-1)*i/(m-1))for i in range(m)]
    '''
    m-1
    '''
    lis = [matrix[i][y[i]] for i in range(m)]
    print(lis)

    def find(target, lis):
        m = len(lis)
        p = (m + 1)//2-1
        if lis[p] == target:
            return True
        elif lis[p] > target:



    if p == target:
        return True
    eli









print(searchMatrix([
  [1,   4,  7, 11, 15, 16],
  [2,   5,  8, 12, 19, 20],
  [3,   6,  9, 16, 22, 23],
  [10, 13, 14, 17, 24, 25],
  [18, 21, 23, 26, 30, 31]
], 9))