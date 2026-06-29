# Program to calculate Compound Interest .

P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Annual Interest Rate (%): "))
T = float(input("Enter the Time (in years): "))

# Compound Amount
A = P * (1 + R / 100) ** T

# Compound Interest
CI = A - P

print("Compound Amount =", round(A, 2))
print("Compound Interest =", round(CI, 2))