import numpy as np
import matplotlib.pyplot as plt


V_hat = np.linspace(0.4, 20.0, 1000)
T_hat = [1.15, 1.0, 0.85]
for i in T_hat:
    p_hat = 8.0*i/(3.0*V_hat - 1.0) - 3.0/(V_hat**2)
    plt.plot(V_hat, p_hat)
    plt.xlabel("Normalised Volum $\\hat{V} = \\frac{V}{V_c}$")
    plt.ylabel("Normalised pressure $\\hat{p} = \\frac{p}{p_c}$")
plt.legend(["$\\hat{T} = 1.15$", "$\\hat{T} = 1.0$", "$\\hat{T} = 0.85$"])
plt.show()
