import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 10
m = 1000
h = (b - a) / m
t = np.arange(a, b, 1)
t1 = np.arange(a, b, 1)

def f(x0, x1, h):
    d = (x1 - x0) / h
    return d

t = np.linspace(0, 10)
func=t**2
D = []
for i in range(0, m - 1):
    D.append(f(func[i], func[i+1], 1))

plt.plot(t1, D,t,2*t)
plt.show()
