import math 

def function(x):
    function = (2*x+1)/(pow(x,2)+3)
    return function

def set_x(num_of_x):
    print('\nX-leri daxil edin')
    x_n = []
    for i in range(num_of_x):
        print(f'x{i}: ',end='')
        x = float(input())
        x_n.append(x)
    print('')
    return x_n

def get_fx(x_n, function):
    f_x = []
    for i in range(len(x_n)):
        f_x.append(function(x_n[i]))
    return f_x

def print_xi(xi):
    for i in range(len(xi)):
        print(f'x{i} = {xi[i]}')
    print('')
    
def print_fx(f_x):
    for i in range(len(f_x)):
        print(f'y{i}: {f_x[i]}')
    print('')

def lagrange_polynomial(x, x_i, f_x):
    numerator = 1 
    denumerator = 1
    result = 0
    for i in range(len(x_i)):
        numerator = 1
        denumerator = 1
        for j in range(len(x_i)):
            if j == i:
                continue
            else:
                numerator *= (x - x_i[j])
                denumerator *= (x_i[i] - x_i[j])
        result += ((numerator / denumerator) * f_x[i])
    return result

def newton_polynomial(x, x_i, f_x):
    result = f_x[0]
    xf = 0 
    xs = 1
    fxs = 0
    denumerator = 1
    # numerator,fxi
    for i in range(1, len(x_i)):
        fxs = 0
        xf = 0
        xs = 1
        denumerator = 1

        for j in range(i):
            xs *=(x-x_i[j])
        for k in range(i+1):
            denumerator = 1
            numerator = f_x[k]
            for z in range(i+1):
                if z ==k:
                    continue
                else:
                    denumerator *= (x_i[k]-x_i[z])
            fxi = numerator/denumerator
            fxs +=fxi
        xf += (xs*fxs)
        result += xf
    return result

def opt_xi(n):
    xi = []
    for i in range(n):
        xi.append(math.cos(((2*i+1) * (math.pi)) / (2*(n))))
    return xi

def r(method, f):
    return method - f

def lagrange(x, x_i, f_x):
    lagrange_pol = lagrange_polynomial(x, x_i, f_x)
    return lagrange_pol

def newton(x, x_i, f_x):
    newton_pol = newton_polynomial(x, x_i, f_x)  
    return newton_pol

def opt(op_xi, op_fx, x):
    lag_op= lagrange_polynomial(x, op_xi, op_fx)
    new_op = newton_polynomial(x, op_xi, op_fx)
    return [lag_op, new_op]

def print_op_xi_fx(op_xi, op_fx):
    print_xi(op_xi)
    print_fx(op_fx)
    
def fx(x, function):
    func = function(x)
    return func

def result_lagrange(x, x_i, f_x, function):
    print(f'\nLaqranj interpolyasiyasi : {lagrange(x,x_i, f_x)}')
    print(f'Netice(Laqranj) : {abs(fx(x,function) - lagrange(x, x_i, f_x))}')

def result_newton(x, x_i, f_x, function):
    print(f'\nNyuton interpolyasiyasi : {newton(x, x_i, f_x)}')
    print(f'Netice(Nyuton) : {abs(fx(x, function) - newton(x, x_i, f_x))}')

def result_opt_lag(opt, op_xi, op_fx, x, function):
    print(f'\nLaqranj interpolyasiyasi ile Optimal Secme : {opt(op_xi, op_fx, x)[0]}')
    print(f'Netice(Laqranj) : {abs(fx(x, function) - opt(op_xi, op_fx, x)[0])}\n')
    
def result_opt_new(opt, op_xi, op_fx, x, function):
    print(f'\nNyuton interpolyasiyasi ile Optimal Secme : {opt(op_xi, op_fx, x)[1]}')
    print(f'Netice(Nyuton) : {abs(fx(x, function) - opt(op_xi, op_fx, x)[1])}\n')
    

num_of_x = int(input('X-lerin sayini teyin edin: '))
x_i = set_x(num_of_x)
f_x = get_fx(x_i, function)
print_fx(f_x)
x = float(input('\nx-i daxil edin : '))
print(f'\nf(x) = {fx(x, function)}')
op_xi = opt_xi(num_of_x)
op_fx = get_fx(op_xi, function)

def lagrange_res():
    result_lagrange(x, x_i, f_x, function)

def newton_res():
    result_newton(x, x_i, f_x, function)
    
def optimal_selection(method):
    print_op_xi_fx(op_xi, op_fx)
    print(f'\nf(x) = {fx(x, function)}')
    if(method == 'a'):
        result_opt_lag(opt, op_xi, op_fx, x, function)
    elif method == 'b':
        result_opt_new(opt, op_xi, op_fx, x, function)
    elif method == 'c':
        result_opt_lag(opt,op_xi,op_fx, x, function)
        result_opt_new(opt, op_xi, op_fx, x, function)

print("\nLaqranj interpolyasiyasi ucun: 1 \nNyuton interpolyasiyasi ucun: 2 \nLaqranj ve Nyuton interpolyasiyasi ucun: 3\n")
method = int(input("Method: "))

match method:
    case 1 :
        lagrange_res()
        print('\nLaqranj interpolyasiyasi ile Optimal Secme usulu ucun Y, eks halda N duymesini daxil edin : \nY/N')
        op = input()
        if op == 'Y':
            optimal_selection('a')       
        elif op == 'N':
            print('Emeliyyat sonlandirilmisdir!')
        else: print('Bele bir emeliyyat movcud deyildir!')
    case 2 :
        newton_res()
        print('\nNyuton interpolyasiyasi ile Optimal Secme usulu ucun Y, eks halda N duymesini daxil edin : \nY/N')
        op = input()
        if op == 'Y':
            optimal_selection('b')
        elif op == 'N':
            print('Emeliyyat sonlandirilmisdir!')
        else: print('Bele bir emeliyyat movcud deyildir!')
    case 3 :
        lagrange_res()
        newton_res()
        print('\nLaqranj ve Nyuton interpolyasiyasi ile Optimal Secme usulu ucun Y, eks halda N duymesini daxil edin : \nY/N')
        op = input()
        if op == 'Y':
            optimal_selection('c')
        elif op == 'N':
            print('Emeliyyat sonlandirilmisdir!')
        else: print('Bele bir emeliyyat movcud deyildir!')