import numpy as np
import matplotlib.pyplot as plt

def matrix_add():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A + B)

def matrix_multiply():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A @ B)

def plot_sine():
    t = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(t, np.sin(t))
    plt.grid(True)
    plt.show()

def plot_cosine():
    t = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(t, np.cos(t))
    plt.grid(True)
    plt.show()

def statistics():
    A = np.random.randint(1, 100, 20)
    print("Mean =", np.mean(A))
    print("Max =", np.max(A))
    print("Min =", np.min(A))

while True:
    print("\n1.Matrix Addition\n2.Matrix Multiplication\n3.Plot Sine\n4.Plot Cosine\n5.Statistics\n0.Exit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        continue
    if choice == 1: matrix_add()
    elif choice == 2: matrix_multiply()
    elif choice == 3: plot_sine()
    elif choice == 4: plot_cosine()
    elif choice == 5: statistics()
    elif choice == 0: break
