class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    def __add__(self, other):
        return self.a + other.a
    def __sub__(self, other):
        return self.a - other.a
    def __mul__(self, other):
        return self.a * other.a
    def __truediv__(self, other):
        return self.a / other.a
if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    calculator = Calculator(a, b)

    print("Addition: ", calculator.add())
    print("Subtraction: ", calculator.subtract())
    print("Multiplication: ", calculator.multiply())
    print("Division: ", calculator.divide())
