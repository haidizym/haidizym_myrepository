class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        left=right=0
        while right<n:
            if nums[right]!=nums[left]:
                left+=1
                nums[left]=nums[right]
            right+=1
        return left+1
