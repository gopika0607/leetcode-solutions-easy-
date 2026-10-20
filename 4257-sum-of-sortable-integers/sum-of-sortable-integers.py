from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev = float('-inf')

            for start in range(0, n, k):
                arr = nums[start:start + k]
                m = len(arr)

           
                drops = [
                    i for i in range(m)
                    if arr[i] > arr[(i + 1) % m]
                ]

                if len(drops) > 1:
                    valid = False
                    break

                pivot = (drops[0] + 1) % m if drops else 0
                rotated = arr[pivot:] + arr[:pivot]

                if rotated[0] < prev:
                    valid = False
                    break

                prev = rotated[-1]

            if valid:
                ans += k

        return ans






     
         
        

         
          

       
              
          

             
            
              
              
                

          
             
               

             
        

         

             
               
             

               

       
           

   




 



      
      



           
        
           

               
        
             

                
          
         
            
                 


               
                

        
         

    

    
       

   
            
          

         

            
            
            

             

                
           

                 
                    
                 

            
             
           

        
           

  

        