class Solution(object):
    def isPalindrome(self, x):
        if str(x)[0] == '-':
            return False
        reverse = int(`x`[::-1])
        if x == reverse:
            return True
        return False

result = Solution()
print result.isPalindrome(-2147483648)