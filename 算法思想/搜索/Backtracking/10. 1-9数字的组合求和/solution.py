class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # k个数（正整数）  &  和为n
        # 组合数中数字取值范围 1~9 且不重复
        # 组合不重复

        # 特判
        if 0 >= n or n > 50 or k <= 0:
            return []
        
        result = []
        self.search([], k, n, result)
        return result
    
    def search(self, pre_nums, k, n, result):
        if len(pre_nums) == k:
            if n == 0:
                result.append(pre_nums)
            else:
                return
        else:
            pre_num = 0
            if pre_nums:
                pre_num = pre_nums[-1]
            for num in range(pre_num+1, 10):
                self.search(pre_nums+[num], k, n-num, result)
