'''
Author: Soufal
Date: 2023-08-08 19:56:00
Description: 
'''
#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = self.removeElement(nums, 0)
        for i in range(temp, len(nums)):
            nums[i] = 0
    def removeElement(self, nums: List[int], val: int) -> int:
        #基于原地去除指定元素0
        if(len(nums) == 0):
            return 0
        slow, fast = 0, 0
        while(fast < len(nums)):
            if(nums[fast] != val):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end

