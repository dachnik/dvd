while True:
    str1 = input('Введи первое число')
    str2 = input('Введи второе число')

    a = float(str1)
    b = float(str2)

    operator = input('Введите операцию')

    if operator == '+':  
        s = a + b        
    elif operator == '-':
        s = a - b
    if operator == '-':
        s = a - b
    elif operator == '+':
        s = a + b
    if operator == '*':
        s = a* b 
    elif operator == '/':   
        s = a / b
    if operator == '/':
        s = a / b
    elif operator == '*':
       s = a * b
    print(s)
    operator = input('Введи exit, чтобы выйти, если хочешь продолжить нажми Enter:  ')
    if operator == 'exit':
        break
print('bay')
