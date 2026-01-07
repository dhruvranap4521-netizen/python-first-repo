a = int(input("Enter your gross salary : "))
c = (a*10/100)
d = (a*3/100) 
b = a + c - d

print(f"Allowances is 10% of gross salary is :{c}")
print(f"Deduction is 3% of gross salary is {d}")
print(f"Net salary is {b}")