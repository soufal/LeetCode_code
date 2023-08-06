#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 让p1指针遍历A再遍历B
        # 让p2指针遍历B后再遍历A，逻辑上两条链表连接在了一起
        # 使得p1和p2同时前进能进入到公共的部分
        p1 = headA
        p2 = headB
        while (p1 != p2):
            # 遍历完A接着遍历B
            if(p1 == None):
                p1 = headB
            else:
                p1 = p1.next
            # 遍历完B，接着遍历A
            if(p2 == None):
                p2 = headA
            else:
                p2 = p2.next
        return p1
# @lc code=end

