from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        for i, freq in count.items():
            if freq > (len(nums) /3):
                res.append(i)
        return res

        