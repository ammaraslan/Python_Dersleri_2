# [0,10] arasında y=x2 nin grafini ciziniz.

import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-10, 10, 100)
# y = x * x
#
# plt.plot(x, y)
# plt.show()


# [0,10] arasında y=x+2 nin grafini ciziniz.

x = np.linspace(0, 10, 5)

y = x + 2

# plt.plot(x, y,linestyle="--")
plt.plot(x, y,linestyle="-.",color="red", linewidth=2, alpha=0.5,marker="*")
plt.xlabel("X kordinayorü")
plt.ylabel("Y kordinayorü")
plt.title("BAŞLIK ALANI")

plt.show()
