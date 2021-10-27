class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i, j, = 0, 0
        result = 0
        n = len(s)
        freq = dict()

        while j < n:

            freq[s[j]] = freq.get(s[j], 0) + 1

            if len(freq) <= k:
                result = max(result, j-i+1)
            elif len(freq) > k:
                while len(freq) > k:
                    if freq[s[i]] - 1 > 0:
                        freq[s[i]] -= 1
                    else:
                        freq.pop(s[i])

                    i += 1

            j += 1

        return result