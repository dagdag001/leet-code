class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            complementary = target - nums[i]
            try:
                complementary_index = nums.index(complementary, i+1)
                return [i, complementary_index]
            except ValueError:
                continue
        return []
                



        