import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes._subplots import Subplot
from random import shuffle

t = np.arange(25)

colors = ['red', 'blue', 'green', 'black', 'orange', 'purple', 'yellow', 'brown']

input_parametrs = [
    {'w1': 12, 'w2': 24, 'w3': 128, 'a1': 12, 'a2': 14, 'a3': 24},
    {'w1': 8, 'w2': 18, 'w3': 32, 'a1': 8, 'a2': 12, 'a3': 16},
]

output_parametrs = [
    {'v1': 78, 'v2': 128, 'v3': 412, 'b1': 12, 'b2': 75, 'b3': 24},
    {'v1': 156, 'v2': 12, 'v3': 34, 'b1': 45, 'b2': 56, 'b3': 12},
]


def build_graph(params: dict, graph: Subplot, *, extra=None) -> None:
    p = params
    Y = 2.89 + p['a1']*np.sin(p['w1']*t + p['a2']*np.sin(p['w2']*t) + p['a3']*np.sin(p['w3']*t))
    plt_color = colors.pop()
    graph.plot(t, Y, color=plt_color, label=extra)


def reshape_dict(params: dict) -> dict:
    d = {}
    for key, val in params.items():
        key = key.replace('b', 'a').replace('v', 'w')
        d[key] = val
    return d


def ins_and_outs() -> None:
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for in_dict in input_parametrs:
        build_graph(in_dict, ax1)
    ax1.set_title('Входные сигналы')
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    for out_dict in output_parametrs:
        out_dict = reshape_dict(out_dict)
        build_graph(out_dict, ax2)
    ax2.set_title('Выходные сигналы')
    plt.legend()
    plt.show()


def pairs() -> None:
    for i, (in_dict, out_dict) in enumerate(zip(input_parametrs, output_parametrs)):
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        out_dict = reshape_dict(out_dict)
        build_graph(in_dict, ax1, extra='Input')
        build_graph(out_dict, ax1, extra='Output')
        ax1.set_title(f'Pairs {i+1}')
    plt.legend()
    plt.show()


def main() -> None:
    ins_and_outs()
    pairs()


if __name__ == '__main__':
    main()