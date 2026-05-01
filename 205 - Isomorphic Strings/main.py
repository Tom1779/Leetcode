class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_inds = {}
        t_inds = {}

        for i in range(len(s)):
            if not s[i] in s_inds.keys():
                s_inds[s[i]] = t[i]
            if not t[i] in t_inds.keys():
                t_inds[t[i]] = s[i]
            if s_inds[s[i]] != t[i] or t_inds[t[i]] != s[i]:
                return False

        return True