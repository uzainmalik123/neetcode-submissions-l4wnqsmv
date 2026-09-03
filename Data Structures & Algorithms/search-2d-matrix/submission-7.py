class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2

            print(matrix[mid])

            for i in matrix[mid]:
                if i == target:
                    return True
                elif i > target:
                    r = mid - 1
                else: 
                    l = mid + 1
            
        return False
                
