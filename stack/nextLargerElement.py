'''Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.'''



def nextLargerElement(arr,n):
    d=[]
    ans=[-1]*n
    for i in range(n):
        while d:
            if d[-1][0]<arr[i]:
                ans[d.pop()[1]]=arr[i]
            else:
                break
        d.append((arr[i],i))
    return ans
if __name__=='__main__':
    arr=list(map(int,input().split()))
    print(nextLargerElement(arr,len(arr)))
