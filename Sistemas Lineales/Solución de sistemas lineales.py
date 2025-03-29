# El código analiza ecuaciones lineales, entregando su matriz apliada y su matriz escalonada correspondiente al sistema.

import sympy as sp

# Definimos las variables
x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')

# Definimos las ecuaciones del sistema
eq1 = sp.Eq(2*x1 - 2*x2 - 2*x3 + 1*x4, 0)
eq2 = sp.Eq(sp.pi*x1 + 1*x2 + 2*x3 - sp.pi*x4, 0)
eq3 = sp.Eq(1*x1 + 11*x2 - 1*x3 + 4*x4, 0)

# Función para analizar el sistema y mostrar detalles adicionales
def analyze_system(equations, variables):
    """
    Analiza un sistema de ecuaciones lineales para determinar si tiene una solución única,
    infinitas soluciones o ninguna solución. También muestra la matriz aumentada,
    su forma escalonada y la forma escalonada reducida si es posible.
    
    Args:
    - equations: lista de ecuaciones.
    - variables: variables del sistema.
    
    Returns:
    - str indicando el tipo de solución.
    """
    # Extraemos la matriz de coeficientes y la matriz de términos independientes
    coeff_matrix, rhs_matrix = sp.linear_eq_to_matrix(equations, variables)
    
    # Matriz aumentada
    augmented_matrix = coeff_matrix.row_join(rhs_matrix)
    
    # Calculamos los rangos
    rank_coeff = coeff_matrix.rank()
    rank_augmented = augmented_matrix.rank()
    num_variables = len(variables)
    
    # Mostramos la matriz aumentada
    print("Matriz aumentada del sistema:")
    sp.pprint(augmented_matrix)

    # Calculamos la forma escalonada
    echelon_form, _ = augmented_matrix.rref()
    print("\nMatriz en su forma escalonada:")
    sp.pprint(echelon_form)

    # Determinamos el tipo de solución
    if rank_coeff < rank_augmented:
        print("\nEl sistema no tiene solución (es inconsistente).")
        return
    
    elif rank_coeff == rank_augmented == num_variables:
        print("\nEl sistema tiene una solución única.")
        solution = sp.linsolve(equations, variables)
        print("Solución única:", solution)
    
    elif rank_coeff == rank_augmented < num_variables:
        print("\nEl sistema tiene infinitas soluciones.")
        
        # Calculamos la solución general
        solution_set = sp.linsolve(equations, variables)
        
        # Variables libres
        free_vars = [v for v in variables if v not in coeff_matrix.nullspace()]
        print("Variables libres:", free_vars)
        print("Soluciones generales en términos de parámetros:")
        print(solution_set)

# Usamos la función en el sistema dado
equations = [eq1, eq2, eq3]
variables = [x1, x2, x3, x4]
analyze_system(equations, variables)
