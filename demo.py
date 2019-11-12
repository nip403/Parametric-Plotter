from engine import Grapher

def x(t):
    return np.cos(t)*100

def y(t):
    return np.sin(t)*50

def main(g):
    g.set_time_constraints(t0=0, step=0.02, fps=50)
    g.init_x_eq(x)
    g.init_y_eq(y)

    g.begin()

if __name__ == "__main__":
    g = Grapher(winsize=500, axis=500)
    main(g)
