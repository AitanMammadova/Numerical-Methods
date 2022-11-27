import math
from scipy.integrate import quad

def function(x):
    # function = 2*pow(x,4) + 3 * x
    # function = pow(x,3)+7
    # function = 1/(math.sqrt(2 * x + 3))
    # function = 2*pow(x, 4)-2
    # function = 3 * pow(x, 3) + 1
    # function = 2 * pow(x, 3) + 1
    # function = 2 * pow(x, 3) + 5 
    # function = 2 * pow(x, 3) + 3 * x 
    # function = 2 * pow(x, 4) + 3 * x 
    # function = 2 * pow(x, 4) - 2
    # function = 2 * pow(x, 4) - 3 * x + 2
    function = pow(x, 4) - 3 * x + 2
    # function = pow(x, 3) - 3 * x + 1
    # function = pow(x, 4) + x + 3
    # function = 1/(x+1)
    return function

def get_xi(a, h, n):
    xi = []
    for i in range(n + 1):
        xi.append(a + (i * h))
        print(f'x{i} = {a + (i * h)}')
    return xi

def rectangle(h, xi, n, function):
    result = 0
    for i in range(1,n + 1):
        result += (function(xi[i - 1] + (0.5 * h)))
    return h*result

def trapezoid(h, xi, n, function):
    result = 0
    for i in range(1,n+1):
        result += ((function(xi[i]) + function(xi[i - 1])) / 2) * h
    return result

def simp_xi_5(a, h, n):
    xi_ = []
    for i in range(0, n):
        xi_.append(a+(i+0.5)*h)
        print(f'x{i+0.5} = {a + ((i + 0.5) * h)}')
    return xi_

def simpson(h, xi, n, xi_, function):
    result = 0
    result += function(xi[0])+function(xi[n])
    for i in range(1,n):
        result+= 2*function(xi[i])
    for i in xi_:
        result += 4*function(i)
    return (h/6)*result

def r(method,I):
    return abs(method - I)

def rectangle_result(h, xi, n, I, function):
    print('\nDuzbucaqlilar usulu =',rectangle(h, xi, n, function))
    print('Integral = ',I)
    print('Xeta =',r(rectangle(h, xi, n, function),I))
    
def trapezoid_result(h, xi, n, I, function):
    print('\nTrapes usulu=',trapezoid(h, xi, n, function))
    print('Integral = ',I)
    print('Xeta =',r(trapezoid(h, xi, n, function),I))
    
def simpson_result(h, xi, n, I, xi_, function):
    print('Simpson usulu =',simpson(h, xi, n, xi_, function))
    print('Integral = ',I)
    print('Xeta =',r(simpson(h, xi, n, xi_, function), I))
    
    
n = int(input('n-i daxil edin : '))
print('\nIntegral ucun a ve b serhedlerini daxil edin:')
a = int(input('a = '))
b = int(input('b = '))
I, err = quad(function, a, b)
h = (b - a)/n
print(f'\nh = {h}\n')
xi = get_xi(a, h, n)
method = int(input("\nDuzbucaqlilar usulu ucun: 1, \nTrapesler usulu ucun: 2, \nSimpson usulu ucun: 3, \nDuzbucaqlilar, Trapesler ve Simpson usulu ucun: 4\n"))
match(method):
    case 1:
        rectangle_result(h, xi, n, I, function)
    case 2:
        trapezoid_result(h, xi, n, I, function)
    case 3:
        xi_ = simp_xi_5(a,h, n)
        simpson_result(h, xi, n, I, xi_, function)
    case 4:
        rectangle_result(h, xi, n, I, function)
        trapezoid_result(h, xi, n, I, function)
        print('\nSimpson usulu ')
        xi_ = simp_xi_5(a,h, n)
        simpson_result(h, xi, n, I, xi_, function)