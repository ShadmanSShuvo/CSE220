import numpy as np
import matplotlib.pyplot as plt


def base_signal(t):
    x = np.exp(-t) * np.cos(t)

    # Signal is zero outside [-pi, pi]
    x[(t < -np.pi) | (t > np.pi)] = 0

    return x


def transform_signal(t, x, alpha):

    # Time reversal:
    # x(-t) is obtained by reversing the sampled signal
    x_reversed = x[::-1]

    # Amplitude scaling:
    # y(t) = alpha * x(-t)
    y = alpha * x_reversed

    return y


def main():

    # Generate time axis from -pi to pi
    t = np.linspace(-np.pi, np.pi, 1000)

    # Generate the original signal x(t)
    x = base_signal(t)

    while True:

        # Take alpha repeatedly from the user
        user_input = input(
            "Enter the value of alpha "
            "(or 'q' to quit): "
        )

        # End the program if the user enters q
        if user_input.lower() == 'q':
            print("Program terminated.")
            break

        # Convert the input into a floating-point number
        try:
            alpha = float(user_input)

        except ValueError:
            print(
                "Invalid input! "
                "Enter a numerical value or 'q'."
            )
            continue

        # Calculate y(t) = alpha * x(-t)
        y = transform_signal(t, x, alpha)

        # Plot the original and transformed signals
        plt.figure(figsize=(8, 5))

        plt.plot(
            t,
            x,
            label='x(t)'
        )

        plt.plot(
            t,
            y,
            label=f'y(t) = {alpha}x(-t)'
        )

        plt.xlabel('t')
        plt.ylabel('Amplitude')

        plt.title(
            'Time Reversal and '
            'Amplitude Scaling of x(t)'
        )

        plt.legend()
        plt.grid(True)

        plt.show()


if __name__ == "__main__":
    main()