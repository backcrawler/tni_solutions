import matplotlib.pyplot as plt
from scipy import interpolate
from collections import namedtuple
from random import random

ver1 = namedtuple('Version_1', ['pixel', 'prog', 'duty_cycle', 'prob'])
ver2 = namedtuple('Version_2', ['system', 'object', 'circuit', 'rel_level'])


DATASETS = [
    [ver1(0.45, 0.45, 0.31, 0.23), ver1(0.06, 0.05, 0.14, 0.16), ver1(0.76, 0.23, 0.92, 0.19)],
    [ver2(0.35, 0.57, 0.12, 0.21), ver2(0.36, 0.35, 0.24, 0.26), ver2(0.76, 0.23, 0.92, 0.19)],
]


def main():
    for version in DATASETS:
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        for n, tup in enumerate(version):
            x = [elem for elem in range(len(tup))]
            y = [elem for elem in tup]
            plt_color = [random(), random(), random()]
            tck = interpolate.splrep(x, list(tup))
            y = interpolate.splev(x, tck)
            ax1.plot(x, y, label=f'Термины раздела {n+1}', color=plt_color)
        ax1.set_title('Иллюстративный образ разделов')
        ax1.grid(True, color='red')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()