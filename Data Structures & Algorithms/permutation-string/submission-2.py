class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        arr1, arr2 = [0] * 26, [0] * 26
        l = 0

        for s in s1:
            arr1[ord(s) - ord('a')] += 1

        for r in range(len(s2)):    
            if r - l + 1 > len(s1):
                arr2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            arr2[ord(s2[r]) - ord('a')] += 1

            if arr1 == arr2:
                return True

        return False