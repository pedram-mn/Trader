import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


#def plotting():
def animate(i):
    data = pd.read_csv("price_log.csv")[-271:]
    times = [time[-8:] for time in data["Date"]]
    x_var = times
    y_var = data["Price($)"]
    plt.cla()
    plt.title("Ethereum price ($) - 10 minutes", color="#EDEE11")
    plt.xlabel("Time(UTC+3:30)", color="#EDEE11")
    plt.ylabel("Price ($)", color="#EDEE11")
    plt.plot(x_var, y_var, "-o", markevery=[-1], color="green")
    ax = plt.gca()
    ax.set_facecolor("#0e0d3c")
    ax = plt.gcf()
    ax.set_facecolor("#0d0228")
    plt.grid(color="#87877a", linestyle='dotted', linewidth=0.5)
    plt.xticks([0, 30, 60, 90, 120, 150, 180, 210, 240, 270], rotation=90, color="#9d000a")
    plt.yticks(color="#9d000a")
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=2000)
plt.show()
