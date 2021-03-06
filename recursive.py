import matplotlib.pyplot as plot
import time


def a_power_n(a, n):
    """
    Function to calculate the a^n using for loop.
    :param a: base, int
    :param n: exponent, int
    :return: prod, int
    """
    prod = 1
    for i in range(1, n+1):
        prod *= a
    return prod


def a_power_n_recursive(a, n):
    """
    Function to calculate the a^n using recursion.
    :param a: base, int
    :param n: exponent, int
    :return: int
    """
    if n == 0:
        return 1
    else:
        return a * a_power_n_recursive(a, n-1)


def main():
    """ Main function """
    a = 99
    x = []

    for i in range(1, 101):
        x.append(i)

    time_simple = []
    time_recursive = []

    for n in range(1, 101):
        start = time.time()
        a_power_n(a, n)
        end = time.time()
        time_simple.append(end-start)

    for n in range(1, 101):
        start = time.time()
        a_power_n_recursive(a, n)
        end = time.time()
        time_recursive.append(end-start)
  
    plot.plot(x, time_recursive, 'ro', x, time_simple, 'bo')
    plot.axis([0, 100, 0, 0.00001])
    plot.xlabel("exponent n")
    plot.ylabel("time")
    plot.show()


if __name__ == "__main__":
    main()
