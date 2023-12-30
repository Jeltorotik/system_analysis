from collections import defaultdict
import json

def aggregate_rankings(rankings):
    d = defaultdict(list)
    for ranks in rankings:
        for i, elem in enumerate(ranks, 1):
            if type(elem) == list:
                for inner_elem in elem:
                    d[inner_elem].append(i)
            else:
                d[elem].append(i)
    return d


def find_D(marks):
    n = len(marks)
    X = dict()
    for key, val in marks.items():
        X[key] = sum(val)
    
    D_X = sum(X.values()) / n
    
    D = sum([(x_i - D_X)**2 for x_i in X])
    D /= n - 1
    return D


def get_json(filename):
    with open(filename, encoding='UTF-8') as f:
        ranking = json.load(f)
    return ranking


def task(filenames):
    rankings = [get_json(filename) for filename in filenames]
    aggregated = aggregate_rankings(rankings)
    D = find_D(aggregated)
    return D 



if __name__ == '__main__':
    experts_1 = ['ranking_A.json', 'ranking_B.json']
    exports_2 = ['ranking_A.json', 'ranking_C.json']
    D1 = task(experts_1)
    D2 = task(exports_2)
    print(f"W_1 = {D1 / max(D1, D2)}")
    print(f"W_2 = {D2 / max(D1, D2)}")

