a = 5
b = 10

print("Before swap (with temp): a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swap (with temp): a =", a, "b =", b)

print("Before swap (without temp): a =", a, "b =", b)

a = a + b
b = a - b
a = a - b

print("After swap (without temp): a =", a, "b =", b)
