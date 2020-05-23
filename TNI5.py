from statistics import mean, variance
from typing import Callable, Sequence
from pprint import pprint
import pandas as pd


def populate_lst(data: Sequence[Sequence], func: Callable) -> list:
    out = []
    for comb in zip(*data):
        out.append(round(func(comb), 4))
    return out


def build_covar(data: Sequence, var_in: list, mean_in: list) -> list:
    out = []
    if len(var_in) != len(mean_in):
        raise ArithmeticError('lengths dont match!')
    LEN = len(var_in)
    prob = 1/(LEN**2)
    for rowNum in range(LEN):
        covRow = []
        for colNum in range(LEN):
            if rowNum == colNum:
                covRow.append(var_in[rowNum])
                continue
            cov = 0
            for i in range(3):
                for j in range(3):
                    cov += (data[i][rowNum] - mean_in[rowNum])*(data[j][colNum] - mean_in[colNum])*prob
            if cov < 1e-6:
                cov = 0
            covRow.append(cov)
        out.append(covRow)
    return out


def main() -> None:
    exprs = [
        [0.844, 0.929, 0.971, 0.229, 0.302, 0.026, 0.240, 0.921],
        [0.322, 0.720, 0.152, 0.145, 0.466, 0.500, 0.885, 0.311],
        [0.037, 0.695, 0.614, 0.206, 0.967, 0.425, 0.110, 0.500],
    ]
    try:
        f = pd.read_excel('tni_5.xlsx')
    except FileNotFoundError:
        pass
    else:
        exprs = f.values()
    Ds = populate_lst(exprs, variance)
    Ms = populate_lst(exprs, mean)
    print(Ds)
    print(Ms)
    result = build_covar(exprs, Ds, Ms)
    pprint(result)


if __name__ == '__main__':
    main()