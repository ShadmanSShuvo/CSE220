import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 30)
y = np.power(x, 2)
yy = np.power(x, 3)
sizes = np.arange(1, 31) * 3
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.tan(x)


plt.subplot(2, 1, 1)
plt.scatter(x, y, s=sizes, marker='o', linestyle='--', color='r', label='y = x^2')
plt.xlabel('x')
plt.ylabel('y')
# plt.title('Plot of y = x^2')
# plt.plot(x, y1, label='sin(x)')
# plt.plot(x, y2, label='cos(x)')
# plt.plot(x, y3, label='tan(x)')
plt.legend()
# plt.grid(True)



plt.subplot(2, 1, 2)
plt.scatter(x, yy, s=sizes, marker='o', linestyle='--', color='g', label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
# plt.title('Plot of y = x^3')
plt.legend()
# plt.grid(True)

plt.show()