class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        # bucket_0 =[]
        # bucket_1 =[]
        # bucket_2=[]
        # for i in nums:
        #     if i == 0:
        #         bucket_0.append(i)
        #     elif i == 1:
        #         bucket_1.append(i)
        #     else:
        #         bucket_2.append(i)
        # nums.clear()
        # nums_sort = bucket_0 +  bucket_1 +  bucket_2
        # for i in nums_sort:
        #     nums.append(i) 
        
        # count = Counter(nums)
        # nums.clear()
        # for i in range (count[0]):
        #     nums.append(0)
        # for i in range (count[1]):
        #     nums.append(1)
        # for i in range (count[2]):
        #     nums.append(2)

        l = 0
        r = len(nums)-1
        mover = 0
        while mover <= r:
            if nums[mover] ==0:
                nums[mover] , nums[l] = nums[l] , nums[mover]
                l+=1
                mover+=1
            elif nums[mover] == 2:
                nums[mover] , nums[r] = nums[r] , nums[mover]
                r-=1
            else:
                mover+=1
            


                
            
        