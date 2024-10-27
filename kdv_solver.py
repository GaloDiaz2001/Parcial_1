import numpy as np
import math as math
import matplotlib.pyplot as plt
import numpy as np
import sys

def kdv_sol(u_result,x,Nx,Nt,L,ymax,u,dx,dt):
    for n in range(0, Nt - 1):
        u_next = u.copy()  
    
        for j in range(2, Nx - 2):
            #sabemos que no hay nunca negativo, y eso nos genera inestabilidad por lo tanto forzamos negativos a 0
            if(u[j]< 0):
                u[j] = 0
            #uxxx central
            u_xxx = (u[j+2] - 2 * u[j+1] + 2 * u[j-1] - u[j-2]) / (2 * dx**3)
            #u_xxx = (u[j] - 3 * u[j-1] + 3 * u[j-2] - u[j-3]) / (dx**3)
            # Actualización de u en el próximo tiempo
            u_next[j] = u[j] - dt *u_xxx - dt/dx * (3*u[j]**2 - 3*u[j-1]**2)
        plt.plot(x ,u_next, 'ro--')
        plt.xlim([-L,L])
        plt.ylim([-0.5,ymax])
        plt.grid()
        plt.savefig(f'frame{n}')
        plt.show()
        # Actualización para el siguiente paso temporal
        u = u_next
        u_result[n+1, :] = u
