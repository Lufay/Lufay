import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import scipy.constants as C
import scipy.optimize as op
import scipy.sparse as sp
import scipy.sparse.csgraph as g
from math import cos

# arr = np.array([
#   [0, 1, 0],
#   [1, 0, 0],
#   [0, 0, 0]
# ])

# arr = np.mat([
#     [
#     random.randrange(2) if j > i else 0 for j in range(10)
#     ] for i in range(10)
# ])
# print(arr)
# newarr = sp.csr_matrix(arr)

# n = g.connected_components(newarr, return_labels=False)
# # if n == 1:
# print(n)
# k = 3
# print(g.dijkstra(newarr, False, range(k), return_predecessors=True))
# print(g.dijkstra(newarr, False, range(k), return_predecessors=True, min_only=True))    # [0, 7], 
# # else:
# g.breadth_first_order()

def get_f(total, per, last, n):
    def f(x):
        k = total * (1+x)**n - last
        for i in range(1, n):
            k -= per * (1+x)**i
        return k
    return f

# month = op.root(get_f(44000, 1833.33+90, 1833.41+180.4, 24), 0.01).x[0]
# year = (1+month)**12-1
# print(month*100, year*100)

month = op.root(get_f(50000, 8421.07, 8421.05, 6), 0.01).x[0]
year = (1+month)**12-1
print(month*100, year*100)



# x = np.arange(-15,2,0.1)
# Ai, Aip, Bi, Bip = sp.airy(x)
# ax1 = plt.subplot(1, 2, 1)
# ax2 = plt.subplot(1, 2, 2)
# ax1.plot(x, Ai)
# ax1.plot(x, Aip)
# ax2.plot(x, Bi)
# ax2.plot(x, Bip)
# ax2.spines['left'].set_position(('outward', -20))
# plt.show()