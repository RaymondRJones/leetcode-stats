from collections import defaultdict, deque
def find_equilibrium_in_tree(n: int, edges: list[int], queries: List[List[int]]) -> List[int]:
    graph = defaultdict()
    for src,dest in edges:
        graph[src].append(dest)

    def bfs(start, dest):
        queue = deque()
        queue.append((start, [start]))
        while queue:
            node, curr_path = queue.popleft()
            if node == dest:
                return curr_path
            for child in graph[node]:
                queue.append((child, curr_path + [child]))
        return path
    
    ans = [0 for _ in range(n)]
    for start, destination in queries:
        seen = set()
        path = bfs(start, destination)
        path = sorted(path)
        median = path[len(path)//2]
        mismatch_count = 0
        for val in path:
            if val != median:
                mismatch_count += 1
        ans[i] = mismatch_count
    return ans
