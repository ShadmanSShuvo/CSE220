import numpy as np
import matplotlib.pyplot as plt


def base_signal(t):
    x = np.exp(-t) * np.cos(t)
    x[(t < -np.pi) | (t > np.pi)] = 0
    return x


def transform_signal(t, x, alpha):
    
    # TODO: implement tranformation
    x_rev = x[::-1]     # x_rev(t) = x(-t)
    y = alpha * x_rev   # y(t) = alpha * x_rev(t) = alpha * x(-t)
    return y


def main():
    t = np.linspace(-np.pi, np.pi, 1000)
    x = base_signal(t)
    

    while True:
        alpha = input()
        if alpha == 'q':
            break
        
        alpha = float(alpha)
        # TODO: complete the loop
        y = transform_signal(t, x, alpha)

        plt.figure(figsize=(8, 5))
        plt.plot(t, x, label='x(t)')
        plt.plot(t, y, label=f'y(t) = {alpha} * x(-t)')
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.title('Time Reversal and Amplitude Scaling of x(t)')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    main()