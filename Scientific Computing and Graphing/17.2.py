from matplotlib import pyplot as plt
import numpy as np


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