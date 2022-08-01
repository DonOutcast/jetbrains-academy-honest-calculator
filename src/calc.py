msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

def enter():
    lexems = ['+', '-', '/', '*']
    result = 0
    print(msg_0)
    user_input = input().split()
    try:
        x = int(user_input[0])
        oper = str(user_input[1])
        y = float(user_input[2])
        if oper not in lexems:
            print(msg_2)
            enter()
    except ValueError:
        print(msg_1)
        enter()
    except SyntaxError:
        print(msg_2)
        enter()
    except IndexError:
        print("Man")
        enter()


enter()

