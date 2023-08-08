'''
Author: Soufal
Date: 2023-08-08 19:41:51
Description: 
'''
#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (len(nums) == 0):
            return 0
        slow, fast = 0, 0
        while(fast < len(nums)):
            if(nums[fast] != val):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

        
# @lc code=end

