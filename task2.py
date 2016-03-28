str1 = input('Введи первое число')
str2 = input('Введи второе число')

a = float(str1)
b = float(str2)

operator = input('Введите операцию')
if operator == '+': 
    s = a + b       
    print(s)
operator = input('Введите операцию')
if operator == '-':
    s = a - b
    print(s)
operator = input('Введите операцию')
if operator == '*':
    s = a* b 
    print(s)
operator = input('Введите операцию')
if operator == '/':
    s = a / b
    print(s)
print('Bye')
