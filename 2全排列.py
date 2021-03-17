class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def dfs(level): #顺次填n个格子
            if level==n:
                ans.append(nums[:])
                return
            for i in range(level,n):
                nums[level],nums[i]=nums[i],nums[level]
                dfs(level+1)
                nums[level],nums[i]=nums[i],nums[level]
        dfs(0)
        return ans
