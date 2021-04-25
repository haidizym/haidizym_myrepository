class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1:return s
        ans=s[0]
        dp=[[False]*n for _ in range(n)]#表示以i，j之间的子串是否是回文串
        max_len=1
        cur_len=1

        for right in range(n):
            for left in range(right+1):
                if right-left<2:
                    dp[left][right]=(s[left]==s[right])
                else:
                    dp[left][right]=dp[left+1][right-1] and s[left]==s[right]
                cur_len=right-left+1
                if dp[left][right] and max_len<cur_len:
                    max_len=max(max_len,cur_len)
                    ans=s[left:right+1]
        return ans
