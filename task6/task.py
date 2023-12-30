from collections import defaultdict
import json

def aggregate_rankings(rankings):
    d = defaultdict(list)
    w = 1.0
    for ranks in rankings:
        for elem in ranks:
            if type(elem) == list:
                temp_weight = w + (len(elem) - 1) / 2
                for inner_elem in elem:
                    d[inner_elem].append(temp_weight)
                w += len(elem)
            else:
                d[elem].append(w)
                w += 1
    return d


def find_S(marks):
    X = dict()
    for key, val in marks.items():
        X[key] = sum(val)
    
    D_X = sum(X.values()) / len(X)
    S = sum([(x_i - D_X)**2 for x_i in X.values()])
    return S


def find_T(ranks):
    t_i = 0
    for elem in ranks:
        if type(elem) == list:
            h_k = len(elem)
            t_i += h_k ** 3 - h_k
    return t_i


def get_json(filename):
    with open(filename, encoding='UTF-8') as f:
        ranking = json.load(f)
    return ranking


def task(filenames):
    rankings = [get_json(filename) for filename in filenames]
    aggregated = aggregate_rankings(rankings)
    S = find_S(aggregated)
    m, n = len(rankings), len(aggregated)


    D = S / (n - 1)
    T = sum([find_T(ranks) for ranks in rankings])
    D_max =  (m**2 * (n**3 - n) - m * T) / (12 * (n - 1))
    
    W = D / D_max
    return W



if __name__ == '__main__':
    experts = ['ranking_A.json', 'ranking_B.json', 'ranking_C.json']
    W = task(experts)
    print(f"W = {W:.2f}")