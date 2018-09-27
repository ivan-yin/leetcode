#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.43%)
# Total Accepted:    480.7K
# Total Submissions: 2M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            strx = list(str(x))[::-1]
            print(strx)
            data = int(''.join(strx).replace('-', '', 1))
            rd = -data
            if rd <= -2147483648:
                return 0
            return rd
        
        strx = list(str(x))[::-1]
        print(strx)
        data = int(''.join(strx))
        maxvalue = 2147483647
        if data > maxvalue:
            return 0
        return data
        
        

Solution().reverse(-231)
