#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor: Fran Hidalgo
Fecha: 22/05/2025
Level: BASIC

Descripción:
    1. Solicitar al usuario que introduzca tres valores enteros.
    2. Determinar el valor mayor de los tres introducidos.
    3. Mostrar el resultado del mayor valor en pantalla.
    4. En caso de empate (3 =), indicarlo por consola.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import doctest


# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------
pass


# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------
pass


# ------------------------------------------------------------------------------
# Main Function
# ------------------------------------------------------------------------------
def main() -> None:
    """ **Entry point** of the `script.py` """
    try:
        # Solicitar al usuario que introduzca tres valores enteros
        num1 = int(input("Introduce el 1er valor: "))
        num2 = int(input("Introduce el 2nd valor: "))
        num3 = int(input("Introduce el 3rd valor: "))
    
    # Validar que los datos introducidos son enteros
    except ValueError:
        print("[ERROR] - Debe introducir un valor con el formato correcto")
        return
    
    # Ordenar los datos mediante introducidos mediante una estructura de control
    if num1 == num2 == num3:
        print(f"[INFO] - Los tres valores son iguales: {num1}")
    elif num1 >= num2 and num1 >= num3:
        print(f"[INFO] - El valor mayor es: {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"[INFO] - El valor mayor es: {num2}")
    else:
        print(f"[INFO] - El valor mayor es: {num3}")


# ------------------------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    doctest.testmod()
    main()