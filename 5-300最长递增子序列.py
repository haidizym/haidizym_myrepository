class Solution:  #动态规划，时间复杂度为 O(n2) 
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:return 0

        dp=[1]*n  #dp[i]用来记录到第i个位置的最长递增子序列长度，状态列表初始化

        for right in range(n):  #左右指针遍历
            for left in range(right+1):
                if nums[left]<nums[right]:
                    dp[right]=max(dp[right],dp[left]+1)  #状态转移方程
        return max(dp)
