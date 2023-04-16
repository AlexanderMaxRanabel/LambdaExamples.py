x = int(input("Enter a number that can be used as an argument: "))
y = int(input("Enter a number that can be used as an argument: "))

expr = lambda x, y: 'Even' if (x * y) % 2 == 0 else 'Odd'
expr_result = expr(x, y)
print(expr_result)
