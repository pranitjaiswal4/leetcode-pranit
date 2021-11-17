class Solution:    
    def reverse(self, x: int) -> int:   
        strx = str(x)
        rev = []
        rev_num_s = ""

        length = len(strx)

        if(x>=0):
            for i in range(0, length):
                rev.append(strx[length-i-1])
            rev_num_s = rev_num_s.join(rev)
            rev_num = int(rev_num_s)

            if(rev_num <= ((2**31)-1)):
                return rev_num
            else:
                return 0
        else:
            for i in range(0, length-1):
                rev.append(strx[length-i-1])
            rev_num_s = rev_num_s.join(rev)
            rev_num = int(rev_num_s)

            if(-rev_num >= -(2**31)):
                return -rev_num
            else:
                return 0
        