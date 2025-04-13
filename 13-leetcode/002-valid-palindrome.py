# Valid Palindrome
# Easy - https://leetcode.com/problems/valid-palindrome/description/


# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.





class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. 将字符串转换为小写
        # 2. 使用filter函数，过滤出字母和数字
        # 3. 使用join函数，将过滤出来的字符拼接成字符串
        # 4. 判断字符串是否等于字符串的反转
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        return s == s[::-1]




class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 将字符串转换为小写
        s = s.lower()
        
        # 初始化左右指针
        left, right = 0, len(s) - 1
        
        while left < right:
            # 移动左指针，跳过非字母数字字符
            while left < right and not s[left].isalnum():
                left += 1
            # 移动右指针，跳过非字母数字字符
            while left < right and not s[right].isalnum():
                right -= 1
            # 比较左右指针指向的字符
            if s[left] != s[right]:
                return False
            # 移动左右指针
            left += 1
            right -= 1
        
        return True