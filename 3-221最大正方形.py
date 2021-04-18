class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if(not matrix):
            return 0
        m=len(matrix)
        n=len(matrix[0])
        res=0
        dp=[[0]*(n+1) for _ in range(m+1)]#dp[i][j]表示以第ii行，第jj列处为右下角的最大正方形的边长。
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(matrix[i-1][j-1]=="1"):
                    #若当前位置为11，则此处可以构成的最大正方形的边长，是其正上方，左侧，和左上界三者共同约束的，且为三者中的最小值加1。
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    res=max(dp[i][j],res)
        return res*res
