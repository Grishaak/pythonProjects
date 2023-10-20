class Solution:
    @staticmethod
    def longestCommonPrefix(strs: list[str]) -> str:
        set_list = set()
        string = ""
        count = 0
        x = min(len(el) for el in strs)
        while count < x:
            for element in strs:
                set_list.add(element[count])
            if len(set_list) > 1:
                return string
            else:
                string += set_list.pop()
            count += 1
        return string

print(Solution.longestCommonPrefix(["flower","flow","flight"]))
