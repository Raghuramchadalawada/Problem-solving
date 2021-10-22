#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        flag=0      
        for i in range(len(nums)):
            if flag==1:
                break
            if target-nums[i] in d:
                for j in d[target-nums[i]]:
                    if j==i:
                        continue
                    else:
                        ans.append(i)
                        ans.append(j)
                        flag=1
        return ans
