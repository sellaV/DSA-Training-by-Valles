class Solution:
    def numyn(self, k):
        return (ord('A') <= ord(k) <= ord('Z') or
                ord('a') <= ord(k) <= ord('z') or
                ord('0') <= ord(k) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left < right:
            while left < right and not self.numyn(s[left]):
                left += 1
            while left < right and not self.numyn(s[right]):
                right -= 1
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True
