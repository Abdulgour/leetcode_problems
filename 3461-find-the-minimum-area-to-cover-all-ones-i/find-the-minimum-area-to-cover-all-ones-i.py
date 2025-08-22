class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            if 1 in grid[i]:
                a=i
                break
        for i in range(n-1,-1,-1):
            if 1 in grid[i]:
                b=i
                break
        Min=m
        Max=0
        for j in range(a,b+1):
            for k in range(m):
                if grid[j][k]==1:
                    Max=max(k,Max)
                    Min=min(k,Min)
        return (b-a+1)*(Max-Min+1)