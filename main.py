#Importacion librerias
import os
import math
import matplotlib.pyplot as plt


def f(x: float, y: float) -> float:
    """
    Funcion a resolver: y' = 1 - sen(y)

    :param x: Valor de x
    :param y: Valor de y
    :return: Valor de y'

    """

    return 1 - math.sin(y)


def f_exacta(x: float) -> float:
    """
    Funcion exacta: y = 2 * arccos((x + 2) / sqrt(2 * x^2 + 4 * x + 4))

    :param x: Valor de x
    :return: Valor de y

    """

    return 2 * math.acos((x + 2) / (math.sqrt(2 * x **2 + 4 * x + 4)))


def euler_method(x0: float, y0: float, delta_x: float, n_max) -> tuple:
    """
    Resolucion de la ecuacion diferencial por el metodo de Euler

    :param x0: Valor inicial de x
    :param y0: Valor inicial de y
    :param delta_x: Valor de Δx
    :param n_max: Valor n en x al que se desea llegar
    :return: Tupla con las listas de valores de (x,y)

    """
    x_axis = [x0 + i * delta_x for i in range(int(n_max/delta_x))] # Genera una lista de valores de x desde x0 hasta n_max con un paso de Δx
    y_axis = [0 for i in range(len(x_axis))] # Genera una lista de valores de y de la misma longitud que la lista de valores de x
    y_axis[0] = y0 # Asigna el valor inicial de y

    for i in range(len(x_axis) - 1):
        y_axis[i + 1] = (y_axis[i]) + (f(x_axis[i], y_axis[i]) * delta_x) # Calcula el valor de y en el siguiente paso de x usando el metodo de Euler

    return x_axis, y_axis


def choose_variables() -> tuple:
    """
    Pide al usuario los valores iniciales de x, y, Δx y n en x al que se desea llegar

    :return: Tupla con los valores iniciales de x, y, Δx y n en x al que se desea llegar

    """
    try:
        print("Ecuacion diferencial: y' = 1 - sen(y)")
        x0: float = float(input("Ingrese el valor inicial de x: "))
        y0: float = float(input("Ingrese el valor inicial de y: "))
        delta_x: float = float(input("Ingrese el valor de Δx: "))
        n_max: int = int(input("Ingrese el valor n en x al que se desea llegar: "))
    except ValueError: # Si el usuario ingresa un valor no numerico vuelve a pedir los valores
        os.system("cls")
        print("Valores no validos, ingrese nuevamente...")
        return choose_variables()

    return x0, y0, delta_x, n_max


def graphics(x_axis: list, y_axis: list) -> None:
    """
    Grafica los resultados obtenidos

    :param x_axis: Lista de valores de x
    :param y_axis: Lista de valores de y

    """
    plt.title("Ecuacion diferencial: y' = 1 - sen(y)")
    plt.plot(x_axis, y_axis, "--", label="Euler")
    plt.plot(x_axis, [f_exacta(x_axis[i]) for i in range(len(x_axis))], label="Exacta", alpha=0.5)
    plt.legend()
    plt.show()


def main() -> None:
    """
    Bloque principal del programa

    """
    x0, y0, delta_x, n_max = choose_variables()
    x_axis, y_axis = euler_method(x0, y0, delta_x, n_max)

    graphics(x_axis, y_axis)


if __name__ == "__main__":
    main()

