#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 以s[i]为中心的最长回文子串
            s1 = self.palindrome(s, i, i)
            # 以s[i]和s[i+1]为中心的最长回文子串
            s2 = self.palindrome(s, i, i+1)
            # res=logest(res, s1, s2)
            if(len(res) < len(s1)):
                res = s1
            if(len(res) < len(s2)):
                res = s2
        return res
        
    def palindrome(self, s: str, l: int, r: int) -> str:
        # 在s中寻找以s[l]和s[r]为中心的最长回文串
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
# @lc code=end

