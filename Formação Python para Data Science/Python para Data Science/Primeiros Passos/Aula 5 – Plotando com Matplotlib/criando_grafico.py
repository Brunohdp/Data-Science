import matplotlib.pyplot as plt
from random import randrange

notas_matematicas = []
for notas in range(8):
  notas_matematicas.append(randrange(0, 11))

x = list(range(1,9))
y = notas_matematicas
plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()