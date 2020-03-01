def maximumNumberOfOnes(width: int, height: int, sideLength: int, maxOnes: int):
    import numpy as np
    import collections
    grid = np.ones((height, width)).astype(int)*maxOnes
    grid2 = np.zeros((height, width)).astype(int)

    dic = collections.defaultdict(set)
    for i in range(height):
        for j in range(width):
            grid2[i][j] = (min(i+sideLength-1, height-1)-max(i-sideLength+1, 0) + 1) *\
                         (min(j + sideLength - 1, width - 1) - max(j - sideLength + 1, 0) + 1)
            dic[grid2[i][j]].add((i, j))
    not_good = set()
    res = 0

    print(grid)
    for i in sorted(list(dic)):
        for j in dic[i]:
            if j not in not_good:
                res += 1
                for k in range(max(j[0]-sideLength+1, 0), min(j[0]+sideLength-1, height-1) + 1):
                    for l in range(max(j[1]-sideLength+1, 0), min(j[1]+sideLength-1, width-1) + 1):
                        grid[k][l] -= 1
                        if grid[k][l] == 0:
                            for m in range(max(k - sideLength + 1, 0), min(k + sideLength - 1, height - 1) + 1):
                                for n in range(max(l - sideLength + 1, 0),
                                               min(l + sideLength - 1, width - 1) + 1):
                                    not_good.add((m, n))

    return res















print(maximumNumberOfOnes(width = 3, height = 3, sideLength = 2, maxOnes = 1))