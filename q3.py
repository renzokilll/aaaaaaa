import numpy as np
import matplotlib.pyplot as plt

# Funções para calcular os parâmetros
def calcular_theta(theta_0, Kr, x):
    return np.arctan(Kr * np.sin(theta_0))

def calcular_Kr(g, lmbda, c):
    return np.sqrt(g * lmbda) / c

def calcular_Ks(Kr, hb):
    return Kr / np.tanh(Kr * hb)

# Parâmetros fornecidos
g = 9.81
H = 1.2
T = 7
theta_0 = np.radians(35)  # Convertendo para radianos
hb = 0.1465  # Valor calculado anteriormente
x_values = np.linspace(0, 91.37, 100)  # Valores de x de 0 a 91.37 m

# Calculando os parâmetros para cada valor de x
lmbda = (g * T**2) / (2 * np.pi)
theta_values = [np.degrees(calcular_theta(theta_0, calcular_Kr(g, lmbda, np.sqrt(g / lmbda)), x)) for x in x_values]
Kr_values = [calcular_Kr(g, lmbda, np.sqrt(g / lmbda)) for _ in x_values]
Ks_values = [calcular_Ks(Kr, hb) for Kr in Kr_values]
H_values = [H * np.sqrt(g / (lmbda) * np.tanh(lmbda * hb)) for _ in x_values]

# Plotando os gráficos
fig, axs = plt.subplots(4, 1, figsize=(8, 12))

axs[0].plot(x_values, theta_values, label=r'$\theta$')
axs[0].set_ylabel('Ângulo da Onda (graus)')
axs[0].legend()

axs[1].plot(x_values, Kr_values, label=r'$Kr$')
axs[1].set_ylabel('Coeficiente de Refração (Kr)')
axs[1].legend()

axs[2].plot(x_values, Ks_values, label=r'$Ks$')
axs[2].set_ylabel('Coeficiente de Empolamento (Ks)')
axs[2].legend()

axs[3].plot(x_values, H_values, label=r'$H$')
axs[3].set_xlabel('Distância da Costa (m)')
axs[3].set_ylabel('Altura da Onda (m)')
axs[3].legend()

plt.tight_layout()
plt.show()
