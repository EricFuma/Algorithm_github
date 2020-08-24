from typing import List
'''
不考虑顺序 == 限定死某一种顺序 ==》从小到大
仍然是回溯法
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or n < k or k == 0:
            return []
        res = []
        #nums = [i+1 for i in range(n)]
        self.search([], 1, k, n, res)
        return res
    
    def search(self, curr_nums, start, k, n, res):
        if len(curr_nums) == k:
            res.append(curr_nums[:])   # 切片！ 在回溯设计阶段就用切片变量输入到函数中
        else:
            for num in range(start, n+1):
                curr_nums.append(num)
                self.search(curr_nums, num+1, k, n, res)
                # 回溯
                curr_nums.pop()
            
    '''
    优化版本的search —— 提前停止
    '''
    def improve_search(self, curr_nums, start, k, n, res):
        # 剩余元素已经不够，不用再继续了
        if n + 1 - start < k - len(curr_nums):
            return False
        for num in range(start, n+1):
            curr_nums.append(num)
            if len(curr_nums) == k:
                res.append(curr_nums[:])
            else:
                self.improve_search(curr_nums, num+1, k, n, res)
            # 回溯
            curr_nums.pop()
            
    '''
    广度优先 —— 优化了，很快
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or n < k or k == 0:
            return []
        queue, res = [], []
        for start in range(1, n+2-k):
            queue.append([start])
            while queue:
                curr_nums = queue.pop(0)
                if len(curr_nums) == k:
                    res.append(curr_nums)
                else:
                    new_start = curr_nums[-1]
                    
                    for num in range(new_start+1, n+2-(k-len(curr_nums))):
                        curr_nums.append(num)
                        if len(curr_nums) == k:
                            res.append(curr_nums[:])
                        else:
                            queue.append(curr_nums[:])
                        curr_nums.pop()
        return res

            

