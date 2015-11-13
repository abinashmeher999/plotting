import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import itemfreq

data = np.genfromtxt('LIWC2007 Results1.csv', dtype=None, delimiter='\t', names=True)
for column_name in data.dtype.names[2:]:
    tmp = itemfreq(data[column_name])
    x = tmp[:, 0]
    y = tmp[:, 1]
    plt.loglog(x, y, basex=10, basey=10)
    plt.show()
    # for y in data.dtype.names[2:]:
    #     plt.scatter(data[x], data[y])
    #     plt.title(x + ' vs ' + y)
    #     plt.show()
