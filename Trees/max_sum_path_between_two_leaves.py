'''
MAXIMUM PATH SUM BETWEEN 2 LEAF NODES:
Given a binary tree in which each node element contains a number. Find the maximum possible sum from one leaf node to another leaf node.

NOTE: Here Leaf node is a node which is connected to exactly one different node.

'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def Util(root,res):
    if root is None:
        return 0
    l=Util(root.left,res)
    r=Util(root.right,res)
    
    if root.left is not None and root.right is not None:
        res[0]=max(res[0],l+r+root.data)
        return max(l,r)+root.data
    if root.left is None:
        return r+root.data
    else:
        return l+root.data

def maxPathSum(root):
    res=[float('-inf')]
    ans=Util(root,res)
    if res[0] != float('-inf'):
        return res[0]
    return ans
   
if __name__ =="__main__":
    root=Node(3)
    root.left=Node(4)
    root.right=Node(5)
    root.left.left=Node(-10)
    root.left.right=Node(4)
    print(maxPathSum(root))
