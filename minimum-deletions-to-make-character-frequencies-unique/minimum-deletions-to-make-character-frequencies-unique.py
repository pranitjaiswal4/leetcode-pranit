class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        freq = dict()

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        counts = list(freq.values())

        visited = set()

        for i in range(len(counts)):
            if counts[i] not in visited:
                visited.add(counts[i])
            else:
                while counts[i] in visited:
                    if counts[i] > 0:
                        counts[i] -= 1
                    else:
                        break

                    ans += 1

                visited.add(counts[i])

        return ans