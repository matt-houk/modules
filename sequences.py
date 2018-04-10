def partial_sum(n, i, expression):
    '''return the partial sum of the expression to the nth iteration, with n starting at i'''
    if n == i:
        return eval(expression)
    return eval(expression) + partial_sum(n - 1, i, expression)

def fibonacci(n):
    '''return the nth fibonacci number'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence(n):
    '''return a list of the fibonacci sequence up to the nth element'''
    sequence = []
    for i in range(0, n+1):
        sequence.append(fibonacci(i))
    return sequence