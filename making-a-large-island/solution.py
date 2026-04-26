class Solution(object):
    def largestIsland(self, grid):
        """
      :type grid: List[List[int]]
      :rtype: int
        """
        n = len(grid)

        def dfs(r, c, island_id):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c]!= 1:
                return 0
            
            grid[r][c] = island_id # Mark the cell with island id
            count = 1
            count += dfs(r + 1, c, island_id)
            count += dfs(r - 1, c, island_id)
            count += dfs(r, c + 1, island_id)
            count += dfs(r, c - 1, island_id)
            return count

        island_sizes = {}
        island_id = 2  # Start island IDs from 2 (1 is for original 1s)
        max_island = 0

        # Find initial island sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    max_island = max(max_island, size)
                    island_id += 1

        # Check for potential larger islands by changing a 0 to 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    adjacent_islands = set()  # Use a set to avoid double-counting
                    
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            adjacent_islands.add(grid[nr][nc])

                    new_island_size = 1  # Start with the newly created 1
                    for island_id in adjacent_islands:
                        new_island_size += island_sizes[island_id]

                    max_island = max(max_island, new_island_size)
        
        return max_island