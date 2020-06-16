class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 特判
        if not nums:
            return nums

        # 没有重复
        # 全排列： n x n-1 x n-2 x ... x 2
        # 设计一个函数，有一个必要参数是 当前已经获取到的元素
        result = []
        self.search([], nums, result)
        return result
    
    def search(self, pre_nums: List[int], nums, result) -> None:
        if len(nums) == 0:
            result.append(pre_nums)
        else:
            # 回溯在这儿，用python中list的特点避免了回退操作，但如果想只用一个list变量，那么仍然要用到append&pop进行回溯
            for i,num in enumerate(nums):
                self.search(pre_nums+[num], nums[:i]+nums[i+1:], result)
