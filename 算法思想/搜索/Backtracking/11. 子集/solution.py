
# 此为未优化方法，用到了中间变量，并且多了一些无用的遍历
# 也即 tmp.append(seq)
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            tmp = []
            for i,seq in enumerate(result):
                tmp.append(seq)
                tmp.append(seq+[num])
            result = tmp
        return result
'''


# 非递归方法借鉴了层序遍历
# 此为去除中间变量、省掉无用遍历后的非递归方法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            length = len(result)
            total = length
            while length > 0:
                idx = total - length
                length -= 1
                result.append(result[idx]+[num])
        return result
