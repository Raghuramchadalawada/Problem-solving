#https://leetcode.com/contest/weekly-contest-291/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n=len(number)
        cur=-1
        for i in range(n-1):
            if number[i]==digit:
                cur=i
                if number[i+1]>digit:
                    return number[:i]+number[i+1:]
        if number[n-1]==digit:
            return number[:n-1]
        else:
            return number[:cur]+number[cur+1:]