import numpy as np
from numpy.linalg import norm

p1 = np.array([10, 10])
p2 = np.array([10, 10])
p3 = np.array([5, 7])

d = norm(np.cross(p2-p1, p1-p3))/norm(p2-p1)
print(d)
