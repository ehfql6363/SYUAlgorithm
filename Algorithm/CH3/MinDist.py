import math

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]


def dist(p1, p2):
    res = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return res


def closestPair(p):
    points = [0,0]
    n = len(p)
    minDist = float("inf")
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = dist(p[i], p[j])
            if d < minDist:
                points[0] = p[i]
                points[1] = p[j]
                minDist = d

    return points, minDist

print(closestPair(p))
