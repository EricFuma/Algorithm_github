class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        # 条件
        # 1. 有重复的候选数组（正整数）
        # 2. 解集不能有重复的组合

        # 特判

        num2count = defaultdict(int)
        for num in candidates:
            num2count[num] += 1
        result = []
        self.search([], list(num2count.items()), 0, target, result)
        return result
    
    def search(self, pre_nums, num_and_count, idx, target, result):
        #print(pre_nums, num_and_count)
        if target == 0:
            result.append(pre_nums)
        else:
            for j in range(idx, len(num_and_count)):
                tmp = target
                count = 1
                num = num_and_count[j][0]
                max_count = num_and_count[j][1]
                while tmp-num >= 0 and count <= max_count:
                    tmp -= num
                    self.search(pre_nums+[num]*count, num_and_count, j+1, tmp, result)
                    count += 1
