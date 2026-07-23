def celsius_to_fahrenheit(c):
    return (9/5) * c + 32


def fahrenheit_to_celsius(f):
    return (5/9) * (f - 32)


choice = input("1.C→F  2.F→C : ")

if choice == "1":
    c = float(input("Celsius: "))
    print(celsius_to_fahrenheit(c))

elif choice == "2":
    f = float(input("Fahrenheit: "))
    print(fahrenheit_to_celsius(f))

else:
    print("Invalid Choice")