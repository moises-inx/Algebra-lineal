# Reimportamos las bibliotecas necesarias y redefinimos el sistema tras el reinicio
import sympy as sp

# Definimos las variables
x1, x2, x3 = sp.symbols('x1 x2 x3')

# Definimos las ecuaciones del sistema
eq1 = sp.Eq(x2 + 5*x3, -4)
eq2 = sp.Eq(x1 + 4*x2 + 3*x3, -2)
eq3 = sp.Eq(2*x1 + 7*x2 + x3, -2)

# Función para analizar el sistema
def analyze_system(equations, variables):
    """
    Analiza un sistema de ecuaciones lineales para determinar si tiene una solución única,
    infinitas soluciones o ninguna solución.
    
    Args:
    - equations: lista de ecuaciones.
    - variables: variables del sistema.
    
    Returns:
    - str indicando el tipo de solución.
    """
    # Creamos la matriz aumentada del sistema
    coeff_matrix = sp.Matrix([[eq.lhs.coeff(v) for v in variables] for eq in equations])
    rhs_matrix = sp.Matrix([eq.rhs for eq in equations])
    augmented_matrix = coeff_matrix.row_join(rhs_matrix)
    
    # Calculamos el rango de la matriz de coeficientes y el rango de la matriz aumentada
    rank_coeff = coeff_matrix.rank()
    rank_augmented = augmented_matrix.rank()
    num_variables = len(variables)
    
    # Determinamos el tipo de solución
    if rank_coeff < rank_augmented:
        return "El sistema no tiene solución (inconsistente)."
    elif rank_coeff == rank_augmented == num_variables:
        return "El sistema tiene una solución única."
    elif rank_coeff == rank_augmented < num_variables:
        return "El sistema tiene infinitas soluciones."
    else:
        return "Error inesperado en el análisis del sistema."

# Usamos la función en el sistema dado
equations = [eq1, eq2, eq3]
variables = [x1, x2, x3]
analysis_result = analyze_system(equations, variables)
print(analysis_result)
