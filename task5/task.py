import numpy as np


def dfs(vertex, graph, visited, component):
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, component)

def get_connected_components(edges):
    # Создаем граф на основе списка ребер
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = set()
        if edge[1] not in graph:
            graph[edge[1]] = set()
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    visited = set()
    connected_components = []
    for vertex in graph.keys():
        if vertex not in visited:
            component = []
            dfs(vertex, graph, visited, component)
            connected_components.append(component)
            
    return connected_components


def preprocess_rankings(rankings):
    d = dict()
    for i, elem in enumerate(rankings):
        if type(elem) == list:
            for inner_elem in elem:
                d[inner_elem] = i
        else:
            d[elem] = i
    return d


def flatten(rankings):
    flat = []
    for elem in rankings:
        if type(elem) == list:
            flat += elem
        else:
            flat.append(elem)
    return flat


def build_relation_matrix(rankings):
    d = preprocess_rankings(rankings)

    n = max(d.keys())
    matrix = np.zeros((n, n))
    for i in d.keys():
        for j in d.keys():
            matrix[i-1][j-1] = d[i] >= d[j]
    return matrix


def find_contradictory_pairs(YA, YB):
    Y_A_transpose = YA.T
    Y_B_transpose = YB.T

    Y_AB = np.multiply(YA, YB)
    Y_AB_transpose = np.multiply(Y_A_transpose, Y_B_transpose)

    pairs = set()
    for i in range(len(Y_AB)):
        for j in range(len(Y_AB)):
            if not(Y_AB[i][j] or Y_AB_transpose[i][j]):
                if (j+1, i+1) not in pairs:
                    pairs.add((i+1, j+1))

    return pairs


def combine_rankings(A, B):
    YA = build_relation_matrix(A)
    YB = build_relation_matrix(B)
    pairs = find_contradictory_pairs(YA, YB)
    connected_components = get_connected_components(pairs)

    flatten_A = flatten(A)
    result = []

    used = set()
    for elem in flatten_A:
        if elem not in used:
            for cl in connected_components:
                if elem in cl:
                    for inner_elem in cl:
                        used.add(inner_elem)
                    result.append(sorted(cl))
                    break
            else:
                result.append(elem)
    
    return result



import json
def get_json(filename):
    with open(filename, encoding='UTF-8') as f:
        ranking = json.load(f)
    return ranking

def task():
    A = get_json('ranking_A.json')
    B = get_json('ranking_B.json')
    
    new_ranking = combine_rankings(A, B)
    return new_ranking

if __name__ == "__main__":
    print(task())
