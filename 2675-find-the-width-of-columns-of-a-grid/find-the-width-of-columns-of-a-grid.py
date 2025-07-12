class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n= len(grid), len(grid[0])
        width = [0]*n
        for i in range(n):
            for j in range(m):
                wid=len(str(abs(grid[j][i])))
                if grid[j][i]<0:
                    wid+=1
                width[i]=max(width[i],wid)
        return width