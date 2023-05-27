from ctypes import *

if __name__ == '__main__':
    my_functions = cdll.LoadLibrary("./c_code.so")
    my_functions.function.restype = c_double
    N_A = my_functions.function(10000, 10000)
    print(f'{N_A:.6f}')
