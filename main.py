import numpy as np
from time import time

m = np.matrix([[2, 2, 3], [-1, 1, 1], [-1, 3, 5]])

start_time = time()
det = np.linalg.det(m)
end_time = time()
print(det)
eleapse_time = end_time - start_time
print("Elapsed time: %0.10f seconds." % eleapse_time)
print()

start_time = time()
inv = np.linalg.inv(m)
end_time = time()
print(inv)
eleapse_time = end_time - start_time
print("Elapsed time: %0.10f seconds." % eleapse_time)
print()