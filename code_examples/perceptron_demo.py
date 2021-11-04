import argparse
import random
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn

plt.rc('font', family='serif')
seaborn.set(style='whitegrid')
seaborn.set_context('talk')


def plot_data(data, ax, lim=0.5):
    data[data.y == 1].plot(
          kind='scatter', x='$x_1$', y='$x_2$', color='green', ax=ax)
    data[data.y == -1].plot(
          kind='scatter', x='$x_1$', y='$x_2$', color='red', ax=ax)
    ax.set_xlim(-lim, lim + 1)
    ax.set_ylim(-lim, lim + 1)


class Perceptron:
    'A simple Perceptron implementation.'
    def __init__(self, weights, bias, alpha=0.1):
        self.weights = weights
        self.bias = bias
        self.alpha = alpha

    def propagate(self, x):
        return self.activation(self.net(x))

    def activation(self, net):
        if net > 0:
            return 1
        return -1

    def net(self, x):
        return np.dot(self.weights, x) + self.bias

    def learn(self, x, y):
        y_hat = self.propagate(x)
        self.weights = [w_i + self.alpha * x_i * (y-y_hat)
                        for (w_i, x_i) in zip(self.weights, x)]
        self.bias = self.bias + self.alpha*(y-y_hat)
        return np.abs(y_hat - y)


def gt1(x):
    return 2 * int(np.sum(x) > 1) - 1


def xor(x):
    return 2 * int((x[0] > 0.5) == (x[1] > 0.5)) - 1


def learn_row(perceptron, row):
    '''
    Train the perceptron on the data row
    Returns 1 if perceptron updated, otherwise 0
    '''
    return perceptron.learn(row[0:2], row[2])


def learn_data(perceptron, data, k=None):
    '''
    Train the perceptron for one epoch on the data
    Returns the number of errors
    '''
    count = 0
    for i, row in data.iterrows():
        count += learn_row(row)
    return count


def threshold(perceptron, x_1, y_offset=0):
    '''
    Compute the location of the perceptron decision boundary
    x_1: the x value where
    y_offset: the y (or x_2) offset for the boundary
    '''
    tmp = -perceptron.weights[0] * x_1 - perceptron.bias - y_offset
    return tmp / perceptron.weights[1]


def plot_perceptron_threshold(perceptron, ax, lim=0.5):
    '''
    Plot the perceptron's decision boundary
    '''
    xlim = (-lim, 1 + lim)

    x2s = [threshold(perceptron, x1) for x1 in xlim]
    above = [threshold(perceptron, x1, y_offset=-100) for x1 in xlim]
    below = [threshold(perceptron, x1, y_offset=100) for x1 in xlim]
    ax.plot(xlim, x2s)
    ax.fill_between(xlim, x2s, above, alpha=0.2, color='green')
    ax.fill_between(xlim, x2s, below, alpha=0.2, color='red')

    ax.set_xlim(-lim, 1 + lim)
    ax.set_ylim(-lim, 1 + lim)


def plot_all(data, t, ax=None, point=None, result=None):
    '''
    Plot the data
    point: if not None, the datapoint we're training on at the moment
    result: if 1, the perceptron misclassified `point`
    '''
    if ax is None:
        fig = plt.figure(figsize=(5, 4))
        ax = fig.gca()
    if point is not None:
        if result is None or result == 0:
            marker = 'o'
        else:
            marker = 'x'
        # default point has size 36
        ax.scatter(point[0], point[1], s=64, color='black', marker=marker)
    plot_data(data, ax)

    ax.set_title(f'$t={t}$')


def make_plot_array(perceptron, data, rows=5, cols=5):
    '''
    Makes a rows x cols array of plots showing perceptron training
    '''
    f, axarr = plt.subplots(
        rows, cols, sharex=True, sharey=True, figsize=(8, 8))
    axs = list(itertools.chain.from_iterable(axarr))
    t = 0
    while t < rows * cols:
        for t_, row in itertools.islice(data.iterrows(), rows * cols):
            plot_perceptron_threshold(perceptron, axs[t])
            result = learn_row(perceptron, row)
            plot_all(data, t, ax=axs[t], point=row[0:2], result=result)

            t += 1
            if t == rows * cols:
                break
    f.tight_layout()
    plt.show()


def make_animation(perceptron, data, fn="test.mp4", frames=20):
    '''
    Animates the step-by-step training of perceptron
    '''

    datarows = list(data.iterrows())

    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca()

    def animate(frame_index):
        ''' Animation subcall '''
        ax.clear()
        ax.set_title(f'$t={frame_index}$')

        row = datarows[frame_index % data.shape[0]][1]
        plot_perceptron_threshold(perceptron, ax=ax)
        result = learn_row(perceptron, row)
        plot_all(data, frame_index, ax=ax, point=row[0:2], result=result)

    anim = animation.FuncAnimation(fig, animate, frames=frames)
    writervideo = animation.FFMpegWriter(fps=1)
    anim.save(fn, writer=writervideo)

    plt.tight_layout()
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_labels", choices=["xor", "gt1"])
    parser.add_argument("plot_type", choices=["plot_array", "animation"])
    parser.add_argument("--frames", type=int, default=20,
                        help="how many animation frames")
    parser.add_argument("--fn", type=str, default="test.mp4",
                        help="where to save the animation")
    args = parser.parse_args()

    seed = 3
    np.random.seed(seed)
    random.seed(seed)

    lim = 0.5

    if args.data_labels == "gt1":
        data = pd.DataFrame(columns=('$x_1$', '$x_2$'),
                            data=np.random.uniform(size=(7, 2)))
        data['y'] = data.apply(gt1, axis=1)
    elif args.data_labels == "xor":
        data = pd.DataFrame(columns=('$x_1$', '$x_2$'),
                            data=np.array([(0, 0), (1, 0), (0, 1), (1, 1)]))
        data['y'] = data.apply(xor, axis=1)
    else:
        raise ValueError()

    perceptron = Perceptron([0.0, -0.5], 0.1)

    if args.plot_type == "plot_array":
        make_plot_array(perceptron, data)
    elif args.plot_type == "animation":
        make_animation(perceptron, data, fn=args.fn, frames=args.frames)
