import sympy as sp

# Definimos las variables
x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')

# Definimos las ecuaciones del sistema
eq1 = sp.Eq(2*x1 - 2*x2 - 2*x3 + 1*x4, 0)
eq2 = sp.Eq(sp.pi*x1 + 1*x2 + 2*x3 - sp.pi*x4, 0)
eq3 = sp.Eq(1*x1 + 11*x2 - 1*x3 + 4*x4, 0)

def row_operations_to_echelon(matrix):
    """
    Convierte la matriz aumentada en su forma escalonada mediante operaciones elementales
    y muestra los pasos aplicados.
    
    Args:
    - matrix: Matriz aumentada a transformar.
    
    Returns:
    - Matriz en forma escalonada.
    """
    mat = matrix.as_mutable()
    rows, cols = mat.shape
    step = 1

    for i in range(min(rows, cols - 1)):  # Última columna es la de términos independientes
        # Buscar el pivote
        pivot_row = i
        while pivot_row < rows and mat[pivot_row, i] == 0:
            pivot_row += 1

        if pivot_row == rows:
            continue  # Saltar si la columna está llena de ceros

        # Intercambiar filas si es necesario
        if pivot_row != i:
            mat.row_swap(i, pivot_row)
            print(f"Paso {step}: Intercambiar fila {i+1} con fila {pivot_row+1}")
            sp.pprint(mat)
            step += 1

        # Hacer que el pivote sea 1 dividiendo la fila
        pivot_value = mat[i, i]
        if pivot_value != 1:
            mat.row_op(i, lambda v, j: v / pivot_value)
            print(f"Paso {step}: Dividir fila {i+1} por {pivot_value}")
            sp.pprint(mat)
            step += 1

        # Hacer ceros debajo del pivote
        for j in range(i + 1, rows):
            if mat[j, i] != 0:
                factor = mat[j, i]
                mat.row_op(j, lambda v, k: v - factor * mat[i, k])
                print(f"Paso {step}: Restar {factor} veces fila {i+1} de fila {j+1}")
                sp.pprint(mat)
                step += 1

    return mat

def row_operations_to_reduced_echelon(matrix):
    """
    Convierte la matriz en su forma escalonada reducida y muestra los pasos aplicados.
    
    Args:
    - matrix: Matriz en forma escalonada.
    
    Returns:
    - Matriz en forma escalonada reducida.
    """
    mat = matrix.as_mutable()
    rows, cols = mat.shape
    step = 1

    for i in reversed(range(rows)):
        # Encontrar el pivote
        pivot_col = None
        for j in range(cols - 1):
            if mat[i, j] != 0:
                pivot_col = j
                break

        if pivot_col is None:
            continue  # Saltar si la fila es cero

        # Hacer ceros encima del pivote
        for j in range(i):
            if mat[j, pivot_col] != 0:
                factor = mat[j, pivot_col]
                mat.row_op(j, lambda v, k: v - factor * mat[i, k])
                print(f"Paso {step}: Restar {factor} veces fila {i+1} de fila {j+1}")
                sp.pprint(mat)
                step += 1

    return mat

def analyze_system(equations, variables):
    """
    Analiza un sistema de ecuaciones lineales y muestra la matriz ampliada,
    las transformaciones hasta la forma escalonada, la forma escalonada reducida
    y las soluciones.
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

    # Convertimos la matriz a su forma escalonada manualmente
    print("\nTransformaciones hasta la forma escalonada:")
    echelon_matrix = row_operations_to_echelon(augmented_matrix)

    # Convertimos la matriz a su forma escalonada reducida
    print("\nTransformaciones hasta la forma escalonada reducida:")
    reduced_matrix = row_operations_to_reduced_echelon(echelon_matrix)

    # Determinamos el tipo de solución
    if rank_coeff < rank_augmented:
        print("\nEl sistema no tiene solución (es inconsistente).")
    
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
