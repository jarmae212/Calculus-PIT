# SUBMITTED BY:   Margate, JM
#                 Oga, P
# INSTRUCTOR:     Jupiter, DJ#     PIT FOR CALCULUS 2

# ----------------------------------------------------------
#           THE INTEGRATION OF A TANGENT FUNCTION
# ----------------------------------------------------------

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("This program will solve the inputted tangent function")
    print("and displays its graphical representation")
    
    while True:
        x = sp.symbols('x')
        print(" ")
        func_str = input("Enter the tangent function: ")

        try:
            function = sp.sympify(func_str)
            integral = sp.integrate(function, x)
            print("Tangent Function: ", func_str)
            print("Integration: ", integral)

            integrated_func = sp.lambdify(x, integral, 'numpy')

            x_vals = np.linspace(-10, 10, 1000)
            
            y_vals = integrated_func(x_vals)
            

            plt.plot(x_vals, y_vals, label='Integral of ' + func_str)
            plt.xlabel('x')
            plt.ylabel('Integral Value')
            plt.title('Integral of ' + func_str)
            plt.legend()
            plt.grid(True)
            plt.show()

            break

        except sp.SympifyError:
            print("Invalid input function! Please provide a valid function.")
            continue

if __name__ == "__main__":
    main()
