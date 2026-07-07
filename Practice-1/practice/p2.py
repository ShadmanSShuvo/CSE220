# Input
S = int(input())
M = int(input())

# Sales matrix
A = []
for i in range(S):
    row = list(map(int, input().split()))
    A.append(row)

# Target sales
target_sales = list(map(int, input().split()))

K = int(input())

# Percentage matrix
P = []
for i in range(S):
    row = []
    for j in range(M):
        row.append(100 * A[i][j] / target_sales[j])
    P.append(row)

print("Percentage Matrix")
for row in P:
    for x in row:
        print(f"{x:.2f}", end=" ")
    print()

# Salesperson Summary
print("\nSalesperson Summary")

sales_avg = []

for i in range(S):
    total = 0
    best_product = 0

    for j in range(M):
        total += P[i][j]
        if P[i][j] > P[i][best_product]:
            best_product = j

    avg = total / M
    sales_avg.append((avg, i))

    print(f"Salesperson {i} : Average = {avg:.2f} Best Product = {best_product}")

# Product Summary
print("\nProduct Summary")

for j in range(M):
    total = 0
    top_salesperson = 0

    for i in range(S):
        total += P[i][j]
        if P[i][j] > P[top_salesperson][j]:
            top_salesperson = i

    avg = total / S
    print(f"Product {j} : Average = {avg:.2f} Top Salesperson = {top_salesperson}")

# Top K Salespersons
sales_avg.sort(key=lambda x: (-x[0], x[1]))

print(f"\nTop {K} Salespersons")
for i in range(K):
    print(sales_avg[i][1])

# Grade Count
excellent = 0
good = 0
average = 0
poor = 0

for i in range(S):
    for j in range(M):
        p = P[i][j]

        if p >= 90:
            excellent += 1
        elif p >= 75:
            good += 1
        elif p >= 60:
            average += 1
        else:
            poor += 1

print("\nGrade Count")
print("Excellent :", excellent)
print("Good :", good)
print("Average :", average)
print("Poor :", poor)