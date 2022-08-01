
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"


memory = 0.0
lexems = ['+', '-', '/', '*']


def ask_user(var) -> None:
    global memory
    print(msg_4)
    user_answer = input()
    print(msg_5)
    if user_answer == "y":
        memory = var
        user_answer_2 = input()
        if user_answer_2 == "y":
            with_memmory()
    elif user_answer == 'n':
        user_answer_2 = input()
        if user_answer_2 == 'y':
            enter()


def with_memmory() -> None:
    result = 0.0
    print(msg_0)
    user_input = input().split()
    try:
        x = float(user_input[0])
        oper = str(user_input[1])
        if oper not in lexems:
            print(msg_2)
            with_memmory()
        if oper == "+":
            result = x + memory
            print(result)
            ask_user(result)
        elif oper == "-":
            result = x - memory
            print(result)
            ask_user(result)
        elif oper == "*":
            result = x * memory
            print(result)
            ask_user(result)
        elif oper == "/":
            result = x / memory
            print(result)
            ask_user(result)
    except ValueError:
        print(msg_1)
        with_memmory()
    except SyntaxError:
        print(msg_2)
        with_memmory()
    except ZeroDivisionError:
        print(msg_3)
        with_memmory()
    except IndexError:
        print("Man")
        with_memmory()


def enter():
    result = 0.0
    print(msg_0)
    user_input = input().split()
    y = user_input[2]
    if y == "M":
        y = memory
    else:
        try:
            y = float(user_input[2])
        except ValueError:
            print(msg_1)
            enter()
        except SyntaxError:
            print(msg_2)
            enter()
    try:
        x = float(user_input[0])
        oper = str(user_input[1])
        if oper not in lexems:
            print(msg_2)
            enter()
        if oper == "+":
            result = x + y
            print(result)
            ask_user(result)
        elif oper == "-":
            result = x - y
            print(result)
            ask_user(result)
        elif oper == "*":
            result = x * y
            print(result)
            ask_user(result)
        elif oper == "/":
            result = x / y
            print(result)
            ask_user(result)
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


if __name__ == "__main__":
    enter()

