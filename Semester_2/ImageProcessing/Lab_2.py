import numpy as np

def normal_scalar_prod(v1, v2):
    if len(v1) != len(v2):
        print('Вектора разной длины!')
        return

    print(f'For vectors: \n {v1=}, \n {v2=}')
    scalar_prod = np.vdot(v1, v2)
    print(f'{scalar_prod=}')

    norm_v1 = np.sqrt(sum(abs((v1))**2))
    norm_v2 = np.sqrt(sum(abs((v2))**2))

    print(f'{norm_v1=}\n{norm_v2=}')

    n_scalar_prod = scalar_prod / (norm_v1 * norm_v2) 
    return np.round(n_scalar_prod, 3)

def print_nsp_angle_and_abs(nsp):
    print(f'{nsp=}')

    nsp_angle = np.degrees(np.arccos(nsp.real))
    print(f'{nsp_angle} grad')

    nsp_abs = abs(nsp)
    print(f'{nsp_abs=}')


print('Рассмотрим первую ситуацию когда контуры совпадают:')
v1 = np.array([1, 1-1j, -1, -1, -1, 1+1j])
v2 = np.array([1, 1-1j, -1, -1, -1, 1+1j])
nsp = normal_scalar_prod(v1=v1, v2=v2)
print_nsp_angle_and_abs(nsp=nsp)

print('\nРассмотрим вторую ситуацию когда контур повернут:')
v1 = np.array([-1j, -1-1j, 1j, 1j, 1j, 1-1j])
nsp = normal_scalar_prod(v1=v1, v2=v2)
print_nsp_angle_and_abs(nsp=nsp)

print('\nРассмотрим третью ситуацию когда контур повернут:')
v1 = np.array([-1, -1+1j, 1, 1, 1, -1-1j])
nsp = normal_scalar_prod(v1=v1, v2=v2)
print_nsp_angle_and_abs(nsp=nsp)

print('\nРассмотрим четвертую ситуацию когда контур повернут:')
v1 = np.array([+1j, +1+1j, -1j, -1j, -1j, -1+1j])
nsp = normal_scalar_prod(v1=v1, v2=v2)
print_nsp_angle_and_abs(nsp=nsp)


print('\nЗадание 2\nПосчитаем оранжевые точки для разных фигур:')
v1_orange = np.array([1, 1+1j, 1-1j, 1, -1-1j, 1-1j, -1+1j,-1-1j, 1+1j, -1+1j])
v2_orange = np.array([1, 1, 1, -1j, -1j, -1,-1,-1, 1j, 1j])
nsp = normal_scalar_prod(v1=v1_orange, v2=v2_orange)
print_nsp_angle_and_abs(nsp=nsp)

print('\nПосчитаем зеленые точки для разных фигур:')
v1_green = np.array([-1+1j,-1-1j, 1+1j, -1+1j, 1, 1+1j, 1-1j, 1, -1-1j, 1-1j])
v2_green = np.array([-1,-1,-1, 1j, 1, 1, 1, 1, -1j, -1j])
nsp = normal_scalar_prod(v1=v1_green, v2=v2_green)
print_nsp_angle_and_abs(nsp=nsp)

print('\nПосчитаем разные точки для звезды:')
nsp = normal_scalar_prod(v1=v1_orange, v2=v1_green)
print_nsp_angle_and_abs(nsp=nsp)

print('\nПосчитаем разные точки для прямоугольника:')
nsp = normal_scalar_prod(v1=v2_orange, v2=v2_green)
print_nsp_angle_and_abs(nsp=nsp)

