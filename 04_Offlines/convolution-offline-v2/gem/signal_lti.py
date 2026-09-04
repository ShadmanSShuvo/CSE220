import numpy as np


def readable_time_ticks(time_values, max_labels=18):
    if len(time_values) <= max_labels:
        return time_values

    step = int(np.ceil(len(time_values) / max_labels))
    ticks = time_values[::step]

    if ticks[-1] != time_values[-1]:
        ticks.append(time_values[-1])

    return ticks


class DiscreteSignal:
    """Finite discrete-time signal with integer indices."""

    def __init__(self, start_time, end_time):
        if start_time > end_time:
            raise ValueError(
                f"start_time ({start_time}) must be <= end_time ({end_time})"
            )
        self.start_time = int(start_time)
        self.end_time = int(end_time)
        self.values = [0.0] * (self.end_time - self.start_time + 1)

    def __len__(self):
        return len(self.values)

    def times(self):
        return range(self.start_time, self.end_time + 1)

    def get_value_at_time(self, t):
        if self.start_time <= t <= self.end_time:
            return float(self.values[t - self.start_time])
        return 0.0

    def set_value_at_time(self, t, value):
        if not (self.start_time <= t <= self.end_time):
            raise ValueError(
                f"Time index {t} is outside range [{self.start_time}, {self.end_time}]"
            )
        self.values[t - self.start_time] = float(value)

    def shift(self, k):
        new_signal = DiscreteSignal(self.start_time + k, self.end_time + k)
        new_signal.values = [float(v) for v in self.values]
        return new_signal

    def add(self, other):
        new_start = min(self.start_time, other.start_time)
        new_end = max(self.end_time, other.end_time)
        result = DiscreteSignal(new_start, new_end)
        for t in result.times():
            val = self.get_value_at_time(t) + other.get_value_at_time(t)
            result.set_value_at_time(t, val)
        return result

    def multiply(self, scalar):
        result = DiscreteSignal(self.start_time, self.end_time)
        result.values = [float(v * scalar) for v in self.values]
        return result

    def nonzero_samples(self, tolerance=1e-12):
        result = []
        for t in self.times():
            val = self.get_value_at_time(t)
            if abs(val) > tolerance:
                result.append((t, val))
        return result

    def plot(self, title, save_path=None, ax=None):
        import matplotlib.pyplot as plt

        if ax is None:
            _, ax = plt.subplots()

        time_values = list(self.times())
        markerline, stemlines, baseline = ax.stem(time_values, self.values)
        markerline.set_markersize(6)
        baseline.set_color("black")
        baseline.set_linewidth(1)

        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_title(title)
        ax.set_xlabel("n")
        ax.set_ylabel("value")
        ax.grid(True, alpha=0.35)
        ax.set_xticks(readable_time_ticks(time_values))
        ax.tick_params(axis="x", labelsize=9)

        if save_path is not None:
            plt.savefig(save_path, bbox_inches="tight", dpi=150)

        return ax


class LTISystem:
    """Discrete-time LTI system described by a finite impulse response."""

    def __init__(self, impulse_response):
        self.impulse_response = impulse_response

    def output_range(self, input_signal):
        start = input_signal.start_time + self.impulse_response.start_time
        end = input_signal.end_time + self.impulse_response.end_time
        return (start, end)

    def get_response_components(self, input_signal):
        components = []
        for k, x_k in input_signal.nonzero_samples():
            comp_signal = self.impulse_response.shift(k).multiply(x_k)
            components.append((k, comp_signal))
        return components

    def output_by_superposition(self, input_signal):
        start, end = self.output_range(input_signal)
        y = DiscreteSignal(start, end)
        components = self.get_response_components(input_signal)
        for _, comp_signal in components:
            y = y.add(comp_signal)
        return y

    def get_contributions_at_time(self, input_signal, n):
        contributions = []
        for k in input_signal.times():
            x_k = input_signal.get_value_at_time(k)
            h_n_minus_k = self.impulse_response.get_value_at_time(n - k)
            prod = x_k * h_n_minus_k
            if abs(prod) > 1e-12:
                contributions.append((k, float(x_k), float(h_n_minus_k), float(prod)))
        return contributions

    def output_at_time(self, input_signal, n):
        val = 0.0
        for k in input_signal.times():
            val += input_signal.get_value_at_time(k) * self.impulse_response.get_value_at_time(n - k)
        return float(val)

    def output(self, input_signal):
        start, end = self.output_range(input_signal)
        y = DiscreteSignal(start, end)
        for n in range(start, end + 1):
            y.set_value_at_time(n, self.output_at_time(input_signal, n))
        return y