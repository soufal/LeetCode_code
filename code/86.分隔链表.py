'''
Author: Soufal
Date: 2023-08-06 16:35:04
Description: 
'''
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 存放小于x的链表的头结点
        temp1 = ListNode(-1)
        # 存放大于x的链表的头结点
        temp2 = ListNode(-1)

        # 两个指针
        p1 = temp1
        p2 = temp2
        # 遍历原链表的指针p
        p = head
        while(p != None):
            if(p.val >= x):
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # 断开原链表中的每个节点的next指针
            # 如果不断掉将会进入无限循环
            tt = p.next
            p.next = None
            p = tt
            # p = p.next        
        p1.next = temp2.next
        return temp1.next


# @lc code=end

