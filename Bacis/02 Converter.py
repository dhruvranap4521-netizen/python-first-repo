a = int(input("Enter Hours :" ))
print(f"{a}hours = {a*60}min.")

b = int(input("Enter Min:" ))
print(f"{b}min. = {b/60}hours")

c = int(input("Enter Dollars (1 $ = 48 Rs.) :" ))
print(f"{c}$ = {c*48}Rs.")

d = int(input("Enter Ruppes (1$ = 48Rs.) :" ))
print(f"{d}Rs. = {d/48}$")

d = int(input("Enter dollars (1$ = 48Rs. & 1 pound = 70Rs.) :" ))
pound = (d * 48) / 70
print(f"{d}$ = {pound} pound")

a = int(input("Enter grams :" ))
print(f"{a}gm = {a/1000}kg")

b = int(input("Enter kg :" ))
print(f"{b}kg = {b*1000}gm")

c = int(input("Enter bytes :" ))
print(f"{c}bytes = {c/1000}KB")
print(f"{c}bytes = {c/1000000}MB")
print(f"{c}bytes = {c/1000000000}GB")

d = int(input("Enter celcius :" ))
print(f"{d}C = {(9/5*d)+32}F")

e = int(input("Enter Fahrenheit :" ))
print(f"{e}F = {(e-32)*5/9}C")

