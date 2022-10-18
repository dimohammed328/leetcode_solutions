numSet = set(range(1, 16))
squares = set([1, 4, 9, 16, 25, 36])
solution = []
prev = False


def ss(prev=None):
    if len(numSet) == 0:
        print(solution)
    for num in numSet:
        if prev is None or num + prev in squares:
            solution.append(num)
            numSet.remove(num)
            ss(prev=num)
            numSet.add(num)
            solution.pop()


ss()
