import math
from typing import List
def tan(x,y):
    deg = math.degrees(math.atan2(x,y))
    if deg < 0:
        return(-1*deg+90)
    else:
        return((90 - deg)%360)
def visiblePoints(points, angle, location):
    if len(points) == 1:
        return(1)
    maxCount = 1
    angleList = [[x-location[0], y - location[1]] for x,y in points if (x-location[0] != 0 or y-location[1]!=0)]
    originPoints = len(points)-len(angleList)
    if len(angleList) == 0:
        return(originPoints)
    angleList = [tan(x,y) for x,y in angleList]
    angleList = sorted(angleList)
    i = 0
    lastElem = angleList[-1]
    while angleList[i]+360-lastElem <= angle:
        angleList.append(angleList[i]+360)
        i += 1
    i = 0
    j = 1
    while j < len(angleList):
        while angleList[i] + angle < angleList[j]:
            i += 1
        if j == len(angleList)-1:
            maxCount = max(maxCount, j-i+1)
            break
        else:
            while j < len(angleList)-1 and angleList[j+1]-angleList[i] <= angle:
                j += 1
            if j == i:
                i+=1
                j+=1
            else:
                maxCount = max(maxCount, j-i+1)
                j+=1
    return(maxCount+originPoints)

    print(angleList)
visiblePoints([[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]],0,[1,1])
    