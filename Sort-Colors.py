class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        bucket_0 =[]
        bucket_1 =[]
        bucket_2=[]
        for i in nums:
            if i == 0:
                bucket_0.append(i)
            elif i == 1:
                bucket_1.append(i)
            else:
                bucket_2.append(i)
        nums.clear()
        nums_sort = bucket_0 +  bucket_1 +  bucket_2
        for i in nums_sort:
            nums.append(i) 
        
                
            
        