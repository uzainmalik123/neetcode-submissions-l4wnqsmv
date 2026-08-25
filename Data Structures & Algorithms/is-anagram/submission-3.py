class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {i: 0 for i in range(26)}

        for i in range(len(s)):
            map[ord(s[i]) - 97] += 1
            map[ord(t[i]) - 97] -= 1

        return all(value == 0 for value in map.values())