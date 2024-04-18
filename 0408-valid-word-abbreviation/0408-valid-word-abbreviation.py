class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a = list()

        i = 0
        while i < len(abbr):
            snum = ""
            num = 0

            if abbr[i].isalpha():
                a.append(abbr[i])
                i += 1
            else:
                if abbr[i] == '0':
                    return False

                k = i
                while k < len(abbr) and abbr[k].isdigit():
                    snum += abbr[k]
                    k += 1
                
                num = int(snum)

                if num > len(word):
                    return False

                for _ in range(num):
                    a.append("*")

                i += len(snum)

        if len(word) != len(a):
            return False

        for i in range(len(word)):
            if a[i] != '*' and word[i] != a[i]:
                return False
        
        return True

