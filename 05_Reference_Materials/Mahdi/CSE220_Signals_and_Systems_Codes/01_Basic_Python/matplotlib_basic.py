import matplotlib.pyplot as plt
import numpy as np
# xs = np.array([1,2,3,7,10])
# ys = np.array([12,32,23,40,39])
# plt.subplot(2,1,1) #row,column, plot_no 1
# plt.plot(xs,ys, marker='o', linestyle='--', color = 'red')

# plt.subplot(2,1,2)
# xs = np.array([1,2,6,7,1])
# ys = np.array([10,50,20,35,42])
# plt.xlabel('Time')
# plt.ylabel('y')
# plt.plot(xs,ys, marker='o', linestyle='--', color = 'g')
# plt.show()

# xs = np.array([1,2,3,7,10])
# ys = np.array([12,32,23,40,39])
# sizes = np.array([6]*5)
# plt.scatter(xs,ys,sizes)
# plt.show()

# plt.bar(xs,ys)
# plt.show()

# plt.barh(xs,ys)
# plt.show()

# labels = ['a','b','c','d','e']
# plt.pie(ys,labels = labels)
# plt.show()

sampling_f = 1000
t = np.linspace(0,1,sampling_f) # 0 theke 1 e 1000 points nibo
f = 5
y = np.sin(2*np.pi*f*t)
plt.figure(1)
plt.plot(t,y, color = 'red')
plt.grid(True)

plt.figure(2)
square_wave = np.sign(y)
plt.plot(t,square_wave)
plt.show()
