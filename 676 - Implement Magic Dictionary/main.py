class MagicDictionary:

    def __init__(self):
        self.magic = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.magic = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.magic:
            if len(word) != len(searchWord):
                continue
            diff = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                return True




        return False
            

        

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)