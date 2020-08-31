class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dis = [float('inf')] * (N + 1)
        dis[0], dis[K] = 0, 0
        graph = collections.defaultdict(list)
        for x, y, l in times:
            graph[x].append((y, l))
        # ---------------------- BFS ----------------------
        '''
        # 广度优先
        bfs()
        '''
        # -------------------------------------------------


        # ---------------------- DFS ----------------------
        def dfs(node, elapsed):
            for time, nei in sorted(graph_dfs[node]):  # 把 sorted 去了，时间复杂度会高很多（贪心思想）
                new_dis = elapsed + time
                if new_dis >= dis[nei]:
                    continue
                dis[nei] = new_dis
                dfs(nei, new_dis)
        '''
        # 深度优先
        graph_dfs = defaultdict(list)
        for x, y, l in times:
            graph_dfs[x].append((l, y))
        dfs(K, 0)
        '''
        # ------------------------------------------------------------------
        
        # ------------------------ Dijkstra --------------------------------
        visited = [0] * (N + 1)
        def DJ():
            for _ in range(N):
                x, min_dis = -1, float('inf')
                for i, d in enumerate(dis[1:]):
                    node = i + 1
                    if visited[node] == 0 and dis[node] < min_dis:
                        x = node
                        min_dis = dis[node]
                if x == -1:
                    break
                visited[x] = 1
                for y, y_d in graph[x]:
                    if visited[y] == 0:
                        dis[y] = min(dis[y], min_dis + y_d)
        DJ()
        ans = max(dis)
        return ans if ans < float('inf') else -1

        

        
       

