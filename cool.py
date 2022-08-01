memory = 0
math_ops = '+-*/'
msg_0 = 'Enter an equation\n'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = 'Yeah... division by zero. Smart move...'
msg_4 = "Do you want to store the result? (y / n):\n" 
msg_5 = "Do you want to continue calculations? (y / n):\n"

def calc():

    x, oper, y = input(msg_0).split()

    if x == 'M':
        x = memory

    elif y == 'M':
        y = memory

    try:
        x = float(x)
        y = float(y)
    
    except (TypeError, ValueError):
        print(msg_1)

    else:
        if oper == '+':
            result = x + y
            return result

        elif oper == '-':
            result = x - y
            return result

        elif oper == '*':
            result = x * y
            return result

        elif oper == '/' and y != 0:
            result = x / y
            return result
        
        else:
            print(msg_3)


while True:
    calculation = calc()
    if type(calculation) == float or type(calculation) == int:
        print(calculation)

        store = input(msg_4)
        continum = input(msg_5)

        if store == 'y':
            memory = calculation
        if continum == 'n':
            break
        else:
            continue
        
    else:
        continue
    
