import os
from DiferencialFuncion import DiferencialFunction

# eq ejemplo y' = 9*cos(10*x) + 2

def main():

    while True:
        try:
            f: str = input("Ingrese la función: y'= ")
            x0: float = float(input("Ingrese el valor inicial de x: "))
            y0: float = float(input("Ingrese el valor inicial de y: "))
            delta_x = float(input("Ingrese el valor de Δx: "))
            n_max = float(input("Ingrese el valor de x en la que se desea graficar: "))
            print("\n")
        except ValueError:
            os.system("cls")
            print("Los valores ingresados no son válidos intente nuevamente", "\n")
            continue

        try:

            function = DiferencialFunction(f, x0, y0, delta_x, n_max) # Crea un objeto de la clase DiferencialFunction


            print("Ecuación diferencial: ")
            function.show_eq()

            print("Solución general: ")
            function.show_general_solution()

            print("Solución específica: ")
            function.show_specific_solution()

        except:
            print("Ocurrio un error con la funcion ingresada, intente nuevamente", "\n")
            continue

        try:
            function.graph() # Grafica la solucion exacta y la solucion aproximada con el metodo de euler

        except NameError:
            print("No se pudo graficar la solución", "\n")
            continue

        flag = input("Presione enter para continuar o 'Q' para terminar... ")

        os.system("cls")

        if flag.lower() == "q":
            os._exit(0)


if __name__ == "__main__":
    main()
