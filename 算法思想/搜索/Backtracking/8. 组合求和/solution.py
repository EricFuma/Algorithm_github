class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 条件：
        # 1. 组合
        # 2. 正整数，无限取数
        # 3. 不能有重复的组合
        
        # 特判
        if not candidates or target <= 0:
            return []
        result = []
        candidates.sort()
        self.search([], 0, candidates, target, result)
        return result
    
    def search(self, pre_nums, idx, candidates, target, result):
        if target == 0:
            result.append(pre_nums)
        else:
            for j in range(idx, len(candidates)):
                tmp = target
                count = 1
                while tmp >= candidates[j]:
                    tmp -= candidates[j]
                    # 这里注意，不能定义一个新的list变量tmp_nums再扩展，因为一旦改变了list变量值，
                    # 那么这个改动就是连带影响所有的。所以在回溯法中最好不要出现 tmp_nums += [candidates[j]] 这样赋值操作
                    self.search(pre_nums+[candidates[j]]*count, j+1, candidates, tmp, result)
                    count += 1
