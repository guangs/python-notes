# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# https://www.youtube.com/watch?v=FCbOzdHKW18&t=13s

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



# 我自己的实现，时间复杂度O(n^2)
def solution(s: str) -> int:
    max_len = 0
    c_set = set()
    for left_index in range(len(s)):
        for right_index in range(left_index, len(s)):
            c = s[right_index]
            if c not in c_set:
                c_set.add(c)
            else:
                max_len = max(max_len, len(c_set))
                c_set.clear()
                break
    return max_len

# 优化后时间复杂度O(n)

def solution(s: str) -> int:
    longest = 0
    l = 0
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        sett.add(s[r])
        longest = max(longest, r - l + 1)

    return longest


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