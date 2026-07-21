import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
q = 1 / 2.0
K = 2 / 3.0
g = 9.8
l = g
# tamaño de paso
dt = 0.04

# Numero de iteraciones
N = 2000

# La funcion nececita ser llamada con Fd
# Los valores del problema son Fd=0,0.1,1.2
def Euler_Cromer_pendulo(Fd):
    # Listas vacias
    omega = []
    theta = []
    t = []
    # Condiciones iniciales
    omega.append(0)
    theta.append(0.2)
    t.append(0)
    # Metodo de Euler Cromer
    for i in range(0, N + 1):
        omega.append(omega[i]+dt*(-g/l*np.sin(theta[i]) -
                                  q*omega[i]+Fd*np.sin(K*dt*(i-1))))
        theta.append(theta[i] + dt * omega[i + 1])
        t.append(dt * i)
    return theta, t


a = Euler_Cromer_pendulo(0)
theta_a = a[0]
t_a = a[1]
plt.plot(t_a, theta_a)
plt.title('$F_d=0rad$', fontsize='20')
plt.grid()
plt.show()

b = Euler_Cromer_pendulo(0.1)
theta_b = b[0]
t_b = b[1]
plt.plot(t_b, theta_b)
plt.title('$F_d=0.1rad$', fontsize='20')
plt.grid()
plt.show()

c = Euler_Cromer_pendulo(1.2)
theta_c = c[0]
t_c = c[1]
plt.plot(t_c, theta_c)
plt.title('$F_d=1.2rad$', fontsize='20')
plt.grid()
plt.show()
