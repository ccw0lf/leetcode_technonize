import re

class Solution:



    def isPalindrome(s):
        s = s.lower()
        s = re.sub(r'[\W_]', "", s)
        
        start = 0
        end = len(s)-1
        
        while start <= end:
            if s[start] != s[end]:

                print(False)
                return False
            start += 1
            end -= 1
        print (True)
        return True
        

s1 =Solution.isPalindrome(" A man, a plan, a canal: Panama")
s2 =Solution.isPalindrome("ab_a")