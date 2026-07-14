scoreA = int(input())
scoreB = int(input())
if scoreA > scoreB:
    pointsA = 3
    pointsB = 0
else:
    if scoreA < scoreB:
        pointsA = 0
        pointsB = 3
    else:
        pointsA = 1
        pointsB = 1
    if scoreA == 0:
        pointsB = 1
    else:
        scoreA = 1
print(pointsA)
print(pointsB)
