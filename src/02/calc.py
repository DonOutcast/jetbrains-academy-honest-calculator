def check(text):
    global memory
    print(text)
    calc = input()
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        float(x), float(y)
        if oper not in ["+", "-", "*", "/"]:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            check(text)
        else:
            if oper == "+":
                store_and_continue((float(x) + float(y)))
            if oper == "-":
                store_and_continue((float(x) - float(y)))
            if oper == "*":
                store_and_continue((float(x) * float(y)))
            if oper == "/":
                if float(y) == 0:
                    print("Yeah... division by zero. Smart move...")
                    check(text)
    except ValueError:
        print('Do you even know what numbers are? Stay focused!')

memory = 0
if __name__ == "__main__":
    check("Enter an equation")
