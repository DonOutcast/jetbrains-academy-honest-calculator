
msg = ""
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"


memory = 0.0
lexems = ['+', '-', '/', '*']


def is_one_digit(var_1) -> bool:
    if var_1 == int(var_1) and -10 < var_1 < 10:
        return True
    return False


def ask_user(var) -> None:
    global memory
    global msg
    print(msg_4)
    user_answer = input()
    print(msg_5)
    if user_answer == "y":
        memory = var
        user_answer_2 = input()
        if user_answer_2 == "y":
            msg = ""
            with_memmory()
    elif user_answer == 'n':
        user_answer_2 = input()
        msg = ""
        if user_answer_2 == 'y':
            enter()


def with_memmory() -> None:
    global msg
    x = 0.0
    # result = 0.0
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
            if is_one_digit(x) and is_one_digit(memory):
                if msg == "":
                    msg += msg_9 + msg_6
                else:
                    msg += msg_6
            if x == 0 or memory == 0:
                msg += msg_8
            print(msg)
            print(result)
            ask_user(result)
        elif oper == "-":
            result = x - memory
            if is_one_digit(x) and is_one_digit(memory):
                if msg == "":
                    msg += msg_9 + msg_6
                else:
                    msg += msg_6
            if x == 0 or memory == 0:
                msg += msg_8
            print(msg)
            print(result)
            ask_user(result)
        elif oper == "*":
            result = x * memory
            if is_one_digit(x) and is_one_digit(memory):
                if msg == "":
                    msg += msg_9 + msg_6
                else:
                    pass
                    # msg_memmory += msg_6
            if x == 1 or memory == 1:
                msg += msg_7
            if x == 0 or memory == 0:
                msg += msg_8
            print(msg)
            print(result)
            ask_user(result)
        elif oper == "/":
            result = x / memory
            if is_one_digit(x) and is_one_digit(memory):
                if msg == "":
                    msg += msg_9 + msg_6
                else:
                    msg += msg_6
            if msg != "":
                msg = msg_9 + msg
            print(msg)
            print(result)
            ask_user(result)
    except ValueError:
        print(msg_1)
        with_memmory()
    except SyntaxError:
        print(msg_2)
        with_memmory()
    except ZeroDivisionError:
        if is_one_digit(x) and is_one_digit(memory):
            if msg == "":
                msg += msg_9 + msg_6
            else:
                msg += msg_6
            print(msg)
        print(msg_3)
        with_memmory()
    except IndexError:
        print("Man")
        with_memmory()


def enter():
    global msg
    # result = 0.0
    x = 0.0
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
            if is_one_digit(x) and is_one_digit(y):
                if msg == "":
                    msg += msg_9 + msg_6
                else:
                    msg += msg_6
            if x == 0 or y == 0:
                msg += msg_8
            print(msg)
            print(result)
            ask_user(result)
        elif oper == "-":
            result = x - y
            if is_one_digit(x) and is_one_digit(y):
                if msg == "":
                    msg += msg_9 + msg_6
                else:
                    msg += msg_6
            if x == 0 or y == 0:
                msg += msg_8
            print(msg)
            print(result)
            ask_user(result)
        elif oper == "*":
            result = x * y
            if is_one_digit(x) and is_one_digit(y):
                if msg == "":
                    msg += msg_9 + msg_6
            if x == 1 or y == 1 and msg != "":
                msg += msg_7
            elif x == 1 or y == 1 and msg == "":
                msg += msg_9 + msg_7
            if x == 0 or y == 0 and msg != "":
                msg += msg_8
            elif x == 0 or y == 0 and msg == "":
                msg += msg_9 + msg_8
            if x <= 1 or y <= 1:
                print(msg)
            print(result)
            ask_user(result)
        elif oper == "/":
            result = x / y
            if is_one_digit(x) and is_one_digit(y):
                if msg == "":
                    msg += msg_9 + msg_6
                else:
                    msg += msg_6
            if msg != "":
                msg = msg_9 + msg
            print(msg)
            print(result)
            ask_user(result)
    except ValueError:
        print(msg_1)
        enter()
    except SyntaxError:
        print(msg_2)
        enter()
    except ZeroDivisionError:
        if is_one_digit(x) and is_one_digit(y):
            if msg == "":
                msg += msg_9 + msg_6
            else:
                msg += msg_6
            print(msg)
        print(msg_3)
        enter()
    except IndexError:
        print("Man")
        enter()


if __name__ == "__main__":
    enter()

