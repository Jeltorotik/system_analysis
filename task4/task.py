from collections import defaultdict
import math

def calc_probs(dice):
    sum_probs = defaultdict(int)
    product_probs = defaultdict(int)
    comb_probs = defaultdict(int)

    for dice1 in [1,2,3,4,5,6]:
        for dice2 in [1,2,3,4,5,6]:
            sum_value = dice1 + dice2
            product_value = dice1 * dice2

            sum_probs[sum_value] += 1/36
            product_probs[product_value] += 1/36
            comb_probs[(sum_value, product_value)] += 1/36
    return sum_probs, product_probs, comb_probs


def calc_entropy(probs):
    entropy = 0.0
    for p in probs.values():
        entropy -= p * math.log2(p)
    return entropy


def task() -> list:
    sum_probs, product_probs, comb_probs = calc_probs(6)

    H_AB = calc_entropy(comb_probs)
    H_A = calc_entropy(sum_probs)
    H_B = calc_entropy(product_probs)

    H_B_A = H_AB - H_A
    I_AB = H_B - H_B_A

    return [round(val, 2) for val in [H_AB, H_A, H_B, H_B_A, I_AB]]


if __name__ == '__main__':
    print(f'{task()} == {[4.34, 3.27, 4.04, 1.06, 2.98]}')
    assert(task() == [4.34, 3.27, 4.04, 1.06, 2.98])