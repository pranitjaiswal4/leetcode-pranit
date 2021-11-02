class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tdict = dict()
        arrdict = dict()
        
        for i in range(len(target)):
            tdict[target[i]] = tdict.get(target[i], 0) + 1
            arrdict[arr[i]] = arrdict.get(arr[i], 0) + 1
        
        # print(tdict, arrdict)
        
        if tdict == arrdict:
            return True
        else:
            return False