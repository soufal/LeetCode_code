'''
Author: Soufal
Date: 2023-08-06 16:48:57
Description: 
'''
#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return None
        # 虚拟头结点
        temp = ListNode(-1)
        p = temp
        # 构建优先级队列,将k个链表的头结点加入最小堆
        # 这里构造的堆进存储的是节点的val
        pq = []
        for listi in lists:
            while listi:
                heapq.heappush(pq, listi.val)
                listi = listi.next

        while(pq):
            # 获取最小节点，接到结果链表中
            node = heapq.heappop(pq)
            p.next = ListNode(node)
            p = p.next
        return temp.next

# @lc code=end

