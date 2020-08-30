# 以 743 题为例：https://leetcode-cn.com/problems/network-delay-time/
'''
Dijkstra算法适用于带权图、告知起点的最短路径的求解（权值必需为正，权值有负的用贝尔曼-福德（Bellman-Ford）算法）
https://www.cnblogs.com/OctoptusLian/p/9048532.html
步骤：
1. 构建邻接矩阵（可以按具体情况进行占位）
2. 构造并初始化 visited 和 dis 序列/字典（注意占位pos的初始化，不能影响整体结果）
# --------------------------- Dijkstra -----------------------------------
3. 外循环 —— 在未遍历点中寻找与 起点 距离最近的 点u （根据dis）
4. visited 更新 —— 加入 u
5. dis 更新 —— 通过 u 在到达 i 能否更近

输出： dis
'''

# 基础实现方法
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 特判

        # 
        matrix = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        for x, y, l in times:
            matrix[x][y] = min(matrix[x][y], l)
        max_dis = float('inf')
        dis = [float('inf')] * (N + 1)
        dis[K] = 0  # 初始化
        dis[0] = 0  # 占位，必须初始化为0
        visited = [0] * (N + 1)

        def DJ():
            for _ in range(1, N+1):
                min_dis = float('inf')
                u = -1
                for i in range(1, N+1):
                    if visited[i] == 0 and dis[i] < min_dis:
                        u = i
                        min_dis = dis[i]
                if u == -1:
                    return -1
                visited[u] = 1
                for i in range(1, N+1):
                    if visited[i] == 0:
                        dis[i] = min(dis[i], dis[u]+matrix[u][i])
        DJ()
        max_dis = max(dis)
        if max_dis == float('inf'):
            return -1
        return max_dis
 
# 堆优化
from collections import defaultdict
import heapq
class Solution_v2(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1

# Solution_v2 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/network-delay-time/solution/wang-luo-yan-chi-shi-jian-by-leetcode/
