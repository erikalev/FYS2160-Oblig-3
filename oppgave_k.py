import numpy as np
import matplotlib.pyplot as plt

T = 0.9
rho = np.linspace(0.2, 2.0, 1000)

p = 8*rho*T/(3 - rho) - 3*rho**2
V = 1/rho
g = -3*rho - 8.0/3.0*T*np.log(3.0/rho - 1) + p/rho

plt.subplot(3, 1, 1)
plt.plot(rho, p, label = "$\\hat{p}(\\hat{\\rho})$")
rho_line = [[0.425614, 0.916972, 1.65726], [0.6470, 0.6470, 0.6470]]
#plt.plot(rho_line[0], rho_line[1], label="Critical pressure")
plt.legend()
plt.xlabel("$\\hat{\\rho}$")
plt.ylabel("$\\hat{p}$")

plt.subplot(3, 1, 2)
V_line = [[0.6470, 0.6470, 0.6470], [0.611328, 1.0944, 2.34894]]
plt.plot(p, V, label = "$\\hat{V}(\\hat{p})$")
#plt.plot(V_line[0], V_line[1], label="Critical pressure")
plt.legend()
plt.xlabel("$\\hat{p}$")
plt.ylabel("$\\hat{V}$")

plt.subplot(3, 1, 3)
plt.plot(p, g, label = "$\\hat{g}(\\hat{p})$")
plt.legend(loc=2)
plt.xlabel("$\\hat{p}$")
plt.ylabel("$\\hat{g}$")

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()
