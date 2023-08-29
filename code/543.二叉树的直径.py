#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, max_diameter=0) -> None:
        self.max_diameter = max_diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 每一条二叉树的“直径”长度，就是一个节点的左右子树的最大深度之和
        # 对每一个节点计算直径，求最大直径
        self.traverse(root)
        return self.max_diameter
    
    #遍历二叉树
    def traverse(self, root):
        if(root==None):
            return
        # 对每个节点计算直径
        left_max = self.max_depth(root.left)
        right_max = self.max_depth(root.right)
        my_diameter = left_max + right_max
        self.max_diameter=max(self.max_diameter, my_diameter)

        self.traverse(root.left)
        self.traverse(root.right)

    # 计算二叉树的最大深度
    def max_depth(self, root):
        if(root==None):
            return 0
        left_max=self.max_depth(root.left)
        right_max = self.max_depth(root.right)
        return 1+max(left_max, right_max)
# @lc code=end

