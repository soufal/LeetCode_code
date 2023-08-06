'''
Author: Soufal
Date: 2023-08-06 17:33:24
Description: 
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            # 有环
            if(fast == slow):
                break
        # 无环直接返回
        if (fast == None or fast.next == None):
            return None
        
        # slow节点重新指向头结点，找环起点
        slow = head
        # 快慢指针同时前进，相交点就是环起点
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return slow
        
# @lc code=end

