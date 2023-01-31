import csv
import matplotlib.pyplot as plt
from pathlib import Path


def plot_pirates_vs_temperatures(path):
    temperatures = []
    pirates = []

    with open(path, "r") as file:
        reader = csv.reader(file)
        next(reader) # pomijanie pierwszego wiersza
        for year, temperature, pirate_count in reader:
            temperatures.append(float(temperature))
            pirates.append(int(pirate_count))

    plt.plot(pirates, temperatures, 'r-o')
    plt.title("Global temperature as a function of pirate population")
    plt.xlabel("Total pirates")
    plt.ylabel("Average global temperature (Celsius)")

    plt.savefig('graph.png')
    plt.show()

plot_pirates_vs_temperatures(Path.home() / 'python-basics-exercises-master' 
/ 'ch17-scientific-computing-and-graphing' 
/ 'practice_files'
/ 'pirates.csv')
