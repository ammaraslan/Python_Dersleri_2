# hiperbolik tan ve tan grafiklerini çizib aralık -pi ile +pi arasını referans alınız.

import numpy as np
import matplotlib.pyplot as plt

# aralık linspace

x = np.linspace(-np.pi, np.pi, 100)

y1 = np.tanh(x)
y2 = np.tan(x)
resim = plt.figure(dpi=600)
resim.set_size_inches(20, 5)

plt.plot(x, y1, color="blue")
# plt.plot(x, y2, color="red")
plt.show()
resim.savefig("tanh.svg")
