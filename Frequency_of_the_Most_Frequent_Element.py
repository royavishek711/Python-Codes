# leetcode 1838. Frequency of the Most Frequent Element

def maxFrequency(nums, k):
    nums.sort()
    left, right, total, res=0, 0, 0, 0
    
    
    while(right<len(nums)):
        total+=nums[right]

        while nums[right]*(right-left+1) > total+k:
            total-=nums[left]
            left+=1
        
        res=max(res, right-left+1)
        right+=1
    
    return res

nums=[1,4,8,13]
k=5

print(maxFrequency(nums, k))
