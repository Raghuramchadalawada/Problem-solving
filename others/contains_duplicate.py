#https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """st=set()
        for i in nums:
            if i in st:
                return True
            st.add(i)
        return False"""
        return not len(set(nums)) == len(nums)
