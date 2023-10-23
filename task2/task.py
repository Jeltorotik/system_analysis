import argparse
import csv
from collections import defaultdict


class Node:
    def __init__(self, value):
        self.value = value
        self.leafs = []
        self.parent = None


def build_tree(edges):
    tree = dict()
    for v, u in edges:
        if v not in tree:
            tree[v] = Node(v)
        if u not in tree:
            tree[u] = Node(u)

        tree[v].leafs.append(u)
        tree[u].parent = v

    root = None
    for node in tree.values():
        if node.parent is None:
            root = node
            break
    return tree, root


def dfs(tree, output, root, grand_parent=None):
    output[root.value][0] = len(root.leafs)
    if root.parent is not None:
        output[root.value][1] = 1
    for leaf in root.leafs:
        output[root.value][2] += len(tree[leaf].leafs)
    if grand_parent is not None:
        output[root.value][3] = 1
    
    if root.parent in tree:
        parent = tree[root.parent]
        output[root.value][4] = len(parent.leafs) - 1
    for leaf in root.leafs:
        dfs(tree, output, tree[leaf], grand_parent=root.parent)


def task(var: str) -> str:
    edges = list(csv.reader(var.split("\n")))
    tree, root = build_tree(edges)
    output = defaultdict(lambda: [0, 0, 0, 0, 0])
    dfs(tree, output, root)
    
    result = []
    for i in range(len(output)):
        result.append(str(output[str(i+1)]))

    return "\n".join(result)

# task("1,2\n1,3\n3,4\n3,5")


"""
2	0	2	0	0
0	1	0	0	1
2	1	0	0	1
0	1	0	1	1
0	1	0	1	1
^   ^   ^   ^   ^
|   |   |   |   |
|   |   |   |   кол-во сиблингов r5
|   |   |   кол-во дедушек r4
|   |   кол-во внуков r3
|   кол-во родителей r2
кол-во детей r1
"""