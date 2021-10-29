#https://leetcode.com/problems/number-of-islands/


class Solution:
    def dfs(self,grid,i,j):
        grid[i][j]='2'
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        for ind in direction:
            x,y=i+ind[0],j+ind[1]
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]):
                if grid[x][y]=='1':
                    self.dfs(grid,x,y)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    res+=1
        return res
