#https://leetcode.com/submissions/detail/575403737/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end=len(nums)
        sm=0
        mx=nums[0]
        for start in range(end):
            sm+=nums[start]
            if sm>0:
                if sm>mx:
                    mx=sm
            else:
                if sm>mx:
                    mx=sm
                sm=0
        return mx
