import numpy as np
import matplotlib.pyplot as plt

n=1000

x=np.linspace(0,1,n)
y0=np.sin(2*np.pi*x)
y1=np.cos(2*np.pi*x)
y=np.sin(2*np.pi*x)+0.1*np.random.randn(n)

# plt.subplot(2,1,1)
# plt.plot(x,y1, label='Cosine')
plt.plot(x,y, label='Noisy Sine')
plt.plot(x,y0, label='Sine')
# plt.title('Sine and Cosine Waves with Noise')
plt.legend()
# plt.subplot(2,1,2)
# plt.hist(y,bins=30)
# plt.title('Histogram of Noisy Sine Wave')
# plt.tight_layout()
plt.show()