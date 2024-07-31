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
# 递归的思想--自顶向下的解法
# class Solution:
#     def fib(self, n: int) -> int:
#         # if(n == 0):
#         #     return 0
#         # if(n == 1 or n == 2):
#         #     return 1
#         # return self.fib(n - 1) + self.fib(n - 2)
#         # 初始化备忘录全为0
#         memo = [0] * (n+1)

#         return self.dp(memo, n)
    
#     def dp(self, memo, n) -> int:
#         # base case
#         if(n == 0 or n == 1):
#             return n
#         # 检查是否已经计算过
#         if(memo[n]):
#             return memo[n]
#         # 更新备忘录
#         memo[n] = self.dp(memo, n-1) + self.dp(memo, n-2)
#         return memo[n]

# 迭代（递推）的解法---自底向上的解法
# class Solution:
#     def fib(self, n: int) -> int:
#         dp = []
#         if(n == 0 or n == 1):
#             return n
#         dp.append(0)
#         dp.append(1)
#         # 状态转移
#         for i in range(2, n+1):
#             temp = dp[i-1] + dp[i-2]
#             dp.append(temp)
#         return dp[n]

# 可以只需要记录前两种状态即可
class Solution:
    def fib(self, n: int) -> int:
        dp = []
        if(n == 0 or n == 1):
            return n
        dp.append(0)
        dp.append(1)
        # 状态转移
        i = 2
        while i <= n:
            temp = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], temp
            i += 1
        return dp[1]
# @lc code=end

