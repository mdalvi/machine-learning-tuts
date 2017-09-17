import numpy as np
import matplotlib.pyplot as plt


class Bandit:
    def __init__(self, m):
        # True mean value
        self.m = m
        # Our estimate of the bandit's mean
        self.mean = 0
        # Number of samples
        self.N = 0

    def pull(self):
        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html#numpy.random.randn
        # https://en.wikipedia.org/wiki/Standard_deviation
        return np.random.randn() + self.m

    def update(self, x):
        # x = latest sample received from the bandit
        self.N += 1
        # The equation is taken from lecture 7. Updating a Sample Mean,
        # it is being used to calculate new mean from old mean
        self.mean = (1 - 1.0 / self.N) * self.mean + 1.0 / self.N * x


def run_experiment(m1, m2, m3, eps, N):
    """
    :param m1: mean of first bandit
    :param m2: mean of second bandit
    :param m3: mean of third bandit
    :param eps: epsilon value to perform epsilon_greedy
    :param N: the number of times we pull
    :return: returns the cumulative average after every play
    """

    # List of bandit instances with three different means viz. m1,m2,m3
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

    # np.empty(N) = returns a list of non-sense floating numbers of size N
    data = np.empty(N)

    for i in range(N):
        # epsilon greedy
        # np.random.random() = Return random floats in the half-open interval [0.0, 1.0)
        # 0 >= p < 1
        p = np.random.random()
        if p < eps:
            # 0 >= j < 3
            j = np.random.choice(3)
        else:
            # np.argmax = Returns the indices of the maximum values along an axis.
            # Fetching the index of bandit with the highest mean value
            j = np.argmax([b.mean for b in bandits])

        # We play the decided bandit
        # x = ( gussian sample from mean = 0 and stdev = 1 ) + true mean
        x = bandits[j].pull()

        # Updateing the sample mean of the current bandit
        bandits[j].update(x)

        # for the plot
        data[i] = x
    # np.cumsum = cumulative sum, also called as the running sum is a running total of the summation of a sequence
    # of numbers which is updated each time a new number is added to the sequence,
    # by adding the value of the new number to the previous running total

    # np.arange = Return evenly spaced values within a given interval.
    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

    # plot moving average ctr
    plt.plot(cumulative_average)
    plt.plot(np.ones(N) * m1)
    plt.plot(np.ones(N) * m2)
    plt.plot(np.ones(N) * m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)

    return cumulative_average


if __name__ == '__main__':
    # Running the experiment 3 times with different epsilons
    c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000)    #10 % epsilon
    c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000)  #5 % epsilon
    c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000)  #1 % epsilon

    # log scale plot
    plt.plot(c_1, label='eps = 0.1')
    plt.plot(c_05, label='eps = 0.05')
    plt.plot(c_01, label='eps = 0.01')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(c_1, label='eps = 0.1')
    plt.plot(c_05, label='eps = 0.05')
    plt.plot(c_01, label='eps = 0.01')
    plt.legend()
    plt.show()
