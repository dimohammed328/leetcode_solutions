import heapq
def prison(n, m, h, v):
    maxHDiff = 1
    maxVDiff = 1
    sortedH = sorted(h)
    sortedV = sorted(v)
    
    if len(h) == 1:
        maxHDiff = 2
    else:
        curr = 2
        for i in range(1,len(sortedH)):
            if sortedH[i] == sortedH[i-1]+1:
                curr += 1
                
            else:
                curr = 2
            maxHDiff = max(maxHDiff, curr)
    if len(v) == 1:
        maxVDiff = 2
    else:
        curr = 2        
        for i in range(1, len(sortedV)):
            if sortedV[i] == sortedV[i-1]+1:
                curr += 1
            else:
                curr = 2
            maxVDiff = max(maxVDiff, curr)
    return maxHDiff*maxVDiff

def teamFormation(score, team_size, k):
    copy = [_ for _ in score]
    prio = []
    mp = {}
    addedFront = 0
    addedBack = 0
    ret = 0
    for i,sc in enumerate(copy):
        if sc in mp:
            heapq.heappush(mp[sc], i)
        else:
            mp[sc] = [i]
    for i in range(k):
        heapq.heappush(prio, -1*copy[i])
        heapq.heappush(prio, -1*copy[-1*i-1])
    for i in range(team_size):
        if len(copy) <= k*2:
            smallest = heapq.nlargest(team_size-i, copy)
            ret += sum(smallest)
            break
        elif 2*k + addedBack + addedFront == len(score):
            ret += -1*sum(heapq.nsmallest(team_size-i, prio))
            break
        else:
            scoreToAdd = heapq.heappop(prio)*-1
            idxToRemove = heapq.heappop(mp[scoreToAdd])
            ret += scoreToAdd
            if idxToRemove < k+addedFront:
                heapq.heappush(prio, -1*copy[k+addedFront])
                addedFront += 1
            else:
                heapq.heappush(prio, -1*copy[(-1*k)-addedBack-1])
                addedBack += 1
    return ret

print(teamFormation([6,18,8,14,10,12,18,9], 8, 3))

