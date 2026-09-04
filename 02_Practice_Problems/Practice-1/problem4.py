import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
north = np.array([120, 135, 128, 142, 150, 158, 162, 170, 168, 180, 185, 195])
south = np.array([110, 118, 125, 130, 138, 145, 150, 155, 160, 168, 172, 180])
central = np.array([100, 108, 115, 120, 130, 140, 148, 152, 158, 165, 170, 175])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1 (Top Left): Monthly Profit Line Plot
ax1 = axes[0, 0]
ax1.plot(months, north, 'b-', label='North')
ax1.plot(months, south, 'g--', label='South')
ax1.plot(months, central, 'r:', label='Central')
ax1.set_title('Monthly Branch Profit (2025)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Profit (in thousand dollars)')
ax1.legend()
ax1.grid(True)

# Plot 2 (Top Right): December Profit Comparison
ax2 = axes[0, 1]
branches = ['North', 'South', 'Central']
dec_profits = [north[-1], south[-1], central[-1]]
colors = ['blue', 'green', 'red']
ax2.bar(branches, dec_profits, color=colors)
ax2.set_title('December Profit Comparison')
ax2.set_xlabel('Branch')
ax2.set_ylabel('Profit (in thousand dollars)')
ax2.grid(axis='y')

# Plot 3 (Bottom Left): North Branch Profit Distribution
ax3 = axes[1, 0]
ax3.scatter(months, north, c='blue', s=60)
ax3.set_title('North Branch Profit Distribution')
ax3.set_xlabel('Month')
ax3.set_ylabel('Profit (in thousand dollars)')
ax3.grid(True)

# Plot 4 (Bottom Right): Quarterly Branch Profit (stacked bar)
ax4 = axes[1, 1]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
north_q = [north[0:3].sum(), north[3:6].sum(), north[6:9].sum(), north[9:12].sum()]
south_q = [south[0:3].sum(), south[3:6].sum(), south[6:9].sum(), south[9:12].sum()]
central_q = [central[0:3].sum(), central[3:6].sum(), central[6:9].sum(), central[9:12].sum()]

north_q = np.array(north_q)
south_q = np.array(south_q)
central_q = np.array(central_q)

ax4.bar(quarters, north_q, color='blue', label='North')
ax4.bar(quarters, south_q, bottom=north_q, color='green', label='South')
ax4.bar(quarters, central_q, bottom=north_q + south_q, color='red', label='Central')
ax4.set_title('Quarterly Branch Profit')
ax4.set_xlabel('Quarter')
ax4.set_ylabel('Profit (in thousand dollars)')
ax4.legend()
ax4.grid(axis='y')

fig.suptitle('Company Branch Performance Analysis (2025)')
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/problem4_output.png', dpi=100)
print("Plot saved as problem4_output.png")
