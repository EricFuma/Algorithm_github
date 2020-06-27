class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 子集： 类似于k（k为任意数）的组合数，但可以为空集
        # 对于一个长度为 n 的序列，其返回的子集个数为 2^n

        # 特判：验证后发现已经包括了，所以不需要
        #if not nums:
        #    return [[]]
        
        result = []
        self.get_set([], 0, nums, result)
        return result
    
    def get_set(self, pre_set, idx, nums, result):
        if idx == len(nums):
            result.append(pre_set)
        else:
            # 取该元素
            self.get_set(pre_set + [nums[idx]], idx+1, nums, result)
            # 不取该元素
            self.get_set(pre_set, idx+1, nums, result)
