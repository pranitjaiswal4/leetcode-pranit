class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        n = len(chars)
        length = 1

        if n == 1:
            return 1
        
        while j < n - 1:
            
            # print(i, j, chars)
            
            if chars[j] == chars[j+1]:
                length += 1
                
            if chars[j] != chars[j+1]:
                i+=1

                if length > 1:
                    str_len = str(length)
                    for k in range(len(str_len)):
                        chars[i+k] = str_len[k]
                        
                    i += (k+1)
                    
                if i < n:
                    chars[i] = chars[j+1]
                        
                length = 1
            
            j += 1
            
        if j == n - 1:
            i+=1

            if length > 1:
                str_len = str(length)
                for k in range(len(str_len)):
                    chars[i+k] = str_len[k]

                i += (k+1)
            
        return i
