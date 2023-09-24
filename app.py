import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation as anime


df = pd.read_csv("africa_c.csv")
print(df.__len__())
# plt.xlim(1950, 2020)
# plt.ylim(0, 180)

shape = plt.plot([])
line = shape[0]

hor = df["year"][650:708]
ver = df["inflation_annual_cpi"][650:708]

plt.fill_between(hor, ver, color="pink")
plt.xlim(1950, 2019)
plt.ylim(0, 80)


def init():
    plt.cla()
    # plt.plot(hor, ver)


def func(f):
    x = list(hor)
    y = list(ver)
    plt.plot(x[f], y[f], color="cyan")
    line.set_data(x, y)
    plt.bar(x[f], y[f], 10, color="darkblue")

    return line


move = anime.FuncAnimation(
    plt.gcf(), func, frames=len(hor), interval=200, init_func=init
)
# plt.tight_layout()
plt.show()
