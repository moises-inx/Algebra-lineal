import sympy as sp

def solve_linear_system(equations, variables):
    """
    Analiza y resuelve un sistema de ecuaciones lineales.

    Args:
    - equations: lista de ecuaciones lineales (en formato sympy.Eq).
    - variables: lista de variables del sistema.

    Returns:
    - Un diccionario con la información del análisis y la solución (si aplica).
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
        result = {
            "type": "inconsistent",
            "message": "El sistema no tiene solución (es inconsistente).",
            "solution": None
        }
    elif rank_coeff == rank_augmented == num_variables:
        solution = sp.solve(equations, variables)
        result = {
            "type": "unique",
            "message": "El sistema tiene una solución única.",
            "solution": solution
        }
    elif rank_coeff == rank_augmented < num_variables:
        solution = sp.solve(equations, variables, dict=True)
        result = {
            "type": "infinite",
            "message": "El sistema tiene infinitas soluciones.",
            "solution": solution
        }
    else:
        result = {
            "type": "error",
            "message": "Error inesperado en el análisis del sistema.",
            "solution": None
        }

    return result

# Ejemplo de uso:
# Definir las variables
x1, x2, x3 = sp.symbols('x1 x2 x3')

# Definir las ecuaciones del sistema
eq1 = sp.Eq(x2 + 5*x3, -4)
eq2 = sp.Eq(x1 + 4*x2 + 3*x3, -2)
eq3 = sp.Eq(2*x1 + 7*x2 + x3, -2)

equations = [eq1, eq2, eq3]
variables = [x1, x2, x3]

# Resolver el sistema
result = solve_linear_system(equations, variables)
print(result["message"])
if result["solution"]:
    print("Solución:", result["solution"])
