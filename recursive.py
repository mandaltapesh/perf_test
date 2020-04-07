import time
import matplotlib.pyplot as plot 


def a_power_n(a, n):

    prod = 1
    for i in range(1, n+1):
        prod *= a
    return prod


def a_power_n_recursive(a, n):

    if n == 0:
        return 1
    else:
        prod = a * a_power_n_recursive(a, n-1)
    return prod


def main():
    a = 99
    x = []

    for i in range(1, 11):
        x.append(i)

    time_simple = []
    time_recursive = []

    for n in range(1, 11):
        start = time.time()
        a_power_n(a, n)
        end = time.time()
        time_simple.append(end-start)

    for n in range(1, 11):
        start = time.time()
        a_power_n_recursive(a, n)
        end = time.time()
        time_recursive.append(end-start)
  
    plot.plot(x, time_recursive, 'ro', x, time_simple, 'bo')
    plot.axis([0, 10, 0, 0.000005])
    plot.xlabel("exponent n")
    plot.ylabel("time")
    plot.show()


if __name__ == "__main__":
    main()
