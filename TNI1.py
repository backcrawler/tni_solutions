import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes._subplots import Subplot
from typing import Sequence
from random import shuffle

t = np.arange(25)

datasets = [
    (1.5, 21, 15, 417),
    (1.75, 32.8, 17, 425),
    (1.37, 28.2, 10.45, 401),
]

colors = ['red', 'black', 'green']


def build_form(tup: Sequence, graph: Subplot, num: int) -> None:
    a, b, c, d = tup
    Y = a*np.sin((a**2)*np.tan((d+b)/(np.cos(c*t)))*t)
    plt_color = colors.pop()
    graph.plot(t, Y, label=f'Test {num+1}', color=plt_color)


if __name__ == '__main__':
    shuffle(colors)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    try:
        file = pd.read_excel('tni_1.xlsx')
    except FileNotFoundError:
        pass
    else:
        datasets = file.values()
    for n, dataset in enumerate(datasets):
        build_form(dataset, ax1, n)
    ax1.set_title('ТНИ1')
    plt.legend()
    plt.show()
