"""P03 - Building piecewise signals with masks. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

T_MIN, T_MAX, N = -3.0, 3.0, 1201


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def rect_pulse(t, width):
    """1 where |t| <= width/2, else 0."""
    x = np.zeros_like(t)
    m1 = np.abs(t)<=width/2
    x[m1] = 1
    return x


def triangle_pulse(t, width):
    """A triangle peaking at 1 for t=0, reaching 0 at |t| = width/2."""
    x = np.zeros_like(t)
    m1 = (t>=0) & (t<=width/2)
    m2 = (t<=0) & (t>=-width/2)
    x[m1] = 1-2*t[m1]/width 
    x[m2] = 1+ 2*t[m2]/width
    return x


def unit_step(t):
    """The Heaviside step: 1 for t >= 0, else 0."""
    m1 = t>=0
    x = np.zeros_like(t)
    x[m1] = 1
    return x


def main():
    t = np.linspace(T_MIN, T_MAX, N)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t, rect_pulse(t, 2.0), label="rect (width 2)")
    ax.plot(t, triangle_pulse(t, 2.0), label="triangle (width 2)")
    ax.plot(t, unit_step(t), label="unit step")
    ax.set_title("Piecewise signals from masks")
    ax.set_xlabel("t"); ax.set_ylabel("Amplitude")
    ax.set_ylim(-0.2, 1.3); ax.grid(True, alpha=0.3); ax.legend()
    plt.show()
    assert rect_pulse(np.array([0.0, 0.9, 1.1]), 2.0).tolist() == [1.0, 1.0, 0.0]
    assert np.isclose(triangle_pulse(np.array([0.0]), 2.0)[0], 1.0)
    assert np.isclose(triangle_pulse(np.array([0.5]), 2.0)[0], 0.5)
    assert unit_step(np.array([-1.0, 0.0, 1.0])).tolist() == [0.0, 1.0, 1.0]
    print("[P03] rect, triangle, and step take the expected values  -> passed.")


if __name__ == "__main__":
    main()
