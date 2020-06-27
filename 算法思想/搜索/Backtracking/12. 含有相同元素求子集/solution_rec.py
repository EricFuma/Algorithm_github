class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 此题很简单：先统计 unique number：出现次数的哈希表
        # 然后每个数字 num 的可能情况由原本的两种（取或不取）变为了k+1种（k为其出现的次数）
        # 然后就和不重复数组的子集没啥区别了

        num2count = {}
        for num in nums:
            num2count[num] = num2count.get(num, 0) + 1
        
        result = []
        self.get_set([], 0, list(num2count.keys()), num2count, result)
        return result
    
    def get_set(self, pre_nums, idx, unique_nums, num2count, result):
        if idx == len(unique_nums):
            result.append(pre_nums)
        else:
            count = num2count[unique_nums[idx]]
            num = unique_nums[idx]
            idx += 1
            for i in range(count+1):
                self.get_set(pre_nums+[num]*i, idx, unique_nums, num2count, result)
