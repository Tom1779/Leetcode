class MapSum:

    def __init__(self):
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for k in self.map:
            if len(k) >= len(prefix):
                if k[0:len(prefix)] == prefix:
                    total += self.map[k]

        return total



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)