from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #stroing the non matching digits from both secret and guess
        unmatched_guess = []
        unmatched_secret = []
        bulls = 0

        for char in range(len(guess)):
            if guess[char] == secret[char]:
                bulls += 1
            else:
                unmatched_secret.append(secret[char])
                unmatched_guess.append(guess[char])

        #getting the count of only the elemnts which appear in both including duplicates
        cows = len(list((Counter(unmatched_secret) & Counter(unmatched_guess)).elements()))

        return f"{bulls}A{cows}B"