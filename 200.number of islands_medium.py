# 200. Number of Islands

# 问题的意思：
# 所有能连在一起的 1 可以看成一个island，如果上下所有都是0的时候，island就形成了
# 问题是找到有几个islands

# Solution:
# 用DFS： 意思就是，从每个点出发，上下左右一直找1，有1就给赋值为0，没有了就结束了，这就是一个island
#

# TC：O(n*m)
# SC：worst case : O(n*m) in case that the grid map is filled with lands where DFS goes by n*m deep


class Solution:
    def dfs(self, grid, r, c):
        # 赋值为0，所以下面的循环再找的时候就不会再找他了
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands