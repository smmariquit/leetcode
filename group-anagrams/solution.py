class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            new_str = "".join(sorted(word))
            if new_str in groups:
                groups[new_str].append(word)
            else:
                groups[new_str] = [word]
        return groups.values()
                



