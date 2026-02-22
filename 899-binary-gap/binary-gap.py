class Solution:
    def binaryGap(self, n: int) -> int:
        max_distance = 0
        last_position = -1
        position = 0
        
        while n > 0:
            if n % 2 == 1: 
                if last_position != -1:
                    max_distance = max(max_distance, position - last_position)
                last_position = position
            
            n //= 2
            position += 1
        
        return max_distance
        