def numberOfBoomerangs(points) -> int:


        def sqrdis(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        import collections
        dic1 = collections.defaultdict(set)
        dic2 = collections.defaultdict(int)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dic1[(sqrdis(points[i], points[j]))].add(direc(points[i], points[j]))
                dic2[(sqrdis(points[i], points[j]), direc(points[i], points[j]))] += 1
        res = 0
        for i in dic1:
            K = 0
            for j in dic1[i]:
                k = dic2[i, j]
                K += k
                # if dic2[i, j] >= 2:
                #     res -= k * (k - 1)
            if K > 1:
                res += K * (K - 1)
        return res


print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))
