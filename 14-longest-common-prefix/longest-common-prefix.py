class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix_hash = {}
        prefix_index = 0
        shortest = len(min(strs,key=len))
        for i in strs:
            for j in range(len(i)):
                if j not in common_prefix_hash:
                    common_prefix_hash[j] = [i[j]]
                else:
                    common_prefix_hash[j].append(i[j])
        for i in common_prefix_hash:
            found = False
            common_len = len(common_prefix_hash[0])
            if len(common_prefix_hash[i]) < common_len:
                prefix_index = i - 1
                break
            if i >= shortest:
                prefix_index = i - 1
                found = True
                break
            for j in range(len(common_prefix_hash[i])):
                if common_prefix_hash[i][j] == common_prefix_hash[i][0]:
                    pass
                else:
                    prefix_index = i-1
                    found = True
                    break
            if found:
                break
            prefix_index = i
        if prefix_index > -1:
            return (strs[0][:prefix_index+1])
        else:
            return ""