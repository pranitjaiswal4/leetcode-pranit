class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        i, j = 0, 0
        n = len(fruits)
        basket = set()
        
        while j < n:
            if fruits[j] not in basket:
                if len(basket) == 2:
                    for fruit in basket:
                        if fruits[j-1] != fruit:
                            basket.remove(fruit)
                            break
                    
                    i = j - 1       
                    while fruits[i] == fruits[j-1]:
                        i -= 1
                    
                    i += 1
                    
            basket.add(fruits[j])
            maxFruits = max(maxFruits, j - i + 1)
                
            j += 1
        
        return maxFruits