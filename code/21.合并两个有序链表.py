'''
Author: Soufal
Date: 2023-08-06 16:09:02
Description: 
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        p = temp
        p1 = list1
        p2 = list2

        while(p1 != None and p2 != None):
            # 比较p1和p2 将小的接到p指针
            if(p1.val > p2.val):
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        if(p1 != None):
            p.next = p1
        if(p2 != None):
            p.next = p2
        return temp.next
# @lc code=end

