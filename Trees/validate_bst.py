#https://leetcode.com/problems/validate-binary-search-tree/

from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        d=deque()
        if root:
            d.append((root,-float("inf"),float("inf")))
        while d:
            node,lb,ub=d.popleft()
            #print(node.val,lb,ub)
            if node.val>=ub or node.val<=lb:
                return False    
            if node.left:
                d.append((node.left,lb,node.val))
            if node.right:
                d.append((node.right,node.val,ub))
        return True 
   
