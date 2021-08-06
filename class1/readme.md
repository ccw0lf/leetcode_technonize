# Class 1 Homework. 
## contexts 
1. BigO 
2. Inplace Swap 
3. Leetcode problem : TwoSum

### Inplace Swap,
``` a =[1,2,3,4,5]
start =0
end= len(a)-1

while start<=end:
    temp = a[start]
    a[start]= a[end]
    a[end]=temp
    start+=1
    end-=1
    print(a)
```


### TwoSum using for 

```
class Solution:
    def twoSum(self, nums, target):
 
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
Solution.twoSum(nums=[2,7,3,6,7],target=6)
```