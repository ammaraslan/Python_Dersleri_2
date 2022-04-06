import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 10, size=20)
y = np.random.randint(0, 5, size=20)
x1 = np.random.randint(0, 10, size=20)
y1 = np.random.randint(0, 7, size=20)

plt.bar(x, y,color="red")
plt.bar(x1, y1)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()