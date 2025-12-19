class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True)
        cur = 0
        time = []
        used = []
        while cur < 4:
            found = False
            for num in range(len(arr)):
                if num in used:
                    continue
                if cur == 0:
                    if arr[num] <= 2:
                        if arr[num] == 2:
                            count = 0
                            for num1 in arr:
                                if num1 < 6:
                                    count += 1
                            if count < 3:
                                continue
                        found = True
                        time.append(str(arr[num]))
                        used.append(num)
                        break
                elif cur == 1:
                    if time[0] == "2":
                        if arr[num] <= 3:
                            found = True
                            time.append(str(arr[num]))
                            time.append(":")
                            used.append(num)
                            break
                    else:
                        found = True
                        time.append(str(arr[num]))
                        time.append(":")
                        used.append(num)
                        break
                elif cur == 2:
                    if arr[num] <= 5:
                        found = True
                        time.append(str(arr[num]))
                        used.append(num)
                        break
                else:
                    found = True
                    time.append(str(arr[num]))
                    used.append(num)
                    break

            if not found:
                return ""
            cur += 1 

        return "".join(time)