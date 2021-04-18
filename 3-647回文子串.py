class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]#dp[i][j] 表示 s[i...j]s[i...j] 是否为回文子串。
        ans = 0
        for k in range(n):
            # i+k<n => i<n-k
            #根据递推公式, 右侧的横纵坐标之差更小, 所以遍历的时候可以按照 k=j-ik=j−i 从小到大遍历
            for i in range(n-k):
                j=i+k
                if k==0: 
                    dp[i][j] = True
                elif k==1:
                    dp[i][j] = s[i]==s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j]: ans+=1
        return ans
