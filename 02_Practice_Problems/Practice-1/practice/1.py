n=int(input())

visits = []

for _ in range(n):
    name, severity, time = input().split()
    #name = input()
    severity = int(severity)
    time = int(time)
    visits.append((name, severity, time))


patients = {}

for name, severity, time in visits:
    if name not in patients:
        patients[name] = {
            "total_time": 0,
            "total_severity_score": 0
        }

    patients[name]["total_time"] += time
    patients[name]["total_severity_score"] += severity


print("\nPatient Summary:")
for patient in sorted(patients):
    print(
        patient,
        patients[patient]["total_time"],
        patients[patient]["total_severity_score"]
    )



highest_patient = None
highest_score = -1

for patient in sorted(patients):
    score = patients[patient]["total_severity_score"]

    if score > highest_score:
        highest_score = score
        highest_patient = patient


print("\nPatient with highest total severity score:")
print(highest_patient, highest_score)