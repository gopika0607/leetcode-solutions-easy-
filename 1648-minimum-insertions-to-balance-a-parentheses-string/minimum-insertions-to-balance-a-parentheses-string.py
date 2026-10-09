class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open_count = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    ans += 1

                if i + 1 < len(s) and s[i + 1] ==')':
                    i += 1
                else:
                    ans += 1

            i += 1
        ans += open_count * 2
        return ans
  
        