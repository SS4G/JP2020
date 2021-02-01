class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])
        totalBoarder = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    totalBoarder += self.calcLandBoarder(R, C, r, c, grid)
        return totalBoarder

    def valid_grid(self, R, C, cord):
        return (0 <= cord[0] <= R - 1) and (0 <= cord[1] <= C - 1)

    def calcLandBoarder(self, R, C, r, c, grid):
        up = (r - 1, c)
        down = (r + 1, c)
        left = (r, c - 1)
        right = (r, c + 1)
        landCnt = 0
        for valid_cord in filter(lambda cord: self.valid_grid(R, C, cord), [up, down, left, right]):
            if grid[valid_cord[0]][valid_cord[1]] == 1:
                landCnt += 1
        return 4 - landCnt
