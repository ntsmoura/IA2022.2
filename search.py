import json
import queue
import time
import timeit

with open("frozen_lake_mapping.json") as f:
    mapped_nodes = json.load(f)

nodes = [None]
nodes.extend(mapped_nodes)


def bfs():
    visited = []
    parent = {}
    root = nodes[1]
    q, q_ids = queue.Queue(), queue.Queue()
    q.put(root)
    q_ids.put(root["id"])
    parent[root["id"]] = None
    while not q.empty():
        u = q.get()
        q_ids.get()
        visited.append(u["id"])
        if u["final"]:
            return parent, u["id"]
        for v in u["child"]:
            if v not in visited and (v not in q_ids.queue):
                parent[v] = u["id"]
                q.put(nodes[v])
                q_ids.put(v)


def dfs():
    visited = []
    parent = {}
    root = nodes[1]
    s, s_ids = [], []
    s.append(root)
    s_ids.append(root["id"])
    parent[root["id"]] = None
    while len(s) > 0:
        u = s.pop()
        s_ids.pop()
        visited.append(u["id"])
        if u["final"]:
            return parent, u["id"]
        for v in u["child"]:
            if v not in visited and (v not in s_ids):
                parent[v] = u["id"]
                s.append(nodes[v])
                s_ids.append(v)


def find_path(parent_list, final):
    path = []
    actual = final
    while actual is not None:
        path.append(actual)
        actual = parent_list[actual]
    return list(reversed(path))


bfs_parents, bfs_final = bfs()
dfs_parents, dfs_final = dfs()
bfs_time = timeit.timeit(bfs, number=10000) / 10000
dfs_time = timeit.timeit(dfs, number=10000) / 10000
print(f"BFS PATH:{find_path(bfs_parents, bfs_final)}, TIME: {bfs_time} s")
print(f"DFS PATH:{find_path(dfs_parents, dfs_final)}, TIME: {dfs_time} s")
