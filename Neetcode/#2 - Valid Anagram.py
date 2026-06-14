class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        
        for char_t in t:
            if char_t not in char_count:
                return False
            else:
                char_count[char_t] -= 1
                if char_count[char_t] < 0:
                    return False
        return True
