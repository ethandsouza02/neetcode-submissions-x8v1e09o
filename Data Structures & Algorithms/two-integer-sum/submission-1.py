class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - nums[i]

            if complement in counter:
                return[counter[complement],i]

            counter[num] = i
        