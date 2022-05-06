import operator

DIGITS = set('0123456789')
OPERATIONS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
    '^' : operator.pow,
}


def is_digit(var):
    return var in DIGITS

def get_number(varstr):
    s = ""
    if varstr[0] == '-':
        s += "-"
        varstr = varstr[1:]
    for c in varstr:
        if not is_digit(c): # checks for numbers in string
            break
        s += c
    return (int(s), len(s))

def perform_operation(string, num1, num2):
    op = OPERATIONS.get(string, None)
    if op is not None:
        return op(num1, num2)
    else:
        return None  # How to handle this?

def eval_math_expr(expr):
    while True:
        try: 
            number1, end_number1 = get_number(expr)
            expr = expr[end_number1:]
            if expr == '': 
                return number1
            op = expr[0]
            expr = expr[1:]
            number2, end_number2 = get_number(expr)
            number1 = perform_operation(op, number1, number2)
            expr = str(number1) + expr[end_number2:]
        except Exception as e: # error catchin
            print(e)
            break
    return number1


if __name__ == '__main__': # easy debugging
    interactive = True
    if interactive:
        expr = input('Enter your expression:')
        print(expr + '=')
        print(eval_math_expr(expr))
    else:
        for expr, res in {"2": 2, "2*4": 8, "4+8": 12, "100/3": 33, "2^3": 8, "-2": -2, "-2-3": -5}.items():
            result = eval_math_expr(expr)
            if res != result:
                print("Computing", expr, "got", result, "instead of", res)