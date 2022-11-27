from sympy import lambdify, symbols

def function(x):
    function = pow(x,3)+3*pow(x,2)-1
    # function = pow(x,3) - 5 * x + 1
    # function = pow(x,3)-x+1
    return function

def check(a, b, function):
    t = function(a) * function(b)
    return t < 0

def define_plus_minus(a, b, function):
    global plus
    global minus
    if check(a, b, function) == True:
        if function(a)>0:
            plus = a
            minus = b
        else:
            plus = b
            minus = a
    return [plus, minus]

def define_x0(f_2, function, p_m):
    global x1
    global x0
    if f_2(p_m[0])*function(p_m[0]) > 0:
        x0 = p_m[0]
        x1 = p_m[1]
        
    elif f_2(p_m[1]) * function(p_m[1]) > 0:
        x0 = p_m[1]
        x1 = p_m[0]
        
    elif f_2(p_m[0]) * function(p_m[0]) == 0:
        if p_m[0]>p_m[1]:
            x0 = p_m[0]-0.1
            x1 = p_m[1]
        else:
            x0 = p_m[0] + 0.1
            x1 = p_m[1]
            
    elif f_2(p_m[1]) * function(p_m[1]) == 0:
        if p_m[0] > p_m[1]:
            x0 = p_m[1] + 0.1
            x1 = p_m[0]
        else:
            x0 = p_m[1] - 0.1
            x1 = p_m[0]
    return x0

def raphson_method(x0, f_1, function):
    x1 = x0 - (function(x0)/  f_1(x0))
    return x1

def chord_method(x0,x1, function):
    x2 = (((x0 * function(x1)) + (x1 * function(x0)))  /  (function(x1) - function(x0)))
    return x2

def result_raphson(f_1, f_2, function, p_m, iter):
    x0 = define_x0(f_2, function, p_m)
    print(f'x0 = {x0}')
    for i in range(1, iter + 1):
        xi = x0
        x0 = raphson_method(xi, f_1, function)
        print(f'x{i} = {x0}')
        
def result_chord(f_2, function, p_m, iter):
    x0 = define_x0(f_2, function, p_m)
    x_1 = x1
    print(f'x0 = {x0}')
    print(f'x1 = {x_1}')
    for i in range(2,iter + 1):
        xi = x_1
        x_1 = chord_method(x0, xi, function)
        print(f'x{i} = {x_1}')

print('Intervali daxil edin')
a = float(input('a = ')) 
b = float(input('b = '))

x = symbols('x')
func = function(x)
f_1 = func.diff(x)  # type: ignore
f_2 = func.diff(x,2)  # type: ignore
func = lambdify(x, func)
f_1 = lambdify(x, f_1)
f_2 = lambdify(x, f_2)

iter = int(input('Iterasiyalarin sayini daxil edin : '))
print('\nToxunanlar usulu ucun:1 \nVeterler usulu ucun: 2 \nToxunanlar ve Veterler usulu ucun: 3\n')
method = int(input())

match(method):
    case 1:
        p_m = define_plus_minus(a,b,function)
        result_raphson(f_1, f_2, function,p_m,iter)
    case 2:
        p_m = define_plus_minus(a,b,function)
        result_chord(f_2, function,p_m,iter)
    case 3:
        print("Toxunanlar usulu")
        p_m = define_plus_minus(a,b,function)
        result_raphson(f_1, f_2, function,p_m,iter)
        print("Veterler usulu")
        p_m = define_plus_minus(a,b,function)
        result_chord(f_2, function,p_m,iter)
    case(other):
        print("Bele bir emeliyyat movcud deyildir!")