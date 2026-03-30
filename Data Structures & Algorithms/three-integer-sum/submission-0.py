class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        i = 0
        j = len(nums) - 1
        k = 0

        nums.sort()

        while i < j:
            while i < j:
                k = -(nums[i] + nums[j])
                if k in nums and nums[i] + nums[j] + k == 0:
                    if nums.index(k) != i and nums.index(k) != j:
                        if sorted([nums[i], nums[j], k]) not in res:
                            res.append(sorted([nums[i], nums[j], k]))
                    elif k == nums[i+1] and i+1 != j:
                        if sorted([nums[i], nums[j], nums[i+1]]) not in res:
                            res.append(sorted([nums[i], nums[j], nums[i+1]]))
                    elif k == nums[j-1] and j-1 != i:
                        if sorted([nums[i], nums[j], nums[j-1]]) not in res:
                            res.append(sorted([nums[i], nums[j], nums[j-1]]))
                j -= 1
            j = len(nums) - 1
            i += 1

        return res