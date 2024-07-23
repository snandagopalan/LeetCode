class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0)+1
        return sorted(nums, key=lambda x: (frequency[x], -x))
        
        
