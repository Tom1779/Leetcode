class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = dict()
        dupes = []

        for path in paths:
            p = path.split()
            p_name = p[0]
            for f in p[1:]:
                f_s = f.split('(')
                f_name = f_s[0]
                content = '(' + f_s[1]
                if not content in files:
                    files[content] = [p_name+'/'+f_name]
                else:
                    files[content].append(p_name+'/'+f_name)

        for v in files.values():
            if len(v) > 1:
                dupes.append(v)

        return dupes
