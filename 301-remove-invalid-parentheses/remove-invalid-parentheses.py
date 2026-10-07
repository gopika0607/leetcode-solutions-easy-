from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        queue = deque([s])
        visited = {s}
        result = []

        while queue:
            current = queue.popleft()

            if self.isValid(current):
                result.append(current)

     
            if result:
                continue

            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result

    def isValid(self, s):
        balance = 0

        for ch in s:
            if ch == '(':
                balance += 1

            elif ch == ')':
                balance -= 1

                if balance < 0:
                    return False

        return balance == 0


  
       

  
   

    

      
         

        
          
                

        
          


           
              

            

          

                
   

     

        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1

               
                  

       
              



        