import numpy as np
from itertools import permutations
from typing import List, Sequence, Tuple

graph_matrix = np.array(
    [[17, 28, 5, 45],
    [23, 18, 48, 8],
    [11, 19, 15, 38],
    [28, 52, 16, 36],]
)


def make_paths(seq: Sequence, obligatory: List) -> List[List]:
    paths = [[]]
    for i in range(1, len(seq)+1):
        temp = [list(perm) for perm in permutations(seq, i)]
        paths.extend(temp)
    while obligatory:
        try:
            left = obligatory.pop(0)
        except IndexError:
            break
        else:
            for path in paths:
                path.insert(0, left)
        try:
            right = obligatory.pop()
        except IndexError:
            break
        else:
            for path in paths:
                path.append(right)
    return paths


def main() -> Tuple:
    paths = make_paths([2, 3], [1, 4])
    m = graph_matrix
    results = {}
    for row in paths:
        for j in range(len(row)):
            row[j] -= 1
    for path in paths:
        summ = 0
        s = ''.join(map(str, path))
        pairs = []
        for i in range(len(s)-1):
            try:
                pair = s[i:i+2]
            except IndexError:
                pass
            pairs.append(tuple(map(int, list(pair))))
        for node in pairs:
            i, j = node
            summ += m[i, j]
        results[s] = summ
    lst = sorted(results.items(), key=lambda tup: tup[1])
    ans = lst[0]
    return ans


if __name__ == '__main__':
    result = main()
    print(result)