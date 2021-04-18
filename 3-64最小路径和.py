class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if m==0 or n==0: return 0
        if m==1 or n==1: return sum(sum(i)for i in grid)

        dp=[[0]*n for _ in range(m)] #表示第i行第j列位置结尾的路径最小和
        dp[0][0]=grid[0][0]

        for i in range(1,m):dp[i][0]=dp[i-1][0]+grid[i][0] #填好边界条件
        for j in range(1,n):dp[0][j]=dp[0][j-1]+grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                    dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
                    #状态转移方程，第i行第j列结尾可以来自上方或左方，取和最小者
        
        return dp[-1][-1]
