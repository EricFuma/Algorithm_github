class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1...n 说明这n个数是不重复的
        # 返回组合数

        # 特判
        if n <= 0:
            return []

        # [1,2,3,4]
        # [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]
        # 这种生成方式就是 ele_1 < ele_2
        result = []
        self.search([], n, k, result)
        return result
    
    def search(self, pre_nums, n, k, result):
        if len(pre_nums) == k:
            result.append(pre_nums)
        else:
            if not pre_nums:
                pre_num = 0
            else:
                pre_num = pre_nums[-1]
            
            # 可以用这个条件限制
            '''
            if k-len(pre_nums) > n-pre_num:  # 若`待填充的槽位 > 剩余元素数量`，则一定不满足条件
                return
            for num in range(pre_num+1, n+1):
                self.search(pre_nums+[num],n, k, result)
            '''

            # 也可以用这个条件限制
            for num in range(pre_num+1, n+2-(k-len(pre_nums))):  # 预留足够填充剩余槽位的元素
                self.search(pre_nums+[num], n, k, result)
    
            
