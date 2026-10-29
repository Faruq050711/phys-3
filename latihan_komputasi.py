"""Metode numerik Komputasi Fisika. Jalankan: python python/latihan_komputasi.py"""
import numpy as np
import matplotlib.pyplot as plt


def euler(f, y0, x0, x1, h):
    xs, ys = [x0], [y0]
    while xs[-1] < x1 - 1e-12:
        ys.append(ys[-1] + h * f(xs[-1], ys[-1]))
        xs.append(xs[-1] + h)
    return np.array(xs), np.array(ys)


def rk4(f, y0, x0, x1, h):
    xs, ys = [x0], [y0]
    while xs[-1] < x1 - 1e-12:
        x, y = xs[-1], ys[-1]
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        ys.append(y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        xs.append(x + h)
    return np.array(xs), np.array(ys)


def newton(f, df, x, tol=1e-10):
    while abs(f(x)) > tol:
        x -= f(x) / df(x)
    return x


def trapesium(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    return (b - a) / n * (f(x).sum() - (f(a) + f(b)) / 2)


def monte_carlo_pi(n=100_000):
    p = np.random.rand(n, 2)
    return 4 * np.mean((p ** 2).sum(axis=1) <= 1)


if __name__ == "__main__":
    f = lambda x, y: y
    print("Euler y(0,2)  :", euler(f, 1, 0, 0.2, 0.1)[1][-1])
    print("Newton sqrt(2):", newton(lambda x: x * x - 2, lambda x: 2 * x, 1))
    print("Trapesium x^2 :", trapesium(lambda x: x ** 2, 0, 2, 2))
    print("Monte Carlo pi:", monte_carlo_pi())

    xe, ye = euler(f, 1, 0, 2, 0.5)
    xr, yr = rk4(f, 1, 0, 2, 0.5)
    x = np.linspace(0, 2, 100)
    plt.plot(x, np.exp(x), label="eksak")
    plt.plot(xe, ye, "o--", label="Euler")
    plt.plot(xr, yr, "s:", label="RK4")
    plt.title("dy/dx = y, h = 0,5")
    plt.legend()
    plt.show()
