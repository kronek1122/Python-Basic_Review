from matplotlib import pyplot as plt
import numpy as np
from numpy import random

# Line Charts
days = np.arange(0, 21)
other_site, real_python = days, days ** 2

plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks([0, 5, 10, 15, 20])
plt.xlabel('Days of reading')
plt.ylabel('Amount of Python Learned')
plt.title("Python Learned Reading Real Python vs Other Site")
plt.legend(['Other Site', 'Real Python'])
plt.show()

# Bar Charts
fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4,
}
plt.bar(fruits.keys(), fruits.values())
plt.show()

#Histograms
plt.hist(random.randn(10000),(20))
plt.savefig('hist.png')
plt.show()
