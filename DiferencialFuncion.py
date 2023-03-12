import sympy
import os
import matplotlib.pyplot as plt


x = sympy.symbols('x')
y = sympy.Function('y')


class DiferencialFunction(object): # Ecuaciones ordinarias diferenciales de primer orden

    def __init__(self, f: str, x0: float, y0: float, delta_x: float=0.1, n_max: float=20) -> None:
        """
        Inicializa la clase DiferencialFunction

        :param f: Funcion a resolver del estilo y'=f(x,y)
        :param x0: Valor inicial de x
        :param y0: Valor inicial de y
        :param delta_x: Valor de Δx por defecto 0.1
        :param n_max: Valor de x en la que se desea graficar por defecto 20
        """

        try:
            self.f = sympy.parse_expr(f) # Convierte la funcion a una expresion de sympy
        except SyntaxError:
            os.system("cls")
            print("La función ingresada no es válida intente nuevamente")
        
        self.eq = sympy.Eq(sympy.diff(y(x)), self.f) # Convierte la funcion a una ecuacion diferencial y'=f(x,y)
        self.delta_x = delta_x
        self.n_max = n_max
        self.x0 = x0
        self.y0 = y0

    def solve_general(self) -> sympy.Eq:
        """
        Resuelve la ecuacion diferencial y'=f(x,y) y devuelve la solucion general

        :return: Solucion general de la ecuacion diferencial
        """
        try:
            return  sympy.dsolve(self.eq, y(x)) # Resuelve la ecuacion diferencial de forma general
        except ValueError:
            print("Lo sentimos, no encantramos una solucion")
    
    def solve_specific(self) -> sympy.Eq:
        """
        Resuelve la ecuacion diferencial y'=f(x,y) y devuelve la solucion especifica

        :return: Solucion especifica de la ecuacion diferencial
        """
        ics = {y(self.x0): self.y0} # Condicion inicial (y(x0)=y0

        try:
            solution =  sympy.dsolve(self.eq, y(x), ics=ics) # Resuelve la ecuacion diferencial con la condicion inicial

        except ValueError:
            print("Lo sentimos, no encantramos una solucion")
            os._exit(0)

        try:
            return solution[0] # Si hay dos soluciones, devuelve la positiva
        except TypeError: # Si solo hay una solucion, devuelve la solucion
            return solution
    
    def solve_euler(self) -> tuple:
        """
        Resuelve la ecuacion diferencial y'=f(x,y) con el metodo de euler y devuelve los valores de x y y

        :return: Lista de valores de (x,y)
        """
        x_axis = [self.x0 + (i * self.delta_x) for i in range(int(self.n_max/self.delta_x))]
        y_axis = [0 for i in range(len(x_axis))]
        y_axis[0] = self.y0
        function = sympy.lambdify([x, y(x)], self.f, 'numpy') # Convierte la funcion a una funcion lambda para poder usarla en el metodo de euler

        for i in range(len(x_axis) - 1):
            y_axis[i + 1] = (y_axis[i]) + function(x_axis[i], y_axis[i]) * self.delta_x

        return x_axis, y_axis
    
    def graph(self) -> None:
        """
        Grafica la solucion exacta y la solucion aproximada con el metodo de euler 
        """
        x_axis, y_axis = self.solve_euler()
        f_exacta = sympy.lambdify([x], self.solve_specific().rhs, 'numpy') # Convierte la funcion exacta a una funcion lambda
        plt.title("Ecuacion diferencial: y'={}".format(self.eq.rhs))
        plt.plot(x_axis, y_axis, "--", label="Euler")
        plt.plot(x_axis, [f_exacta(x_axis[i]) for i in range(len(x_axis))], label="Exacta", alpha=0.5)
        plt.legend()
        plt.show()

    def show_eq(self) -> None:
        """
        Muestra la ecuacion diferencial con el metodo sympy.pprint para mejor visualizacion
        """
        sympy.pprint(self.eq)

    def show_general_solution(self) -> None:
        """
        Muestra la solucion general con el metodo sympy.pprint para mejor visualizacion
        """
        sympy.pprint(self.solve_general())

    def show_specific_solution(self) -> None:
        """
        Muestra la solucion especifica con el metodo sympy.pprint para mejor visualizacion
        """
        sympy.pprint(self.solve_specific())



