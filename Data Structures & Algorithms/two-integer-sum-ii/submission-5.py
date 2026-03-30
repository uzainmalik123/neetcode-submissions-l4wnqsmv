class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = 1

        while len(numbers) > j != i:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif j == len(numbers) - 1 and i != len(numbers) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        
        return []



