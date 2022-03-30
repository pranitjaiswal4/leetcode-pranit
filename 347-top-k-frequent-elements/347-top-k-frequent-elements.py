class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = list()
        freq = dict()
        
        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 1
        #     else:
        #         freq[num] += 1
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
                
        sorted_freq = sorted(freq.items(), key = lambda x : x[1], reverse = True)
        
        for i in range(k):
            result.append(sorted_freq[i][0])
            
        return result