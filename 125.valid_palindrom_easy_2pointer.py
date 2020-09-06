# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# step 1: clean the string
# method 1: reverse string, then compare: O(N)
# method 2: use two pointers from left and right to compare O(N/2)

# two pointer problem
# TC: O(N)
# SC: O(1)

# Note: 注意 while left < right and not s[left].isalnum():
# 一定要有 left < right 这个条件
class Solution:
    def isPalindrome(self, s: str) -> bool:


        # method 2:

        n = len(s)

        left = 0
        right = n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
