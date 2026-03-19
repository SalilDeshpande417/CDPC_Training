class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = abs(x)
        rev = 0 
        
        while n != 0:
            rem = n % 10
            n = n // 10
            rev = rev * 10 + rem
        
        if x < 0:
            return False
        
        if rev == x:
            return True
        else:
            return False 
s = Solution()
print(s.isPalindrome(121))   # Expected: True
print(s.isPalindrome(-121))  # Expected: False 