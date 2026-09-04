n = int(input())
visits = []
data = {}

for _ in range(n):
    parts = input().split()
    name, severity, treatment_time = parts[0], int(parts[1]), int(parts[2])
    visits.append((name, severity, treatment_time))

    if name not in data:
        data[name] = {"total_treatment_time": 0, "total_severity_score": 0}
    data[name]["total_treatment_time"] += treatment_time
    data[name]["total_severity_score"] += severity

for name in sorted(data.keys()):
    print(name, data[name]["total_treatment_time"], data[name]["total_severity_score"])

top_name = None
top_score = -1
for name in sorted(data.keys()):
    score = data[name]["total_severity_score"]
    if score > top_score:
        top_score = score
        top_name = name

print("TOP", top_name, top_score)
