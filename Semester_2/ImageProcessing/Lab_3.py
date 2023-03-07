import numpy as np
from Lab_2 import scalar_prod, norm_vector

def auto_correlation(v1: np.ndarray, roll: int = -1) -> complex:
    result = np.zeros(len(v1), dtype=complex)
    
    v1_roll = v1
    for i in range(len(v1)):
        scal_pr = scalar_prod(v1, v1_roll)
        result[i] = scal_pr
        v1_roll = np.roll(v1_roll, roll)
    
    return result

def cross_correlation(v1: np.ndarray, v2: np.ndarray, roll: int = -1) -> np.ndarray:
    if len(v1) != len(v2):
        raise TypeError('Вектора разной длины!')
    
    max_scal_pr: complex = 0 + 0j

    for _ in range(len(v1)):
        max_scal_pr = max(scalar_prod(v1, v2), max_scal_pr)
        v2 = np.roll(v2, roll)
    
    return max_scal_pr/(norm_vector(v1) * norm_vector(v2))

def haar_wavelet(v1: np.ndarray) -> np.ndarray:
    length = v1.shape[0]
    result = np.zeros(shape=(2, length//2), dtype=complex)
    ac_vector = auto_correlation(v1)
    for i in range(0, length, 2):
        result[0, i // 2] = (ac_vector[i] + ac_vector[i+1]) / 2
        result[1, i // 2] = (ac_vector[i] - ac_vector[i+1]) / 2
    return result

def equalize_vector(v1: np.ndarray, new_count) -> np.ndarray:
    result = np.zeros(new_count, dtype=complex)
    count = v1.shape[0]

    if count > new_count:
        for i in range(count):
            result[i * new_count // count] += v1[i]
    elif count < new_count:
        for i in range(new_count):
            idx = i * count / new_count
            j = int(idx)
            k = idx - j
            result[i] = v1[j] * (1 - k) + v1[(j+1) % count] * k 
    else:
        result = v1

    return result


if __name__ == '__main__':
    triangle = np.array([1+1j, 1+1j, 1+1j, 1+1j, 1-1j, 1-1j, 1-1j, 1-1j, -2, -2, -2, -2])
    rhomb = np.array([1+1j, 1+1j, 1+1j, 1-1j, 1-1j, 1-1j, -1-1j, -1-1j, -1-1j, -1+1j, -1+1j, -1+1j])
    star = np.array([1-1j, 1, -1-1j, 1-1j, -1+1j,-1-1j, 1+1j, -1+1j, 1, 1+1j])
    cross = np.array([1, 1, -1j, 1, -1j, -1j, -1, -1j, -1, -1, 1j, -1, 1j, 1j, 1, 1j])

    print('Triangle autocorellation:')
    print(auto_correlation(triangle))
    print('Triangle haar wavelet:')
    print(f'{haar_wavelet(triangle)}\n')

    print('Rhomb autocorellation:')
    print(auto_correlation(rhomb))
    print('Rhomb haar wavelet:')
    print(f'{haar_wavelet(rhomb)}\n')

    print('Star autocorellation:')
    print(auto_correlation(star))
    print('Star haar wavelet:')
    print(f'{haar_wavelet(star)}\n')

    print('Cross autocorellation:')
    print(auto_correlation(cross))
    print('Cross haar wavelet:')
    print(f'{haar_wavelet(cross)}\n')


    print('\nTask 2:')
    print('Cross equalization:')
    print(equalize_vector(cross, 12))
    print(equalize_vector(star, 20))

    #print(cross_correlation(v1, v2))
