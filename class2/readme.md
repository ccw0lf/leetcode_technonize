# Class 2 Homework. 
## contexts 
1. Class 
2. Method
3. Constructor 
4. Leetcode problem , Valid Palindrome

### [Leet code profile ](https://leetcode.com/iamtakdir/)

### Class ,
```class Human :
    def __init__(self,name, age):

        self.name = name
        self.age= age

        print (f" Name is {name} age is  {age}")

h1=Human("Shishir",20)
```


### Valid Palindrome 

```
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
```