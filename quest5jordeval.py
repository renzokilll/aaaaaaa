import numpy as np
import matplotlib.pyplot as plt

# Parâmetros dados
H13 = 2.6  # Altura significativa H1/3 em metros
Tp = 8.0   # Período de pico em segundos
g = 9.81   # Aceleração devido à gravidade em m/s^2
m0 = (H13 / 4.0)**2  # Momento espectral

# Frequências
frequencies = np.linspace(0.01, 1.0, 1000)  # Frequências de 0.01 Hz a 1.0 Hz

# Espectro JONSWAP
sigma = 0.07 if Tp <= 10 else 0.09  # Parâmetro sigma
omega = 2 * np.pi / Tp  # Frequência angular de pico
S = m0 * (1.25 / omega**4) * frequencies**(-5) * np.exp(-(5 / 4) * (frequencies / omega)**(-4)) * \
    np.exp(-0.5 * (frequencies / sigma)**2)

# Gráfico do espectro JONSWAP
plt.figure(figsize=(10, 6))
plt.plot(frequencies, S, label='Espectro JONSWAP')
plt.title('Espectro JONSWAP')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Densidade Espectral de Potência (m^2/Hz)')
plt.legend()
plt.grid(True)
plt.show()

# Verificação da relação Hm0/σ ≈ 4sqrt(m0)
Hm0 = 4 * np.sqrt(m0)
sigma_check = H13 / Hm0

# Exibição dos resultados
print(f"Relação Hm0/σ: {Hm0:.4f}")
print(f"4 * sqrt(m0): {4 * np.sqrt(m0):.4f}")
print(f"Verificação da relação Hm0/σ ≈ 4sqrt(m0): {sigma_check:.4f}")
