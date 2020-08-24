# https://leetcode-cn.com/problems/permutations/
'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
'''

from typing import List
'''
搜索——回溯法——切片！
1) BFS
2) DFS
3) 巧妙的 DFS
'''


class Solution:
    # 从 n 个点组成的完全图中找长度为n的路径（不能走重复的点）

    '''
    方法一、广度优先搜索 bfs_permute
    '''
    def bfs_permute(self, nums: List[int]) -> List[List[int]]:
        # 特判
        if len(nums) < 2:
            return [nums]
        
        queue, res = [], []
        n = len(nums)
        for i in range(n):
            start = nums[i]
            queue.append([start])
            while queue:
                curr = queue.pop(0)
                for j in range(n):
                    if nums[j] not in curr:
                        curr.append(nums[j])
                        if len(curr) == n:
                            res.append(curr)  # 不用切片，因为一定不需要回溯
                        else:
                            queue.append(curr[:])  # 切片，因为一定需要回溯
                            # 回溯
                            curr.pop()
        return res
    
    '''
    方法二、深度优先搜索
    '''
    def search(self, curr_nums, left_nums, result):
        if not left_nums:
            result.append(curr_nums)
        else:
            for i,num in enumerate(left_nums):
                self.search(curr_nums+[num], left_nums[:i]+left_nums[i+1:], result)

    def dfs_permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i, start in enumerate(nums):
            self.search([start], nums[:i]+nums[i+1:], res)
        return res


    '''
    三、巧妙的 DFS
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 特判
        if len(nums) < 2:
            return [nums]

        def backtrack(first = 0):
            if first == n:
                res.append(nums[:])  # 切片！
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    # 回溯
                    nums[first], nums[i] = nums[i], nums[first]
        
        res = []
        n = len(nums)
        backtrack()
        return res


