def Euler(f, y, t, dt, params=[]):
    RHS = f(t, y, *params)
    y += RHS*dt

def RHS(t, y, *params):
    dy = np.zeros_like(y)
    dy[0] = -kx / m
    dy[1] = y[1]
    return dy


