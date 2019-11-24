from engine import Grapher
import numpy as np

def x(t):
    return np.cos(t)*100

def y(t):
    return x(t-1)*2 % 100

def main(g):
    g.set_time_constraints(t0=-100, step=0.02, fps=50)
    g.init_x_eq(x)
    g.init_y_eq(y)

    g.begin()

if __name__ == "__main__":
    g = Grapher(winsize=500, axis=500)
    main(g)

# Neat equations I found:
#   x = 100cos(t)
#   y = 50log(|x(t)| - |2x(t-1) % 100 - 75|)
#
#   x = 100cos(t)
#   y = log(t)x(t)
#
#   x = 2t
#   y = e**(t/100) + 100sin(t - cos(t))
