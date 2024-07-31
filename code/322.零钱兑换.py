#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    # 自顶向下的解法
    # memo = []
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # 初始化备忘录为一个不会被取到的特殊值，代表还未被计算
    #     self.memo = [-666] * (amount+1)
    #     return self.dp(coins, amount)
        
    # def dp(self, coins: List[int], amount: int) -> int:
    #     if(amount == 0):
    #         return 0
    #     if(amount < 0):
    #         return -1

    #     # 查备忘录，防止重复计算
    #     if(self.memo[amount] != -666):
    #         return self.memo[amount]

    #     # 定义结果为一个极大值
    #     res = float('inf')
    #     for coin in coins:
    #         #计算子问题的答案
    #         sub_problem = self.dp(coins, amount - coin)
    #         # 子问题无解则跳过
    #         if(sub_problem == -1):
    #             continue
    #         # 在子问题中选择最优解，然后加一
    #         res = min(res, sub_problem + 1)
        
    #     # 把计算结果存到备忘录中
    #     self.memo[amount] = res if res != float('inf') else -1
    #     return self.memo[amount]

    #自底向上的解法：
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp数组的定义：当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出。
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # 外层for循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层for循环在求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if (i - coin < 0):
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if(dp[amount]!=amount + 1) else -1

# @lc code=end

