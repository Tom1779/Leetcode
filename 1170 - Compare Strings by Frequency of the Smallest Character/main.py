class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for query in range(len(queries)):
            queries[query] = "".join(sorted(queries[query], key=str.lower))
            queries[query] = queries[query].count(queries[query][0])

        for word in range(len(words)):
            words[word] = "".join(sorted(words[word], key=str.lower))
            words[word] = words[word].count(words[word][0])

        words.sort(reverse=True)

        NSBF = []

        for query in queries:
            total = 0
            for word in words:
                if word > query:
                    total += 1
            NSBF.append(total)

        return NSBF