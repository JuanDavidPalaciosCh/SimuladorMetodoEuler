# Simulador metodo de euler
***
El programa nos permite comparar el metodo numerico de Euler con la solución especifica haciendo uso de la librería Matplotlib y Sympy, para poder ingresar la función a resolver de una ecuación de tipo y'(x) = f(x, y)

## Table of Contents
1. [Información general](#general-info)
2. [Ejemplo de uso](#example)
3. [Tecnologías](#technologies)
4. [Instalación y uso](#installation)

<a name="general-info"></a>
### Información general
***
El programa simula el metodo de euler para resolver ecuaciones diferenciales ordinarias de primer orden. El programa permite ingresar la ecuacion diferencial, el valor inicial y el intervalo de tiempo para poder graficar la solucion exacta de la ecuacion diferencial y la solucion aproximada por el metodo de Euler.

<a name="example"></a>
##Ejemplo de uso:
***
Input:
```
Ingrese la función: y'= y(x) * sin(x)
    Ingrese el valor inicial de x: 0
    Ingrese el valor inicial de y: 1
    Ingrese el valor de Δx: 0.01
    Ingrese el valor de x en la que se desea graficar: 20
```

Output:
```
Ecuación diferencial:
d
──(y(x)) = y(x)⋅sin(x)
dx


Solución general:
           -cos(x)
y(x) = C₁⋅ℯ


Solución específica:
                         -cos(x)
y(x) = 2.71828182845905⋅ℯ

(https://github.com/JuanDavidPalaciosCh/SimuladorMetodoEuler/assets/example.jpg)
```

<a name="technologies"></a>
### Tecnologías
***
A list of technologies used within the project:
* [Python](https://www.python.org): Version 3.11.2 
* [SymPy](https://www.sympy.org/es/): Version 1.11.1
* [Matplotlib](https://matplotlib.org): Version 3.7.1

<a name="installation"></a>
## Instalación y uso
***
```
$ git clone https://github.com/JuanDavidPalaciosCh/SimuladorMetodoEuler.git
$ cd ../path/to/the/file
$ py main.py
```