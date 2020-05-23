import numpy as np


def get_answers(A, Y, P) -> tuple:
    M1 = np.array(A)
    V1 = np.array(Y)
    ans = np.linalg.solve(M1, V1)
    perc_ans = sum(val*x for val, x in zip(ans, P))
    return ans, perc_ans


def main() -> None:
    init_data = [
        ( [[3, 7], [2, 8]], [260, 228], [0.45, 1.18] ),
        ( [[3, 7], [2, 8]], [260, 250], [0.35, 1.3] ),
        ( [[3, 7], [2, 8]], [272, 262], [0.25, 1.23] ),
        ( [[3, 7], [2, 8]], [246, 262], [0.259, 1.341] )
    ]
    for n, data_row in enumerate(init_data):
        A = data_row[0]
        Y = data_row[1]
        P = data_row[2]
        ans, perc_ans = get_answers(A, Y, P)
        print(f'{n+1} solution: x={ans[0]} y={ans[1]} p={perc_ans}')


if __name__ == '__main__':
    main()