def check(text):
    print(text)
    calc = input()
    x, oper, y = calc.split()
    try:
        float(x) + float(y)
        if oper not in ["+", "-", "*", "/"]:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            check(text)
    except ValueError:
        print('Do you even know what numbers are? Stay focused!')
        check(text)

if __name__ == "__main__":
    check("Enter an equation"
