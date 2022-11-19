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

def opt(op_xi, op_fx, x):
    lag_op= lagrange_polynomial(x, op_xi, op_fx)
    new_op = newton_polynomial(x, op_xi, op_fx)
    return [lag_op, new_op]

def print_op_xi_fx(op_xi, op_fx):
    print_xi(op_xi)
    print_fx(op_fx)
    
def opt_selection(m):
    print('\nOptimal Secme usulu ucun Y, eks halda N duymesini daxil edin : \nY/N')
    op = input()
    if op == 'Y':
        print_op_xi_fx(op_xi, op_fx)
        print(f'\nf(x) = {fx(x, function)}')  
        if m=='l':
            print(f'Laqranj interpolyasiyasi ile Optimal Secme : {opt(op_xi, op_fx, x)[0]}')
            print(f'Netice(Laqranj) : {abs(fx(x, function) - opt(op_xi, op_fx, x)[0])}\n')    
        elif m =='n':
            print(f'Nyuton interpolyasiyasi ile Optimal Secme : {opt(op_xi, op_fx, x)[1]}')
            print(f'Netice(Nyuton) : {abs(fx(x, function) - opt(op_xi, op_fx, x)[1])}\n')
        elif m == 'l_n':
            print(f'Laqranj interpolyasiyasi ile Optimal Secme : {opt(op_xi, op_fx, x)[0]}')
            print(f'Netice(Laqranj) : {abs(fx(x, function) - opt(op_xi, op_fx, x)[0])}\n')  
            print(f'Nyuton interpolyasiyasi ile Optimal Secme : {opt(op_xi, op_fx, x)[1]}')
            print(f'Netice(Nyuton) : {abs(fx(x, function) - opt(op_xi, op_fx, x)[1])}\n')            
    elif op == 'N':
        print('Emeliyyat sonlandirilmisdir!')
    else: print('Bele bir emeliyyat movcud deyildir!')
    
def fx(x, function):
    func = function(x)
    return func


num_of_x = int(input('X-lerin sayini teyin edin: '))
x_i = set_x(num_of_x)
f_x = get_fx(x_i, function)
print_fx(f_x)
x = float(input('\nx-i daxil edin : '))
print(f'\nf(x) = {fx(x, function)}')
op_xi = opt_xi(num_of_x)
op_fx = get_fx(op_xi, function)

print("\nLagranj usulu ucun: 1\nNyuton usulu ucun: 2\nLagranj ve Nyuton usulu ucun: 3")
method = int(input())

match(method):
    case 1:
        print(f'\nLaqranj interpolyasiyasi : {lagrange_polynomial(x,x_i, f_x)}')
        print(f'Netice(Laqranj) : {abs(fx(x,function) - lagrange_polynomial(x, x_i, f_x))}') 
        opt_selection('l') 
    case 2:
        print(f'\nNyuton interpolyasiyasi : {newton_polynomial(x, x_i, f_x)}')
        print(f'Netice(Nyuton) : {abs(fx(x, function) - newton_polynomial(x, x_i, f_x))}')
        opt_selection('n')
    case 3:
        print(f'\nLaqranj interpolyasiyasi : {lagrange_polynomial(x,x_i, f_x)}')
        print(f'Netice(Laqranj) : {abs(fx(x,function) - lagrange_polynomial(x, x_i, f_x))}')
        print(f'\nNyuton interpolyasiyasi : {newton_polynomial(x, x_i, f_x)}')
        print(f'Netice(Nyuton) : {abs(fx(x, function) - newton_polynomial(x, x_i, f_x))}') 
        opt_selection('l_n')   
    case other :
        print('Bele bir emeliyyat movcud deyildir!')           