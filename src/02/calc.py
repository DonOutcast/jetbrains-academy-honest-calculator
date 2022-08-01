msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
result = 0


def enter():
    lexems = ['+', '-', '/', '*']
    global result
    print(msg_0)
    user_input = input().split()

    try:
        x = float(user_input[0])
        oper = str(user_input[1])
        y = float(user_input[2])
        if oper not in lexems:
            print(msg_2)
            enter()
        if oper == "+":
            result = x + y
            print(result)
        elif oper == "-":
            result = x - y
            print(result)
        elif oper == "*":
            result = x * y
            print(result)
        elif oper == "/":
            result = x / y
            print(result)
    except ValueError:
        print(msg_1)
        enter()
    except SyntaxError:
        print(msg_2)
        enter()
    except ZeroDivisionError:
        print(msg_3)
        enter()
    except IndexError:
        print("Man")
        enter()


enter()
