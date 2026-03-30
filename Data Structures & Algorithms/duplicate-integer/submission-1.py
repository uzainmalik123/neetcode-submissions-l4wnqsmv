class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter_list = Counter(nums)

        for num in counter_list:
            if counter_list.get(num, 0) > 1:
                return True
            
        return False