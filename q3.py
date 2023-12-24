import numpy as np
import matplotlib.pyplot as plt

# Parâmetros fornecidos
g = 9.81  # Aceleração devida à gravidade (m/s^2)
T = 10.0  # Período da onda (s)
theta_0 = 35.0  # Ângulo de incidência em águas profundas (graus)
density = 992.0  # Densidade da água (kg/m^3)

# Funções para cálculos
def calculate_parameters():
    L0 = (g * T**2) / (2 * np.pi)
    C0 = L0 / T
    cg0 = (g * T) / (2 * np.pi)
    hc = C0**2 / g
    Hc = 0.5 * hc
    Lr = (C0 / cg0) * np.tan(np.radians(theta_0))
    xb = Lr**2 / (2 * hc)
    hb = hc + Hc
    Hb = Hc * (1 + 0.5 * (hb / hc))
    
    return xb, theta_0, hc, Hc, Hb

# Criar dados para o gráfico
xb_values = np.linspace(0, 1.2 * calculate_parameters()[0], 100)
theta_values = [theta_0] * len(xb_values)
Kr_values = [0.5 * (1 + np.tanh(x / calculate_parameters()[0])) for x in xb_values]
Ks_values = [1 / np.cosh(x / calculate_parameters()[0]) ** 2 for x in xb_values]
H_values = [calculate_parameters()[3] * (1 + 0.5 * (calculate_parameters()[2] / calculate_parameters()[3]))] * len(xb_values)

# Criar gráfico
fig, axs = plt.subplots(4, 1, figsize=(8, 10), sharex=True)

# Gráfico do ângulo da onda (theta)
axs[0].plot(xb_values, theta_values, label='Ângulo da Onda (θ)')
axs[0].set_ylabel('Ângulo (graus)')
axs[0].legend()

# Gráfico do coeficiente de refração (Kr)
axs[1].plot(xb_values, Kr_values, label='Coeficiente de Refração (Kr)')
axs[1].set_ylabel('Kr')
axs[1].legend()

# Gráfico do coeficiente de empolamento (Ks)
axs[2].plot(xb_values, Ks_values, label='Coeficiente de Empolamento (Ks)')
axs[2].set_ylabel('Ks')
axs[2].legend()

# Gráfico da altura da onda (H)
axs[3].plot(xb_values, H_values, label='Altura da Onda (H)')
axs[3].set_xlabel('Distância da Costa até Rebentação (m)')
axs[3].set_ylabel('Altura (m)')
axs[3].legend()

plt.tight_layout()
plt.show()
