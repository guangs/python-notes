# https://www.workat.tech/problem-solving/practice/longest-palindrome
# Medium
# ./resources/008-longest-palindrome-substring.png

# https://leetcode.com/problems/longest-palindromic-substring/

# https://www.youtube.com/watch?v=XYQecbcd6_c


def longest_palindrome(s: str) -> str:
    max_len = 0
    max_str = ''
    n = len(s)

    for i in range(n):
        # odd length
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r -l + 1 > max_len:
                max_len = r - l + 1
                max_str = s[l: r+1]
            l -= 1
            r += 1
        # even length
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r -l + 1 > max_len:
                max_len = r - l + 1
                max_str = s[l: r+1]
            l -= 1
            r += 1
    print(max_str)
    return max_str


s1 = "mississippi"
s2 = "avcccvbgf"
s3 = "abcdc"
s4 = "a"
s5 = "abc"

longest_palindrome(s1) # "ississi"
longest_palindrome(s2) # "vcccv"
longest_palindrome(s3) # "cdc"
longest_palindrome(s4) # "a"
longest_palindrome(s5) # "a"