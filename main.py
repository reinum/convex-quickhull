import time
import numpy as np
from numpy.linalg import norm

points = open("points_10k.txt", "r").read().splitlines()
start_time = time.time()

triangled = []

"""
CONVEX HULL PROBLEM | QUICKHULL
- inspo by devon crawfords school hw kekw

this shit goes in a loop:
- find the lowest X coord
- find the highest X coord
- find the highest/lowest Y coord
    - the furthest away from the Y coordinate relevant to the X coord of the invisible line between 2 furthest away points
    - i mean, trying all of the points should be doable i guess lmao
- make a triangle
- remove all of the points inside the triangle

repeat until all points are deleted or triangled
"""


def calcDistance(p1, p2, p3):
    # thanks stackoverflow stranger

    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)

    if p1[0] == p2[0] and p1[1] == p2[1]:
        raise Exception("Something REALLY shit the fan, Lowest X == Highest X")
    else:
        return norm(np.cross(p2-p1, p1-p3))/norm(p2-p1)


def area(A, B, C):
    # thanks geeksforgeeks

    # converting
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def insideTriangle(Axy, Bxy, Cxy, point):
    # thanks geeksforgeeks

    # Calculate area of triangle ABC
    A = area(Axy, Bxy, Cxy)
    # Calculate area of triangle PBC
    A1 = area(point, Bxy, Cxy)
    # Calculate area of triangle PAC
    A2 = area(Axy, point, Cxy)
    # Calculate area of triangle PAB
    A3 = area(Axy, Bxy, point)
    # Check if sum of A1, A2 and A3
    # is same as A
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


# converting necessary shit
floatedPoints = []
for point in points:
    pointXY = point.split(" ")  # get xy floats
    # converting both coords to floats in 1 line, sick
    pointXY = [float(coor) for coor in pointXY]
    floatedPoints.append(pointXY)

runs = 1
while True:
    thisRun = []
    lowestX, highestX = None, None
    pointIndex = {}
    for point in floatedPoints:
        # if X of this point is lower than the lowest X we found before
        if lowestX == None or point[0] < lowestX:
            lowestX = point[0]
            pointIndex[str(point[0])] = point[1]
        # if X of this point is higher than the highest X we found before
        elif highestX == None or point[0] > highestX:
            highestX = point[0]
            pointIndex[str(point[0])] = point[1]
    if floatedPoints == [] or highestX == -69:
        break
    highestXY = [highestX, pointIndex[str(highestX)]]
    lowestXY = [lowestX, pointIndex[str(lowestX)]]
    # we now have the lowest and highest X i guess
    # now time for the part i dont fucking know how to make
    # calcing distance from a point to the line
    distanceIndex = {}
    largestDistance = -1
    for point in floatedPoints:
        d = calcDistance(lowestXY, highestXY, point)
        if d > largestDistance:
            largestDistance = d
            distanceIndex[str(d)] = point
    furthestPoint = distanceIndex[str(largestDistance)]
    # iterating over points and seeing if they are in the triangle or not
    removePoints = []
    for point in floatedPoints:
        isPointInTriangle = insideTriangle(
            lowestXY, highestXY, furthestPoint, point)
        if isPointInTriangle:
            removePoints.append(point)

    for element in removePoints:
        floatedPoints.remove(element)
    print(
        f"[RUN {str(runs)}] Removed {str(len(removePoints))} point(s) in a hull!")
    print(f"[RUN {str(runs)}]", " | ".join(thisRun))
    print(
        f"[RUN {str(runs)}] Triangle points:", " ".join([str(el) for el in [lowestXY, highestXY, furthestPoint]]))
    runs += 1
    print("##################################################################")

print(floatedPoints)
print("Quickhulled in", int(round((time.time()-start_time)*1000, ndigits=0)), "ms!")
