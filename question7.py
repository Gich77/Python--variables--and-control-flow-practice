def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides. Lengths must be positive numbers."

    if (a + b > c) and (b + c > a) and (a + c > b):
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or b == c or a == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "The given sides do not form a valid triangle."

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

result = classify_triangle(a, b, c)
print(result)