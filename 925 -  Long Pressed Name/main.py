class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        cur = 0
        last = False

        for char in typed:
            if cur == len(name):
                    last = True
                    cur -= 1
            if char != name[cur]:
                if cur == 0:
                    return False
                if char != name[cur-1]:
                    return False
                else:
                    if last:
                        return False
            else:
                cur += 1
        if cur < len(name):
            return False
        return True