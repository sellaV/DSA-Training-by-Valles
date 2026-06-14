class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            total = 0
            for char in word:
                num = ord(char) - ord('a')
                total += weights[num]
            mod = total % 26
            result.append(chr((ord('z')-mod)))
        return ''.join(result)
