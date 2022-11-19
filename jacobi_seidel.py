def set_func(n):
    print('Tenlikler sisitemini daxil edin')
    set_equations = []
    equations = []
    for i in range(n):
        equation = input(f'{i + 1})')
        set_equations.append(equation)
    for i in range(n):
        equations.append(set_equations[i].split(' '))
    equations = [list( map(int, i) ) for i in equations]
    return equations

def print_func(equations, n):
    y = []
    for i in range(n):
        for j in range(n + 1):
            if j < n:
                print(f'{equations[i][j]}x{j + 1}',end=' ')
        y.append(equations[i][n])
        print(equations[i][n])
    return y
        
def set_x0():
    print('\nx0 : ',end='')
    x = input()
    x0 = x.split(' ')
    return [float(i) for i in x0]

def jacobi(equations, x0, y, n):
    xi = []
    for i in range(n):
        sum = 0
        global xii
        for j in range(n):
            if i == j:
                xii = (equations[i][j])
                continue
            else:
                sum += (-1) * (x0[j] * equations[i][j])
        xi.append((sum + y[i]) / xii)
    return xi

def seidel(equations, x0, y, n):
    xi = []
    for i in range(n):
        sum = 0
        global xii
        for j in range(n):
            if i == j:
                xii = (equations[i][j])
                continue
            else:
                 sum += (-1) * (x0[j] * equations[i][j])   
        xi.append((sum + y[i]) / xii);
        x0[i] = xi[i]
    return xi

def result_jacobi(equation, iter, x0, y, n):
    print(f'x0 = {x0}')    
    for i in range(1,iter + 1):
        x_0 =x0  
        print(f'x{i} = {jacobi(equation, x_0, y, n)}')
        x0 = jacobi(equation, x_0, y, n)
        
def result_seidel(equation, iter, x0, y, n):
    print(f'x0 = {x0}')    
    for i in range(1,iter + 1):
        x_0 =x0  
        x0 = seidel(equation, x_0, y, n)
        print(f'x{i} = {x0}')
        
n = int(input('Tenliklerin sayini daxil edin : '))
equation = set_func(n)
print('\nTenlikler sistemi : ')
y = print_func(equation, n)
x0 = set_x0()
iter = int(input('\nIterasiyalarin sayini daxil edin : '))
method = int(input("\nYakobi usulu ucun: 1\nZeydel usulu ucun: 2\nYakobi ve Zeydel usulu ucun 3\n"))

match(method):
    case 1:
        print(f'\nYakobi usulu')
        result_jacobi(equation, iter, x0, y, n)
    case 2:
        print(f'\nZeydel usulu')
        result_seidel(equation, iter, x0, y, n)
    case 3:
        print(f'\nYakobi usulu')
        result_jacobi(equation, iter, x0, y, n)
        print(f'\nZeydel usulu')
        result_seidel(equation, iter, x0, y, n)
    case other :
        print('Bele bir emeliyyat movcud deyildir!')              