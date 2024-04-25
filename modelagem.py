import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def function(t):
    return 2 * (t >= 0) + 0.70710678 * np.exp(-100 * t) * np.cos(100 * t + 4 * np.pi / 3)

# Criando um array de tempo de 0 a 0.05 segundos com passo de 0.0001 segundos
t = np.arange(0, 0.05, 0.0001)

# Calculando os valores da função para cada ponto de tempo
y = function(t)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='2u(t) + 0,70710678e^(-100t)cos(100t+4pi/3)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Comportamento da função ao longo do tempo')
plt.grid(True)
plt.legend()
plt.show()