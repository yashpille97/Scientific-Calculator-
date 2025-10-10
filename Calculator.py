try:
    a=(input('enter the your operation: \n1=single number operation: \n2=two number operation: \n'))
    if a=='1':
        import math
        o=int(input('enter the operation(sine(3),cos(4),log value (5),square root (6)'))
        if o==3:
            float(input('Enter number:'))
            sine_value = math.sin(o)
            print(sine_value)
        elif o==4:
            float(input('Enter number:'))
            cosine_value = math.cos(o)
            print(cosine_value)
        elif o==5:
            float(input('Enter number:'))
            log_value = math.log(o)
            print(log_value)
        elif o==6:
            float(input('Enter number:'))
            square_root = math.sqrt(o)
            print(square_root)
        else:
            print('none')

    else :
        operand_1 = float(input('enter the first number: '))

        operand_2 = float(input('enter the second number: '))
        operator = (input('enter the operator (+,-,*,/,):'))
        if operator == '+':
            print(operand_1 + operand_2)
        elif operator == '-':
            print(operand_1 - operand_2)
        elif operator == '*':
            print(operand_1 * operand_2)
        elif operator == '/':
            if operand_2 == 0:
                print('can not divide by zero')
            else:
                print(operand_1 / operand_2)

        else:
            print('none')



except ValueError:
    print('Invalid input')

