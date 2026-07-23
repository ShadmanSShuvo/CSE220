import numpy as np
import matplotlib.pyplot as plt

class DiscreteSignal:
    def __init__(self, start_time, end_time):
        self.t = np.arange(start_time, end_time + 1, 1)
        self.x = np.zeros(end_time - start_time + 1)

    def set_value_at_time(self, t, value):
        if t in self.t:
            idx = np.where(self.t == t)[0][0]
            self.x[idx] = value
        else:
            print(f"Time {t} is out of bounds for this signal.")
    
    def get_value_at_time(self, t):
        if t > self.t.max() or t < self.t.min():
            return 0
        # FIXED: Changed self.np to np, and added conditional lookup matching self.t
        idx = np.where(self.t == t)[0][0]
        return self.x[idx]
    
    def shift(self, k):
        self.t = self.t + k

class LTISystem:
    def __init__(self, s: DiscreteSignal):
        self.s = s
    
    def output(self, h: DiscreteSignal):
        start_out = self.s.t.min() + h.t.min()
        end_out = self.s.t.max() + h.t.max()
        

        y = DiscreteSignal(start_out, end_out)
        sum = 0
        for n in range(start_out, end_out + 1):
            total_sum = 0
            # Iterate over the valid time range of the input signal s
            for k in range(self.s.t.min(), self.s.t.max() + 1):
                total_sum += self.s.get_value_at_time(k) * h.get_value_at_time(n - k)
                sum += total_sum
            y.set_value_at_time(n, total_sum)
            
        return y, sum

# Define input signal S
S = DiscreteSignal(1, 9)
values_S = [5, 2, 6, 5, 9, 3, 1, 6, 7]
for t_val, x_val in zip(range(1, 10), values_S):
    S.set_value_at_time(t_val, x_val)

# Define impulse response h
h = DiscreteSignal(1, 5)
values_h = [15, 5, 9, 3, 4]
for t_val, x_val in zip(range(1, 6), values_h):
    h.set_value_at_time(t_val, x_val)

# Compute response through LTI System
lti = LTISystem(S)
output_signal, sum = lti.output(h)

# Print the resulting convolved signal values
print("Output Time Indices:", output_signal.t)
print("Output Signal Values:", output_signal.x)
print("convolution: ", sum )

# Plotting the result
plt.figure(1)
plt.scatter(S.t, S.x, label = "input signal")
plt.scatter(h.t, h.x, label = "impulse signal")


plt.figure(2)
plt.stem(output_signal.t, output_signal.x)
plt.title("LTI System Output (Convolution)")
plt.xlabel("Time (n)")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()
