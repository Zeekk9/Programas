# importing the packages
import numpy as np
import matplotlib.pyplot as plt

# Defining the delta function


def delta(n):
    if n == 0:
        return 1
    else:
        return 0

# Defining lists


h_ = []
x_ = []
y_ = []
n = 7

# Writing the h[n] function in terms of delta function
for i in range(-n, n+1):
    h = delta(i) + delta(i-1) + delta(i-4) + delta(i-5)
    h_.append(h)

# Plotting the h[n] function
plt.figure(1)
plt.stem(range(-n, n+1), h_, '--')


plt.show()
