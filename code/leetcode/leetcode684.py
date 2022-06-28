# 并查集
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        vertex = list(range(n + 1))

        def find(v):
            if vertex[v] != v:
                vertex[v] = find(vertex[v])  # 寻找节点的最终父亲，并且把他最终父亲作为标记
            return vertex[v]

        def union(v1, v2):
            vertex[find(v1)] = find(v2)

        for v1, v2 in edges:
            if find(v1) != find(v2):
                union(v1, v2)
            else:
                return [v1, v2]

        return []


# 你自己写的，思路没错，就是没有优化
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_set = []
        for edge in edges:
            # print("current edge",edge)
            occur_index = []
            for e in edge:
                for index in range(len(union_set)):
                    if e in union_set[index]:
                        occur_index.append(index)
            # print(union_set)
            # print(occur_index)
            if len(occur_index) == 0:
                union_set.append({edge[0], edge[1]})
            elif len(occur_index) == 1:
                """
                集合取并集，union 是生成新的集合，update是原地操作
                """
                union_set[occur_index[0]].update({edge[0], edge[1]})
            elif len(occur_index) == 2:
                if occur_index[0] == occur_index[1]:
                    return edge
                else:
                    union_set[occur_index[0]].update(union_set.pop(occur_index[1]))

# a={1,2,3}
# b={3,4,5}
# print(a.update(b))
# print(a)
