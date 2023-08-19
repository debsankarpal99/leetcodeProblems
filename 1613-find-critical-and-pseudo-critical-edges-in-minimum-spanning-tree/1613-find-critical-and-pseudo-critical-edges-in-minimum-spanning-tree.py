class Solution:
    def find(self, u, parent):
        if u == parent[u]:
            return u
        return self.find(parent[u], parent)

    def union_DSU(self, u, v, parent):
        p1 = self.find(u, parent)
        p2 = self.find(v, parent)
        parent[p2] = p1

    def mst(self, k, edges, include, exclude):
        n = len(include)
        m = len(exclude)
        parent = list(range(k))
        res = 0
        count = 0

        if n != 0:
            self.union_DSU(include[0], include[1], parent)
            res += include[2]
            count += 1

        for edge in edges:
            u, v, cost = edge

            if m != 0 and exclude[0] == u and exclude[1] == v and exclude[2] == cost:
                continue

            if n != 0 and include[0] == u and include[1] == v and include[2] == cost:
                continue

            p1 = self.find(u, parent)
            p2 = self.find(v, parent)

            if p1 != p2:
                self.union_DSU(p1, p2, parent)
                res += cost
                count += 1

        return res if count == k - 1 else float('inf')

    def findCriticalAndPseudoCriticalEdges(self, k, edges):
        orig_edges = []
        for edge in edges:
            orig_edge = [edge[0], edge[1], edge[2]]
            orig_edges.append(orig_edge)

        X = len(orig_edges)
        ans = []
        critical_edges = []
        pseudo_critical_edges = []

        sorted_edges = sorted(edges, key=lambda x: x[2])

        empty_vec = []
        orig_cost = self.mst(k, sorted_edges, empty_vec, empty_vec)

        for i in range(X):
            excluded_cost = self.mst(k, sorted_edges, empty_vec, orig_edges[i])
            included_cost = self.mst(k, sorted_edges, orig_edges[i], empty_vec)

            if excluded_cost > orig_cost:
                critical_edges.append(i)

            elif included_cost == orig_cost:
                pseudo_critical_edges.append(i)

        ans.append(critical_edges)
        ans.append(pseudo_critical_edges)
        return ans
