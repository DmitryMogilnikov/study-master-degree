import numpy as np

def scalar_prod(v1: np.ndarray, v2: np.ndarray) -> complex:
    return np.vdot(v1, v2)

def norm_vector(vector: np.ndarray) -> float:
    return np.linalg.norm(vector)

def normal_scalar_prod(v1: np.ndarray, v2: np.ndarray) -> complex:
    if len(v1) != len(v2):
        raise TypeError('Вектора разной длины!')

    return scalar_prod(v1, v2) / (norm_vector(v1) * norm_vector(v2)) 

if __name__ == '__main__':
    print('Рассмотрим первую ситуацию когда контуры совпадают:')
    v1 = np.array([1, 1-1j, -1, -1, -1, 1+1j])
    v2 = np.array([1, 1-1j, -1, -1, -1, 1+1j])
    print(normal_scalar_prod(v1, v2))

    print('\nРассмотрим вторую ситуацию когда контур повернут:')
    v1 = np.array([-1j, -1-1j, 1j, 1j, 1j, 1-1j])
    print(normal_scalar_prod(v1, v2))

    print('\nРассмотрим третью ситуацию когда контур повернут:')
    v1 = np.array([-1, -1+1j, 1, 1, 1, -1-1j])
    print(normal_scalar_prod(v1, v2))

    print('\nРассмотрим четвертую ситуацию когда контур повернут:')
    v1 = np.array([+1j, +1+1j, -1j, -1j, -1j, -1+1j])
    print(normal_scalar_prod(v1, v2))


    print('\nЗадание 2\nПосчитаем оранжевые точки для разных фигур:')
    v1_orange = np.array([1, 1+1j, 1-1j, 1, -1-1j, 1-1j, -1+1j,-1-1j, 1+1j, -1+1j])
    v2_orange = np.array([1, 1, 1, -1j, -1j, -1,-1,-1, 1j, 1j])
    print(normal_scalar_prod(v1_orange, v2_orange))

    print('\nПосчитаем зеленые точки для разных фигур:')
    v1_green = np.array([-1+1j,-1-1j, 1+1j, -1+1j, 1, 1+1j, 1-1j, 1, -1-1j, 1-1j])
    v2_green = np.array([-1,-1,-1, 1j, 1j, 1, 1, 1, -1j, -1j])
    print(normal_scalar_prod(v1_green, v2_green))

    print('\nПосчитаем разные точки для звезды:')
    print(normal_scalar_prod(v1_orange, v1_green))

    print('\nПосчитаем разные точки для прямоугольника:')
    print(normal_scalar_prod(v2_orange, v2_green))
