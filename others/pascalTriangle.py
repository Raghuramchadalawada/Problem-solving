#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(1,numRows):
            temp=ans[len(ans)-1]
            app=[1]
            for j in range(1,len(temp)):
                app.append(temp[j-1]+temp[j])
            app.append(1)
            ans.append(app)
        return ans
        
