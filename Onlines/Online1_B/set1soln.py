import numpy as np
import matplotlib.pyplot as plt

DT = 0.05  # sampling interval for the time axis
T_MIN, T_MAX = -np.pi, np.pi  # x(t) is defined only on this range


def generate_time_axis(t_min=T_MIN, t_max=T_MAX, dt=DT):
    return np.arange(t_min, t_max + dt / 2, dt)


def base_signal(t):
    x = np.sin(t)
    x[(t < T_MIN) | (t > T_MAX)] = 0
    return x


def interpolate_signal(t, x, query_t):

    # Signal is zero outside [-pi, pi]
    if query_t < T_MIN or query_t > T_MAX:
        return 0

    # Find nearest sample on the right
    right_index = np.searchsorted(t, query_t)

    # Exact sample found
    if right_index < len(t) and np.isclose(
        t[right_index], query_t
    ):
        return x[right_index]

    # Find nearest sample on the left
    left_index = right_index - 1

    # Missing sample:
    # average nearest left and right values
    interpolated_value = (
        x[left_index] + x[right_index]
    ) / 2

    return interpolated_value


def transform_signal(t, x, alpha, beta):

    # Create an empty output signal
    y = np.zeros(len(t))

    # Calculate y(t) = x(alpha*t + beta)
    for i in range(len(t)):

        # Transformed time
        query_t = alpha * t[i] + beta

        # Find signal value using interpolation
        y[i] = interpolate_signal(
            t,
            x,
            query_t
        )

    return y


def plot_signals(t, x, y, alpha, beta):

    plt.figure(figsize=(9, 5))

    plt.plot(
        t,
        x,
        label="x(t)",
        linewidth=2
    )

    plt.plot(
        t,
        y,
        label=f"y(t) = x({alpha}t + {beta})",
        linewidth=2,
        linestyle="--"
    )

    plt.title(
        "Time Scaling and Shifting of a Signal"
    )

    plt.xlabel("t")
    plt.ylabel("Amplitude")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


def main():

    t = generate_time_axis()
    x = base_signal(t)

    print(
        "Enter alpha and beta to plot "
        "y(t) = x(alpha*t + beta)."
    )

    print(
        "Type 'q' at any prompt to quit.\n"
    )

    while True:

        # Take alpha
        alpha = input("Enter alpha: ")

        # Exit for q
        if alpha.lower() == "q":
            break

        # Convert alpha to float
        alpha = float(alpha)

        # Alpha must be positive
        if alpha <= 0:
            print("Alpha must be greater than 0.\n")
            continue

        # Take beta
        beta = input("Enter beta: ")

        # Exit for q
        if beta.lower() == "q":
            break

        # Convert beta to float
        beta = float(beta)

        # Generate transformed signal
        y = transform_signal(
            t,
            x,
            alpha,
            beta
        )

        # Plot both signals
        plot_signals(
            t,
            x,
            y,
            alpha,
            beta
        )

    print("Exiting.")


if __name__ == "__main__":
    main()