上面提到了该题有一个关键条件，就是`序列中的数字是没有重复的`。这实际上是一个简化条件，那么如果没有这个条件，我们应该怎么解题呢？  
这也就引出了第二个题目： 

- 题目编号：47  
- 题目名称：全排列  
- 题目链接：https://leetcode-cn.com/problems/permutations-ii/  
- 题目描述：给定一个可包含重复数字的序列，返回所有不重复的全排列  


## 分析
#### 题目条件
1. 序列中可能有重复的数字  
2. 返回不重复的所有全排列  

#### 正向思考
因为是第一题的进阶嘛，所以一开始的想法肯定还是从第一题的基础上进行改进，以适应现在的条件。  
最简单的思路不外乎是用第一题的回溯法获取“有重复的全排列”，再去重（list也是可以比较的），但这显然是比较笨的解法。  
还是从一个例子入手。假设序列为 [1,2,3,3,4]，其中3是重复的元素，仍然按之前的思路进行序列扩展：   
Step 1：可以选择 1，2，3，4作为0位置上的元素，序列中有两个3，但是对于第二次出现的3，我们发现是一种`重复`，需要删除或跳过这种情况    
Step 2：在剩下元素中遍历，填充1位置，但遇到重复数字的时候，仍要跳过    
……  
Step 5: 就用剩下那个数字填充就可以了，就不需要考虑重复数字了    

从上面的分析我们可以看到，该题与题46的最大区别就是要略过每个位置上重复遍历某数的情况


#### 实现
那么怎么实现呢，我们可以在每个位置上维护一个 set。在某个位置上每遍历一个元素num，就判断它有没有在 set 中：没在，说明不重复，将num放入set中，否则就要跳过这种情况。  
其他就没有区别了，代码如下~

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 特判
        if not nums:
            return nums
        result = []
        self.search([], nums, result)
        return result

    def search(self, pre_nums, nums, result):
        if nums == []:
            result.append(pre_nums)
        else:
            mySet = set()
            for i,num in enumerate(nums):
                if num not in mySet:
                    mySet.add(num)
                    self.search(pre_nums+[num], nums[:i]+nums[i+1:], result)
                else:
                    continue
```
