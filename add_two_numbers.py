# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def makeNumber(linked):
            ret_list = []
            while linked != None:
                ret_list.append(linked.val)
                linked = linked.next
            string = ""
            for digit in ret_list:
                string = string + str(digit)
            string = string[::-1]
            return string
        num1 = makeNumber(l1)
        num2 = makeNumber(l2)
        result = int(num1) + int(num2)
        result_list = []
        for digit in str(result):
            result_list.append(int(digit)) 
        return result_list[::-1]
            
        
