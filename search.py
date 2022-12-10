import json
import queue
import time

with open("frozen_lake_mapping.json") as f:
    mapped_nodes = json.load(f)

nodes = [None]
nodes.extend(mapped_nodes)


def bfs():
    start_time = time.process_time()
    visited = []
    parent = {}
    root = nodes[1]
    q = queue.Queue()
    q.put(root)
    parent[root['id']] = None
    while not q.empty():
        u = q.get()
        visited.append(u['id'])
        if u['final']:
            end_time = time.process_time()
            return parent, u['id'], (end_time - start_time)
        for v in u['child']:
            if v not in visited:
                parent[v] = u['id']
                q.put(nodes[v])


def dfs():
    start_time = time.process_time()
    visited = []
    parent = {}
    root = nodes[1]
    s = []
    s.append(root)
    parent[root['id']] = None
    while len(s) > 0:
        u = s.pop()
        visited.append(u['id'])
        if u['final']:
            end_time = time.process_time()
            return parent, u['id'], (end_time - start_time)
        for v in u['child']:
            if v not in visited:
                parent[v] = u['id']
                s.append(nodes[v])


def find_path(parent_list, final):
    path = []
    actual = final
    while actual is not None:
        path.append(actual)
        actual = parent_list[actual]
    return list(reversed(path))

bfs_parents, bfs_final, bfs_time = bfs()
dfs_parents, dfs_final, dfs_time = dfs()
print(f"BFS PATH:{find_path(bfs_parents, bfs_final)}, TIME: {bfs_time} s")
print(f"DFS PATH:{find_path(dfs_parents, dfs_final)}, TIME: {dfs_time} s")
