'''
Author: Soufal
Date: 2023-08-08 19:17:50
Description: 
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        slow, fast = 0, 0
        while(fast < len(nums)):
            if(nums[slow] != nums[fast]):
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
# @lc code=end

