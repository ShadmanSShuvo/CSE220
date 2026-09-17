a = float(input())
b = float(input())
c = float(input())

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest =", largest)