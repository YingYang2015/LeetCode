
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# method: 2 pointers, then have a is_palindrome function to test sub-string every time
# TC: O(N)
# SC: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s1):
            n = len(s1)
            left = 0
            right = n- 1

            while left < right:
                if s1[left].lower() != s1[right].lower():
                    return False
                left += 1
                right -= 1

            return True

        n = len(s)
        left = 0
        right = n - 1

        while left < right:
            if s[left].lower() != s[right].lower():
                return is_palindrome(s[left + 1:right + 1]) or is_palindrome(s[left:right])

            left += 1
            right -= 1

        return True


def validPalindrome_test():
    s = Solution()
    assert s.validPalindrome('') == True
    assert s.validPalindrome('anan') == True
    assert s.validPalindrome('anfdfs') == False
    assert s.validPalindrome('ana') == True

if __name__ == '__main__':
    validPalindrome_test()