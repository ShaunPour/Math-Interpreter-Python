def main():
    expression = input("Enter your expression (please note that you must input a space after the first number and before the second or the program will return an error): ")
    x, y, z = expression.split(" ")

    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))

main()
