"""
Здесь будет наш график
utils.py
"""

import numpy  # pip install numpy
import matplotlib  # модуль для графиков
import numpy as np
from matplotlib import pyplot

# функция которая рисует  точки и стрелки
def plot_points(features, labels):
    X = np.array(features)
    Y = np.array(labels)
    spam = X[np.argwhere(Y == 1)]
    ham = X[np.argwhere(Y == 0)]
    pyplot.scatter([s[0][0] for s in spam],
                   [s[0][1] for s in spam],
                   s=100,
                   color="cyan",
                   edgecolor='k',
                   marker="^"
                   )
    pyplot.scatter([s[0][0] for s in ham],
                   [s[0][1] for s in ham],
                   s=100,
                   color="red",
                   edgecolor='k',
                   marker="s"
                   )
    pyplot.xlabel("aack")
    pyplot.ylabel("beep")
    pyplot.legend(["happy", "sad"])


def draw_line(a, b, c, starting=0,  ending=3, **kwargs):
    """ рисует линию ax + bx + c = 0"""
    x = np.linspace(starting, ending, 1000)
    pyplot.plot(x, -c/b - a * x/ b, **kwargs)


