import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi, 100)

# y = np.random.randint(0, 100, size=(50))
y = np.sin(x)


x1 = np.linspace(-np.pi, np.pi, 100)
y1 = np.cos(x)

plt.plot(x, y)
plt.plot(x1, y1)
plt.show()




