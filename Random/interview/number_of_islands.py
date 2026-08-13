"""
DFS, BFS
Bloomberg Medium
"""

from collections import deque # BFS uses a queue

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1

                    dfs(r, c)

        return island_count
    
    # Time & space complexity: O(m * n)

    def numIslandsBfs(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1

                    queue = deque([(r, c)])
                    grid[r][c] = "0"

                    while queue:
                        curr_r, curr_c = queue.popleft()

                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = curr_r + dr, curr_c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                queue.append((nr, nc))
                                grid[nr][nc] = "0"

        return island_count
