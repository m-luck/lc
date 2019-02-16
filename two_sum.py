class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        countA = -1
        ht = {}
        count = -1
        for numA in nums:
            count+=1
            if numA not in ht:
                ht[numA] = []
            ht[numA].append(count)
        for numA in ht:
            numB = target - numA
            if (numB in ht):
                if (numA != numB):
                    return [ht[numA][0],ht[numB][0]]
                elif len(ht[numA]) > 1:
                    return [ht[numA][0],ht[numA][1]]
