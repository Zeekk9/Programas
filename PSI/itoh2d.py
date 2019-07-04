import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def itoh_2D(W):
    renglon, columna = W.shape
    phi = np.zeros(W.shape)
    psi = np.zeros(W.shape)
    phi[0, 0] = W[0, 0]
    # Se Desenvuelve la primera columna
    for m in range(1, columna):
        Delta = W[0, m] - W[0, m - 1]
        WDelta = np.arctan2(np.sin(Delta), np.cos(Delta))
        phi[0, m] = phi[0, m - 1] + WDelta
    psi[0, :] = phi[0, :]

    for k in range(columna):
        psi[0, k] = W[0, k]
        for p in range(1, renglon):
            Delta = W[p, k] - W[p - 1, k]
            WDelta = np.arctan2(np.sin(Delta), np.cos(Delta))
            phi[p, k] = phi[p - 1, k] + WDelta
    return phi
