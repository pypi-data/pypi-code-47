import matplotlib.pyplot as plt
import numpy as np


def moving_average(x, y):
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    print('run this module as main')
    x = np.linspace(0, 10, 100)
    y = x + np.random.randn(100)
    moving_average(x, y)
