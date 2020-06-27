# 比递归更快
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 此题很简单：先统计 unique number：出现次数的哈希表
        # 然后每个数字 num 的可能情况由原本的两种（取或不取）变为了k+1种（k为其出现的次数）
        # 然后就和不重复数组的子集没啥区别了

        num2count = {}
        for num in nums:
            num2count[num] = num2count.get(num, 0) + 1
        
        result = [[]]
        for num, count in num2count.items():
            length, total = len(result), len(result)  # 记录“上一层”子集元素的个数
            while length > 0:
                idx = total - length
                length -= 1
                for i in range(1, count+1):  # 这里注意上下界
                    result.append(result[idx]+[num]*i)
        return result
            
    
   
