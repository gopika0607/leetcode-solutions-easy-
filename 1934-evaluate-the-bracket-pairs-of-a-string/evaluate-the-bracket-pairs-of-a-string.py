class Solution:
    def evaluate(self, s, knowledge):

        d = {}

        for key, value in knowledge:
            d[key] = value

        ans = ""
        i = 0

        while i < len(s):

            if s[i] == '(':
                i += 1
                key = ""

                while s[i] != ')':
                    key += s[i]
                    i += 1

                if key in d:
                    ans += d[key]
                else:
                    ans += "?"

            else:
                ans += s[i]

            i += 1

        return ans