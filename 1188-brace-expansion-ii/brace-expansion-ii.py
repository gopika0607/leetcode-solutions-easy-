class Solution:
    def braceExpansionII(self, expression: str):
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    sub, i = parse(i + 1)
                    
                elif expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1
                    continue
                    
                else:
                    sub = {expression[i]}
                    i += 1

          
                current = {
                    a + b
                    for a in current
                    for b in sub
                }

            result.update(current)

         
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)
        