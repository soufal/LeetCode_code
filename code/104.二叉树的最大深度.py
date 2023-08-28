'''
Author: Soufal
Date: 2023-08-28 15:30:32
Description: 
'''
#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遍历思路的解法
# class Solution:
#     def __init__(self, res=0, depth=0) -> None:
#         # 记录最大深度
#         self.res = res
#         # 记录遍历到的节点的深度
#         self.depth = depth

#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # 遍历一遍二叉树，用一个外部变量记录每个节点所在的深度
#         # 取最大值就是最大深度
#         # 二叉树遍历框架
#         self.traverse(root)
#         return self.res
    
#     def traverse(self,root: Optional[TreeNode]) -> None:
#         if(root == None):
#             return
#         # 前序位置
#         self.depth += 1
#         # 到达叶子节点，更新最大深度
#         if((root.left == None) and (root.right == None)):
#             self.res = max(self.res, self.depth)
#         # 递归左右子树
#         self.traverse(root.left)
#         self.traverse(root.right)
#         # 后序位置--左右之树均遍历结束
#         self.depth -= 1

# 分解问题的解法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        # 利用定义，计算左右之树的最大深度
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 整棵树的最大深度等于左右子树的最大深度取最大值
        # 然后再加上根节点自己
        res = max(leftMax, rightMax) + 1
        return res



# @lc code=end

