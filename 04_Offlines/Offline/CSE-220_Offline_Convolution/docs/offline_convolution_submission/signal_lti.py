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

    # Create a finite discrete-time signal over the given integer range.
    def __init__(self, start_time, end_time):
        if end_time < start_time:
            raise ValueError("end_time must be >= start_time")
        self.start_time = start_time
        self.end_time = end_time
        self.values = [0.0] * (end_time - start_time + 1)

    # Return the number of stored samples in the signal.
    def __len__(self):
        return len(self.values)

    # Return the integer time indices covered by the signal.
    def times(self):
        return range(self.start_time, self.end_time + 1)

    # Return the signal value at the given time index.
    def get_value_at_time(self, t):
        if t < self.start_time or t > self.end_time:
            return 0.0
        return self.values[t - self.start_time]

    # Set the signal value at the given time index.
    def set_value_at_time(self, t, value):
        if t < self.start_time or t > self.end_time:
            raise IndexError(
                f"time {t} is outside stored range [{self.start_time}, {self.end_time}]"
            )
        self.values[t - self.start_time] = value

    # Return a shifted copy of the signal representing x[n - k].
    def shift(self, k):
        shifted = DiscreteSignal(self.start_time + k, self.end_time + k)
        shifted.values = list(self.values)
        return shifted

    # Return the sum of this signal and another signal.
    def add(self, other):
        new_start = min(self.start_time, other.start_time)
        new_end = max(self.end_time, other.end_time)
        result = DiscreteSignal(new_start, new_end)
        for n in result.times():
            result.set_value_at_time(
                n, self.get_value_at_time(n) + other.get_value_at_time(n)
            )
        return result

    # Return a scaled copy of the signal.
    def multiply(self, scalar):
        result = DiscreteSignal(self.start_time, self.end_time)
        result.values = [v * scalar for v in self.values]
        return result

    # Return the nonzero samples of the signal.
    def nonzero_samples(self, tolerance=1e-12):
        samples = []
        for n in self.times():
            value = self.get_value_at_time(n)
            if abs(value) > tolerance:
                samples.append((n, value))
        return samples

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

    # Store the impulse response that defines the LTI system.
    def __init__(self, impulse_response):
        self.impulse_response = impulse_response

    # Return the output time range for the convolution result.
    def output_range(self, input_signal):
        start = input_signal.start_time + self.impulse_response.start_time
        end = input_signal.end_time + self.impulse_response.end_time
        return start, end

    # Return all shifted and scaled impulse-response components for the input.
    def get_response_components(self, input_signal):
        components = []
        for k, x_k in input_signal.nonzero_samples():
            component = self.impulse_response.shift(k).multiply(x_k)
            components.append(component)
        return components

    # Return the system output using superposition of response components.
    def output_by_superposition(self, input_signal):
        start, end = self.output_range(input_signal)
        result = DiscreteSignal(start, end)

        components = self.get_response_components(input_signal)
        for component in components:
            result = result.add(component)

        return result

    # Return the nonzero product terms that contribute to one output sample.
    def get_contributions_at_time(self, input_signal, n):
        contributions = []
        for k, x_k in input_signal.nonzero_samples():
            h_value = self.impulse_response.get_value_at_time(n - k)
            if h_value != 0:
                contributions.append((k, x_k * h_value))
        return contributions

    # Return one output sample of the LTI system.
    def output_at_time(self, input_signal, n):
        total = 0.0
        for k in input_signal.times():
            x_k = input_signal.get_value_at_time(k)
            if x_k != 0:
                total += x_k * self.impulse_response.get_value_at_time(n - k)
        return total

    # Return the complete output signal of the LTI system.
    def output(self, input_signal):
        start, end = self.output_range(input_signal)
        result = DiscreteSignal(start, end)

        for n in result.times():
            result.set_value_at_time(n, self.output_at_time(input_signal, n))

        return result
