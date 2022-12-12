class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = ["(","{","["]
        pairs = {'(':')','[':']','{':'}'}
        stack = []
        
        if len(s) <= 1:
            return False
        
        for p in s:
            if p in opening:
                stack.append(p)
                print(len(stack))
               
            else:
                if len(stack) > 0:
                    if pairs[stack.pop()] == p:
                        print(pairs[stack.pop()] )
                        print(p)
                        continue
                    else:
                        return False
                else:
                    return False 
    
        if len(stack) != 0:
            return False
        else:
             return True      

                

         

mine = Solution()

print(mine.isValid("(]"))

# pairs = {'(':')','[':']','{':'}'}

# print(pairs['('])