class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for char in s:
            dict[char] = dict.get(char,0) + 1

        for char in t:
            dict[char] = dict.get(char,0) - 1
                
        for value in dict.values():
            if value != 0:
                return False
            
        return True