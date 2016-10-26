import numpy as np
import matplotlib.pyplot as plt


rho_hat = np.linspace(0.0, 2.0, 1000)
T_hat = [1.15, 1.0, 0.85]
for i in T_hat:
    p_hat = 8.0*rho_hat*i/(3.0 - rho_hat) - 3.0*rho_hat**2
    plt.plot(rho_hat, p_hat)
    plt.xlabel("Normalised density $\\hat{\\rho} = \\frac{1}{\\hat{V}}$")
    plt.ylabel("Normalised pressure $\\hat{p} = \\frac{p}{p_c}$")
plt.legend(["$\\hat{T} = 1.15$", "$\\hat{T} = 1.0$", "$\\hat{T} = 0.85$"])
plt.show()
