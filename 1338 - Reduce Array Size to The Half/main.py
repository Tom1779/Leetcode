class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        num_count = dict()

        for n in arr:
            if not n in num_count:
                num_count[n] = 1
            else:
                num_count[n] += 1

        num_count = dict(sorted(num_count.items(), key=lambda item: item[1], reverse=True))
        print(num_count)

        total = 0
        min_rem = 0
        for n in num_count:
            if total >= len(arr)/2:
                break
            total += num_count[n]
            min_rem += 1

        return min_rem
