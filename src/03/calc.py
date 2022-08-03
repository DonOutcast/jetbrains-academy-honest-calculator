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
                else:
                    store_and_continue((float(x) / float(y)))
    except ValueError:
        print('Do you even know what numbers are? Stay focused!')
        check(text)


def store_and_continue(result):
    global memory
    print(result)
    print("Do you want to store the result? (y / n):")
    if input() == "y":
        memory = result
    print("Do you want to continue calculations? (y / n):")
    if input() == "y":
        check("Enter an equation")


memory = 0
if __name__ == "__main__":
    check("Enter an equation")
