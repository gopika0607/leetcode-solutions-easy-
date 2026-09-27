class Solution:
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch != ')':
                stack.append(ch)

            else:
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()   # remove '('

                stack.extend(temp)

        return ''.join(stack)
        