'''
Author: Soufal
Date: 2023-08-08 19:28:37
Description: 
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 类似题26数组的删除重复元素
        if(head == None):
            return None
        slow, fast = head, head
        while(fast != None):
            if(fast.val != slow.val):
                # slow = slow.next
                # slow.val = fast.val
                slow.next = fast
                slow = slow.next

            fast = fast.next
        # 需要断开链表与后面重复元素的链接，返回前面不重复的部分
        slow.next = None
        return head
# @lc code=end

