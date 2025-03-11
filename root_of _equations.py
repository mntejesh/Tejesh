a = int(input("Give a:"))

b = int(input("Give b:"))

c = int(input("Give c:"))

d = b**2-4*a*c
r1 = d**0.5
r2 = (-b + r1)/2*a
r3 = (-b - r1)/2*a
print(f"Roots:({r2},{r3})")
