# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.




# 时间复杂度O(n^2)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_str = ''
        sub_str = ''
        for c in s:
            if c in sub_str:
                if len(sub_str) > len(max_str):
                    max_str = sub_str
                sub_str = ''
            sub_str += c
        return len(max_str)



# 优化
# 使用滑动窗口和字典来优化这个算法，时间复杂度降低到O(n)
# 时间复杂度O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length