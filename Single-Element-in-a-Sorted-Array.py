class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = 1
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            try:
                if nums[l] == nums[r]:
                    l+=2
                    r+=2
                else:
                    return nums[l]
            except IndexError:
                return nums[l]
                
                