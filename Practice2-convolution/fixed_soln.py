import numpy as np
import matplotlib.pyplot as plt


class DiscreteSignal:
    def __init__(self, start_time, end_time):
        self.t = np.arange(start_time, end_time + 1)
        self.x = np.zeros(len(self.t))

    def set_value_at_time(self, t, value):
        if t in self.t:
            idx = np.where(self.t == t)[0][0]
            self.x[idx] = value

    def get_value_at_time(self, t):
        if t < self.t.min() or t > self.t.max():
            return 0
        idx = np.where(self.t == t)[0][0]
        return self.x[idx]

    def shift(self, k):
        shifted = DiscreteSignal(self.t.min() + k,
                                 self.t.max() + k)
        shifted.x = self.x.copy()
        return shifted


class LTISystem:
    def __init__(self, h):
        self.h = h

    def output(self, input_signal):

        start = input_signal.t.min() + self.h.t.min()
        end = input_signal.t.max() + self.h.t.max()

        y = DiscreteSignal(start, end)

        for n in range(start, end + 1):

            value = 0

            for k in range(input_signal.t.min(),
                           input_signal.t.max() + 1):

                value += (input_signal.get_value_at_time(k) *
                          self.h.get_value_at_time(n - k))

            y.set_value_at_time(n, value)

        return y


# ---------------- Example ----------------

S = DiscreteSignal(1, 9)
values_S = [5, 2, 6, 5, 9, 3, 1, 6, 7]

for t, v in zip(range(1, 10), values_S):
    S.set_value_at_time(t, v)


h = DiscreteSignal(1, 5)
values_h = [15, 5, 9, 3, 4]

for t, v in zip(range(1, 6), values_h):
    h.set_value_at_time(t, v)


lti = LTISystem(h)
y = lti.output(S)

print("Output Time:", y.t)
print("Output Values:", y.x)

plt.figure(figsize=(8,4))
plt.stem(y.t, y.x)
plt.title("Convolution Output")
plt.grid(True)
plt.show()
