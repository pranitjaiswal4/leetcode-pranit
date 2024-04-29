class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = list()
        self.total = 0

        for wt in w:
            self.total += wt
            self.prefix_sum.append(self.total)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)

        left = 0
        right = len(self.prefix_sum)

        while left < right:
            mid = (left + right) // 2

            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()