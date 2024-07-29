'''
Author: Soufal
Date: 2024-07-29 16:38:29
Description: 
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # if(n == 0):
        #     return 0
        # if(n == 1 or n == 2):
        #     return 1
        # return self.fib(n - 1) + self.fib(n - 2)
        # 初始化备忘录全为0
        memo = [0] * (n+1)

        return self.dp(memo, n)
    
    def dp(self, memo, n) -> int:
        # base case
        if(n == 0 or n == 1):
            return n
        # 检查是否已经计算过
        if(memo[n]):
            return memo[n]
        # 更新备忘录
        memo[n] = self.dp(memo, n-1) + self.dp(memo, n-2)
        return memo[n]
        
# @lc code=end

