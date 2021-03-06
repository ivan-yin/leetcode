#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (38.50%)
# Total Accepted:    398.2K
# Total Submissions: 1M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        if x<0 or x%10 == 0:
            return False

        # 字符串的解决方式  
        # rev = str(x)[::-1]
        # if rev != str(x):
        #     return False


        # 不用字符串的解决方式
        div = 0
        while div < x:
            div = int(div*10 + x%10)
            x = int(x/10)

        return (int(div/10) == x) or (div == x)
        

Solution().isPalindrome(121)
