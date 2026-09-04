# import numpy as np
# import matplotlib.pyplot as plt

# x=np.linspace(-5,5,100)
# y=np.random.rand(100)
# sq = np.sign(y)
# plt.plot(x,y, label='Random Values')
# plt.plot(x,sq, label='Sign Function')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Random Values and Sign Function')
# plt.legend()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

n=1000

x=np.linspace(0,1,n)
y=np.sin(2*np.pi*x*5)
y0=np.sign(y)

plt.figure(1)
# plt.subplot(2,1,1)
plt.plot(x,y, label='Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
plt.legend()

plt.figure(2)
# plt.subplot(2,1,2)
plt.plot(x,y0, label='Sign Function', color='orange')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sign Function')
plt.legend()

plt.figure(3)
plt.stem(x,y, label='Sign Function Stem', linefmt='orange', markerfmt='D', basefmt='k')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sign Function Stem Plot')
plt.legend()

plt.show()