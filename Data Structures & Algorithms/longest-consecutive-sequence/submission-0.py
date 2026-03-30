class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        currentSeq = 0
        maxSeq = 0

        for j in range(len(nums)):
            i = nums[j]
            while i in nums:
                currentSeq += 1
                i += 1
            if currentSeq > maxSeq:
                maxSeq = currentSeq
                currentSeq = 0
            else:
                currentSeq = 0

        return maxSeq