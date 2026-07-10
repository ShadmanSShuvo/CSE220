import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# The signal: given only as an index axis n and values x.
# Anything outside the stored n is treated as 0.
# ============================================================
n = np.array([-3, -2, -1, 0, 1, 2, 3])
x = np.array([10, 20, 30, 40, 50, 60, 70], dtype=float)


# ============================================================
# The pull-based transform: y[n] = x[alpha*n + beta]
#   - keep the output axis fixed (n_out)
#   - for each output index, compute the argument alpha*n + beta
#   - pull x at that argument; 0 if out of range or non-integer
# ============================================================
def transform(n_samp, x_samp, alpha, beta, n_out):
    n_out = np.asarray(n_out)
    arg = alpha * n_out + beta            # index each output pulls FROM
    out = np.zeros(n_out.shape, dtype=float)

    is_int = (arg == np.round(arg))       # discrete: only integer args are real samples
    ai = np.round(arg).astype(int)

    # look each integer argument up in n_samp
    pos = np.searchsorted(n_samp, ai)
    pos = np.clip(pos, 0, len(n_samp) - 1)     # keep index legal for the check
    valid = is_int & (n_samp[pos] == ai)       # real hit AND integer

    out[valid] = x_samp[pos[valid]]            # copy hits; the rest stay 0
    return out


# ============================================================
# Examples — the output axis is ALWAYS the same n
# ============================================================
n_out = n   # keep the axis fixed

y_scale   = transform(n, x, alpha=2,  beta=0,  n_out=n_out)   # x[2n]  (compress)
y_reverse = transform(n, x, alpha=-1, beta=0,  n_out=n_out)   # x[-n]  (reverse)
y_delay   = transform(n, x, alpha=1,  beta=-2, n_out=n_out)   # x[n-2] (delay right 2)
y_combo   = transform(n, x, alpha=-2, beta=1,  n_out=n_out)   # x[-2n+1]

print("n         :", n)
print("x[n]      :", x)
print("x[2n]     :", y_scale)
print("x[-n]     :", y_reverse)
print("x[n-2]    :", y_delay)
print("x[-2n+1]  :", y_combo)


# ============================================================
# Plot original vs x[2n]
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
ax1.stem(n, x);        ax1.set_title("x[n]");    ax1.grid(True)
ax2.stem(n, y_scale);  ax2.set_title("y[n]=x[2n]"); ax2.grid(True)
for ax in (ax1, ax2):
    ax.set_xlabel("n"); ax.set_ylabel("amplitude"); ax.set_xticks(n)
fig.tight_layout()
plt.savefig("transform.png")
plt.show()