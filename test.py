import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

plt.tight_layout()
plt.savefig("p1.png")

x = np.linspace(-10, 10, 100)

fig, ax = plt.subplots()
ax.set_ylim(-10, 10)
ax.set_xlim(-10, 10)
ax.plot(x, x, label='linear')
ax.plot(x**3, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('vasic graphs')
ax.legend()
ax.axvline(x=0, color='grey', lw=0.5)
ax.axhline(y=0, color='grey', lw=0.5)

plt.tight_layout()
plt.savefig("p2.png")


data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

plt.tight_layout()
plt.savefig("p3.png")

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.savefig("p4.png")

x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]
variance = [1, 2, 7, 4, 2, 3]

x_pos = [i for i, _ in enumerate(x)]

fig2, ax2 = plt.subplots()
ax2.barh(x_pos, energy, color='green', xerr=variance)
ax2.set_ylabel("Energy Source")
ax2.set_xlabel("Energy Output (GJ)")
ax2.set_title("Energy Output by Source")

ax2.set_yticks(x_pos, x)
plt.tight_layout()
plt.savefig("p5.png")

N = 5
men_means = (20, 35, 30, 35, 27)
women_means = (25, 32, 34, 20, 25)
ind = np.arange(N)  # the x locations for the groups
width = 0.35  # the width of the bars
fig3, ax3 = plt.subplots()
ax3.bar(ind, men_means, width, label='Men')
ax3.bar(ind + width, women_means, width, label='Women')
ax3.set_ylabel('Scores')
ax3.set_title('Scores by group and gender')
ax3.set_xticks(ind + width / 2, labels=('G1', 'G2', 'G3', 'G4', 'G5'))
ax3.legend(loc='best')
plt.tight_layout()
plt.savefig("p6.png")

countries = ['USA', 'Canada', 'Mexico', 'Germany', 'France']
bronzes = np.array([10, 15, 5, 20, 25])
silvers = np.array([20, 25, 15, 30, 35])
golds = np.array([30, 35, 25, 40, 45])
ind = [x for x, _ in enumerate(countries)]

fig4, ax4 = plt.subplots()
ax4.bar(ind, bronzes, label='Bronze', color='brown')
ax4.bar(ind, silvers, bottom=bronzes, label='Silver', color='silver')
ax4.bar(ind, golds, bottom=bronzes + silvers, label='Gold', color='gold')
ax4.set_ylabel('Medals')
ax4.set_title('Medals by Country')
ax4.set_xticks(ind, countries)
ax4.legend(loc='best')
plt.tight_layout()
plt.savefig("p7.png")


import pandas as pd
from pandas.plotting import parallel_coordinates
df = pd.read_csv('Book1.csv')  # Updated path to match your workspace
print(df)
plt.figure()
parallel_coordinates(df, 'Type', colormap=plt.get_cmap("Set2"), alpha=0.5, linewidth=2)
plt.title('Parallel Coordinates Plot')
plt.xlabel('Features')
plt.ylabel('Values')
plt.tight_layout()
plt.savefig("p8.png")