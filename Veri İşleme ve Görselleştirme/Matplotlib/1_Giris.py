import matplotlib.pyplot as plt


x = [2, 5, 1, 6]
y = [6, 4, 0, 6]
x1 = [3, 4, 9, 11]
y1 = [6, 5, 4, 0]
x2 = [1, 2, 3, 12]
y2 = [7, 1, 2, 3]

plt.bar(x, y)
plt.plot(x1, y1)
plt.scatter(x2, y2)

plt.ylabel("Y Başlık")
plt.xlabel("X Başlık")
plt.title("BAŞLIK ALANIDIR")
plt.show()

