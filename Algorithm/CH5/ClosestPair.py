import math

def distance(p1, p2):
    result = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return result

def stripCloset(P, d):
    n = len(P)
    dMin = d
    P.sort(key = lambda point: point[1])

    for i in range(n):
        j = i+1

        while j < n and P[j][1] - P[i][1] < dMin:
            dij = distance(P[i], P[j])
            if dij < dMin:
                dMin = dij
            j += 1

    return dMin


def closestpair(P):
    n = len(P)
    minDist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(P[i], P[j])
            if dist < minDist:
                minDist = dist
    return minDist


def closestPairDist(P, n):
    if n <= 3:
        return closestpair(P)

    mid = n//2
    midX = P[mid][0]

    dLeft = closestPairDist(P[:mid], mid)
    dRight = closestPairDist(P[mid+1:], n-mid)
    d = min(dLeft, dRight)

    Pm = []
    for i in range(n):
        if abs(P[i][0] - midX) < d:
            Pm.append(P[i])

    ds = stripCloset(Pm, d)

    return min(d, ds)

p = [(2,3), (12,30), (40, 50), (5,1), (12,10), (3,4)]
p.sort(key = lambda point: point[0])
print(closestPairDist(p, len(p)))

