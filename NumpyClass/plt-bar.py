import numpy as np
import matplotlib.pyplot as plt
n=11
x = np.linspace(0, 10, n)
y = np.random.rand(n)

# plt.barh(x, y)
#plt.bar(x, y)#, color='blue', alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot Example')
# plt.pie(x)
plt.pie(y)
plt.show()