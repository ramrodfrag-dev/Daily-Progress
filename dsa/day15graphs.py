import queue
import networkx as nx
import matplotlib.pyplot as plt
import collections

def bfs_traversal(graph,start_node):
    visited=set()
    q=collections.deque()
    q.append(start_node)
    bfs_order=[]
    visited.add(start_node)
    
    while q:
        vertex=q.pop()
        bfs_order.append(vertex)
        for node in graph[vertex]:
            if node not in visited:
                q.append(node)
    return bfs_order
    
def dfs_traversal(graph,start_node,visited=None):
    if visited is None:
        