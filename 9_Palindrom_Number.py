class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = str(x)
        return n == n[::-1]
        # if n == n[::-1]:
        #     return True
        # else:
        #     return False
