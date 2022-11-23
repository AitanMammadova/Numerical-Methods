from sympy import *
from scipy.integrate import quad

def function(x):
    # function = pow(x,3)+3*pow(x,2)-1
    function = pow(x,3)-x+1
    return function

def check(a, b, function):
    t = function(a)*function(b)
    return t<0

def define_plus_minus(a, b, function):
    global plus
    global minus
    if check(a, b, function) == True:
        if function(a) > 0:
            plus = a
            minus = b
        else:
            plus = b
            minus = a       
            
def bisection(plus, minus, function):
    average = (plus + minus) / 2
    fx = function(average)
    if fx > 0:
        plus = average
    else:
        minus = average
    return [plus,minus]

def result_bisection(a, b, iter, function):
    x0 = [plus, minus]
    print(f'x0 = {sorted(x0)}')
    define_plus_minus(a, b, function)
    for i in range(1, iter +1):
        xi = x0
        x0 = bisection(xi[0], xi[1], function)
        print(f'x{i} = {sorted(x0)}')
        
print('Intervali daxil edin')
a = float(input('a = ')) 
b = float(input('b = '))

x = symbols('x')
func = function(x)
f_1 = func.diff(x)
f_2 = func.diff(x,2)
func = lambdify(x, func)
f_1 = lambdify(x, f_1)
f_2 = lambdify(x, f_2)

iter = int(input('Iterasiyalarin sayini daxil edin : '))

define_plus_minus(a, b, function)
result_bisection(a, b, iter, function)