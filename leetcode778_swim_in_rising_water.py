import heapq
from typing import List
from collections import defaultdict


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        graph = defaultdict(list)
        for row in range(ROWS):
            for col in range(COLS):
                for dr, dc in dirs:
                    nr = row+dr
                    nc = col+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        edge_weight = max(grid[row][col], grid[nr][nc])
                        graph[(row, col)].append(((nr, nc), edge_weight))
        visited = set()
        maxCostSoFar = 0
        current = (0, 0)
        heap = []
        while len(visited) < ROWS*COLS:
            visited.add(current)
            for node, cost in graph[current]:
                if node not in visited:
                    heapq.heappush(heap, (cost, node))
            cost, nextNode = heapq.heappop(heap)
            while nextNode in visited:
                cost, nextNode = heapq.heappop(heap)
            maxCostSoFar = max(maxCostSoFar, cost)
            current = nextNode
            if current == (ROWS-1, COLS-1):
                return maxCostSoFar
        return maxCostSoFar


s = Solution()
grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
    12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
print(s.swimInWater(grid))
