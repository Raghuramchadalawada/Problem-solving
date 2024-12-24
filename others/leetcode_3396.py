#https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
class solution:
    def minimumOperations(self, array: List[int]) -> int:
        n = len(array)
        uni = len(set(array))
        count=0
        while n!=uni and n>0:
            if 0<uni<3:
                    count+=1
                    break
            elif len(array)>2:
                array = array[3:]
                n = len(array)
                uni = len(set(array))
                count+=1
        return count
        
