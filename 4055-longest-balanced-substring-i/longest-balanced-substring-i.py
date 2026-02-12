class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            freq = [0] * 26
            
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                
                counts = [f for f in freq if f > 0]
                
                if len(set(counts)) == 1:
                    max_len = max(max_len, j - i + 1)
        
        return max_len
