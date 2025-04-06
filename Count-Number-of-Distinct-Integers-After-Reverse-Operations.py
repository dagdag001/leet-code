class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverseNums = []
        for i in nums:
            reverseNums.append(int(str(i)[::-1]))
        nums = nums + reverseNums
        return len(set(nums))