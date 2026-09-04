import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
north = np.array([120, 135, 128, 142, 150, 158, 162, 170, 168, 180, 185, 195]) 
south = np.array([110, 118, 125, 130, 138, 145,  150, 155, 160, 168, 172, 180]) 
central = np.array([100, 108, 115, 120, 130, 140, 148, 152, 158, 165, 170, 175]) 

branch = ["North", "South", "Central"]
dec_profit = [north[-1], south[-1], central[-1]]
plt.figure(figsize=(14, 10))

plt.subplot(2,2,1)
plt.plot(months, north, color="blue", label="north")
plt.plot(months, south, color="green", linestyle="--", label="south")
plt.plot(months, central, color="red", linestyle=":", label="central")
plt.title("Monthly Branch Profit (2025)")
plt.xlabel("Month")
plt.ylabel("Profit (in thousand dollars)")
plt.legend()
plt.grid(True)


plt.subplot(2,2,2)
plt.bar(branch, dec_profit, color=["blue", "green", "red"])
plt.grid(True)


plt.subplot(2,2,3)
plt.scatter(months, north, color="blue")
plt.grid(True)


plt.subplot(2,2,4)
# Quarterly profit
north_q = [sum(north[0:3]), sum(north[3:6]), sum(north[6:9]), sum(north[9:12])]
south_q = [sum(south[0:3]), sum(south[3:6]), sum(south[6:9]), sum(south[9:12])]
central_q = [sum(central[0:3]), sum(central[3:6]), sum(central[6:9]), sum(central[9:12])]

quarters = ['Q1', 'Q2', 'Q3', 'Q4']

plt.bar(quarters, north_q, color='blue', label='North')
plt.bar(quarters, south_q, bottom=north_q, color='green', label='South')

bottom = np.array(north_q) + np.array(south_q)

plt.bar(quarters, central_q, bottom=bottom, color='red', label='Central')
plt.grid(True)

plt.show()