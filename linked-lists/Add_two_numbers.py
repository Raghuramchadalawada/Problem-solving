# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        tail = None
        carry = 0
        val_sum = 0
        it1 = l1
        it2 = l2
        while it1 and it2:
            temp = ListNode()
            val_sum = it1.val +it2.val+carry
            print("val_sum:",val_sum )
            if val_sum>9:
                temp.val = val_sum%10
                carry = val_sum//10
                print("enteered: ", temp.val, carry)
            else:
                temp.val = val_sum
                carry = 0
            if ans is None:
                ans = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next
            it1 = it1.next
            it2 = it2.next

        while it1:
            temp = ListNode()
            val_sum = it1.val+carry
            if val_sum >9:
                temp.val = val_sum%10
                carry = val_sum//10
            else:
                temp.val = val_sum
                carry = 0
            if ans is None:
                ans = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next
            it1 = it1.next

        while it2:
            temp = ListNode()
            val_sum = it2.val+carry
            if val_sum >9:
                temp.val = val_sum%10
                carry = val_sum//10
            else:
                temp.val = val_sum
                carry  = 0
            if ans is None:
                ans = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next
            it2 = it2.next
        
        if carry == 1:
            temp = ListNode()
            temp.val = carry
            tail.next = temp

        return ans

        

