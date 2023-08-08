#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 利用双指针-左右指针技巧，类似二分查找的方法
        left, right = 0, len(numbers)-1
        while(left <= right):
            sum_lf = numbers[left] + numbers[right]
            if(sum_lf == target):
                return [left+1,right+1]
            elif(sum_lf < target):
                left += 1
            elif(sum_lf > target):
                right -= 1
        return [-1, -1]
                

# @lc code=end

