import numpy as np
import matplotlib.pyplot as plt


def readable_time_ticks(time_values, max_labels=18):
    if len(time_values) <= max_labels:
        return time_values

    step = int(np.ceil(len(time_values) / max_labels))
    ticks = list(time_values[::step])

    if ticks[-1] != time_values[-1]:
        ticks.append(time_values[-1])

    return ticks


class DiscreteSignal:
    """Finite discrete-time signal with integer indices."""

    def __init__(self, start_time, end_time):
        self.start_time = int(start_time)
        self.end_time = int(end_time)
        self.values = np.zeros(self.end_time - self.start_time + 1, dtype=float)

    def __len__(self):
        return len(self.values)

    def times(self):
        return range(self.start_time, self.end_time + 1)

    def get_value_at_time(self, t):
        if t > self.end_time or t < self.start_time:
            return 0.0
        return float(self.values[t - self.start_time])

    def set_value_at_time(self, t, value):
        if t > self.end_time or t < self.start_time:
            raise ValueError(f"t={t} is outside the signal's stored range [{self.start_time}, {self.end_time}]")
        self.values[t - self.start_time] = float(value)

    def shift(self, k):
        new_signal = DiscreteSignal(self.start_time + k, self.end_time + k)
        for t in self.times():
            new_signal.set_value_at_time(t + k, self.get_value_at_time(t))
        return new_signal

    def add(self, other):
        new_start = min(self.start_time, other.start_time)
        new_end = max(self.end_time, other.end_time)
        new_signal = DiscreteSignal(new_start, new_end)
        for t in new_signal.times():
            new_signal.set_value_at_time(t, self.get_value_at_time(t) + other.get_value_at_time(t))
        return new_signal

    def multiply(self, scalar):
        new_signal = DiscreteSignal(self.start_time, self.end_time)
        for t in self.times():
            new_signal.set_value_at_time(t, scalar * self.get_value_at_time(t))
        return new_signal

    def nonzero_samples(self, tolerance=1e-12):
        result = []
        for t in self.times():
            val = self.get_value_at_time(t)
            if abs(val) > tolerance:
                result.append((t, val))
        return result

    def plot(self, title="Discrete Signal", save_path=None, ax=None):
        show_later = False
        if ax is None:
            _, ax = plt.subplots(figsize=(7, 4))
            show_later = True

        time_values = list(self.times())
        markerline, stemlines, baseline = ax.stem(time_values, self.values)
        markerline.set_markersize(6)
        baseline.set_color("black")
        baseline.set_linewidth(1)

        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_title(title)
        ax.set_xlabel("n")
        ax.set_ylabel("Amplitude")
        ax.grid(True, alpha=0.35)
        ax.set_xticks(readable_time_ticks(time_values))
        ax.tick_params(axis="x", labelsize=9)

        if save_path is not None:
            plt.savefig(save_path, bbox_inches="tight", dpi=150)
        elif show_later:
            pass

        return ax


class LTISystem:
    """Discrete-time LTI system described by a finite impulse response."""

    def __init__(self, impulse_response: DiscreteSignal):
        self.impulse_response = impulse_response

    def output_range(self, input_signal: DiscreteSignal):
        return (
            input_signal.start_time + self.impulse_response.start_time,
            input_signal.end_time + self.impulse_response.end_time,
        )

    def output_at_time(self, input_signal: DiscreteSignal, n: int):
        val = 0.0
        for k in input_signal.times():
            val += input_signal.get_value_at_time(k) * self.impulse_response.get_value_at_time(n - k)
        return float(val)

    def output(self, input_signal: DiscreteSignal):
        start, end = self.output_range(input_signal)
        y = DiscreteSignal(start, end)
        for n in range(start, end + 1):
            y.set_value_at_time(n, self.output_at_time(input_signal, n))
        return y
