class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,num in enumerate(nums):
            if num in a:
                return [i, a[num]]
            a[target-num] = i


        