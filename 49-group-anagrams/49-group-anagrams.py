class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')] += 1
            if tuple(key) in res:
                res[tuple(key)].append(s)
            else:
                res[tuple(key)] = [s]
        
        return res.values()
                
            
        