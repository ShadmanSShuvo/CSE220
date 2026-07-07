import numpy as np

S = int(input())
M = int(input())

A = []
for _ in range(S):
    row = list(map(int, input().split()))
    A.append(row)
A = np.array(A, dtype=float)

target_sales = np.array(list(map(int, input().split())), dtype=float)
K = int(input())

# 1. Achievement percentage matrix
P = 100 * A / target_sales

print("Percentage Matrix")
for i in range(S):
    print(" ".join(f"{P[i, j]:.2f}" for j in range(M)))
print()

# 2. Salesperson summary
print("Salesperson Summary")
salesperson_avg = P.mean(axis=1)
for i in range(S):
    best_product = int(np.argmax(P[i]))
    print(f"Salesperson {i} : Average = {salesperson_avg[i]:.2f} Best Product = {best_product}")
print()

# 3. Product summary
print("Product Summary")
product_avg = P.mean(axis=0)
for j in range(M):
    top_salesperson = int(np.argmax(P[:, j]))
    print(f"Product {j} : Average = {product_avg[j]:.2f} Top Salesperson = {top_salesperson}")
print()

# 4. Top K salespersons by average achievement
print(f"Top {K} Salespersons")
top_k_ids = np.argsort(-salesperson_avg)[:K]
for sid in top_k_ids:
    print(sid)
print()

# 5. Grade counts
def grade(p):
    if p >= 90:
        return "Excellent"
    elif p >= 75:
        return "Good"
    elif p >= 60:
        return "Average"
    else:
        return "Poor"

grade_counts = {"Excellent": 0, "Good": 0, "Average": 0, "Poor": 0}
for i in range(S):
    for j in range(M):
        grade_counts[grade(P[i, j])] += 1

print("Grade Count")
for g in ["Excellent", "Good", "Average", "Poor"]:
    print(f"{g} : {grade_counts[g]}")
