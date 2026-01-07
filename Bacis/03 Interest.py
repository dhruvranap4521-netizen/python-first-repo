p = int(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
n = float(input("Enter Time (in years): "))

i = (p * r * n) / 100
print(f"Simple Interest = {i}")
print(f"Total Amount = {p + i}")
