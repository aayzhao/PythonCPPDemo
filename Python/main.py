"""Location of the main method for demonstration."""

from sqrt import sqrt
from function_timer import time_function, compare_functions
import ctypes as ct
import time

def main():
    #setup
    sqrtLib = ct.WinDLL("C:/Users/artil/source/repos/PythonCPPDemo/x64/Debug/SqrtUtil.dll")
    sqrtLib.c_sqrt.argtypes = [ct.c_double]
    sqrtLib.c_sqrt.restype = ct.c_double

    print(sqrtLib.c_sqrt(2.0)) # success!
    compare_functions(sqrtLib.c_sqrt, sqrt)

if __name__ == "__main__":
    main()