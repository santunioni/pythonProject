import numpy as np
import matplotlib.pyplot as plt


angles = np.arange(0, 50, step=0.001)
percentages = np.divide(100, np.cos(angles*2*np.pi/360)) - 100

plt.grid()
plt.title('Porcentagem por ângulo')
plt.xlabel('Ângulo do telhado')
plt.ylabel('Percentagem a mais de área necessária')
plt.plot(angles, percentages, lw=3, color='darkred')
plt.xticks([0, 10, 20, 30, 40, 50], ['0°', '10°', '20°', '30°', '40°', '50°'])
plt.yticks([0, 10, 20, 30, 40, 50], ['+0%', '+10%', '+20%', '+30%', '+40%', '+50%'])
plt.show()
#plt.savefig('percentagem.png')
