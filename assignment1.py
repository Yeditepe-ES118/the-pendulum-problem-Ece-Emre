<<<<<<< HEAD
import math

def find_period(L0, L1):
    g = 9.81
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)
    
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print(f"When L = {float(L):.1f} m, T = {T:.1f} s")
    
    return T0, T1
=======
import math

def find_period(L0, L1):
    g = 9.81
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)
    
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print(f"When L = {float(L):.1f} m, T = {T:.1f} s")
    
    return T0, T1
>>>>>>> b7831897325249f87762a8410e60f7bfdf0ba5da
