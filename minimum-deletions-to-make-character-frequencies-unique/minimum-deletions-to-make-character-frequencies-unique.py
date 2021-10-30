class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        freq = dict()

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        counts = list(freq.values())
        counts.sort(reverse=True)
        # print(counts, ans)

        i, j = 0, 1

        while j < len(counts):
            # print(i, j)

            if counts[j] == counts[i]:
                i = j
                counts[j] -= 1
                ans += 1
            elif counts[j] > counts[i]:
                if counts[i] - 1 > 0:
                    ans += counts[j] - counts[i] + 1
                    counts[j] = counts[i] - 1
                    i = j
                else:
                    ans += counts[j]
            else:
                i = j

            j += 1

            # print(counts, ans)

        return ans
        # print(counts, ans)

        return ans