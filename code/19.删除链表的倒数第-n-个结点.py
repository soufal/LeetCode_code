'''
Author: Soufal
Date: 2023-08-06 17:16:29
Description: 
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 虚拟头结点
        # 作用为防止出现空指针的情况，例如链表总共只有5个节点，此时需要删除倒数第5个节点，
        # 也就是头结点，按照算法逻辑此时应该先找到倒数第6个节点，但该节点不存在，因此需要虚拟头结点
        temp = ListNode(-1)
        temp.next = head
        # 删除倒数第n个节点，需要找到倒数第n+1个节点
        x = find_from_end(temp, n+1)
        # 删除倒数第n个节点
        x.next = x.next.next
        return temp.next

def find_from_end(head: Optional[ListNode], k):
    p1 = head

    # p1先走k步
    for i in range(k):
        p1 = p1.next
    
    p2 = head
    # p1和p2同时走，直到p1到最后
    while p1 != None:
        p2 = p2.next
        p1 = p1.next
    
    # 此时跑p2已指向n-k+1个节点，即倒数dik个节点
    return p2

# @lc code=end

