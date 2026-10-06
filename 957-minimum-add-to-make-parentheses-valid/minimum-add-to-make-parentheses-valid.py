class Solution:
    def minAddToMakeValid(self, s):
        open_count = 0
        answer = 0

        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    answer += 1

        return answer + open_count
      
             


                 
                     
                  


                                                                                                          
                       
                                                                        
                                                                                                                                                                        

  

      

       
      
              
     
                
                  
          
                 
      

        