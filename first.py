x = int(input("Enter a number that can be used as an argument: "))
y = int(input("Enter a number that can be used as an argument: "))
r = int(input("Enter a number that can be used as an argument and a target for division: "))

expression = lambda x, y, z, r: 0 if (x*z) + (y*(z*2)) - x + 1 % r == r * x else 1
expression_res = expression(x, y, r*5, r)
print(expression_res)


