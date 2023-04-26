#Question link - https://www.codingninjas.com/codestudio/problems/frog-jump_3621012

#recursive solution
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    if n<=1:
        return 0
    else:
        oneStep=abs(heights[n-1]-heights[n-2])
        if n>2:
            twoStep = abs(heights[n-1]-heights[n-3])
        else:
            twoStep = sys.maxsize
        # print("n =",n," one = ",oneStep,"two = ",twoStep)
        return min(oneStep+frogJump(n-1,heights),
                    twoStep+frogJump(n-2,heights))
                    
                    
                    
                    
#memoisation
def sol(n: int, heights: List[int], dp=List[int]) -> int:

    # Write your code here.
    if n<=1:
        return 0
    elif dp[n-1]!=-1:
        return dp[n-1]
    else:
        oneStep=abs(heights[n-1]-heights[n-2])
        if n>2:
            twoStep = abs(heights[n-1]-heights[n-3])
        else:
            twoStep = sys.maxsize
        # print("n =",n," one = ",oneStep,"two = ",twoStep)
        dp[n-1] = min(oneStep+sol(n-1,heights,dp),
                    twoStep+sol(n-2,heights,dp))
        return dp[n-1]

def frogJump(n: int, heights: List[int]) -> int:
    dp=[-1 for i in range(n)]
    return sol(n,heights,dp)
    
#Dynamic Prograamming
def frogJump(n: int, heights: List[int]) -> int:
    v1=0
    v2=abs(heights[1]-heights[0])
    for i in range(2,n):
        temp=min(v1+abs(heights[i]-heights[i-2]),v2+abs(heights[i]-heights[i-1]))
        v1=v2
        v2=temp
    return v2
