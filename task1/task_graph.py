import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json-path",
        type=str
    )
    return parser.parse_args()


class Node:
    def __init__(self, value):
        self.value = value
        self.leafs = []


def parse_graph(graph_raw):
    root = Node(value=graph_raw['value'])
    for leaf_raw in graph_raw["leafs"]:
        leaf = parse_graph(leaf_raw)
        root.leafs.append(leaf)
    return root


def dfs(root, parent=None):
    neighs = []
    if parent:
        neighs.append(parent.value)

    for leaf in root.leafs:

        neighs.append(leaf.value)
        dfs(leaf, parent=root)

    print(f'Вершина: {root.value}, прямые соседи: {neighs}')




def main():
    args = parse_args()

    with open(args.json_path, 'r') as f:
        graph_raw = json.load(f)

    # print(json.dumps(graph_raw, indent=4))

    root = parse_graph(graph_raw)
    dfs(root)





if __name__ == '__main__':
    main()