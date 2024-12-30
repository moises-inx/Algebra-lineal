import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

def plot_vector_space(vectors, dim=2):
    """
    Simula un espacio vectorial y grafica los vectores asociados.

    Args:
    - vectors: Lista de vectores a graficar (listas o arrays de longitud 2 o 3).
    - dim: Dimensión del espacio (2 o 3).
    """
    if dim not in [2, 3]:
        raise ValueError("Solo se admiten espacios de 2 o 3 dimensiones.")

    vectors = np.array(vectors)

    if dim == 2:
        # Configuración de la gráfica 2D
        plt.figure(figsize=(8, 8))
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)

        # Graficar cada vector
        for vec in vectors:
            plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color=np.random.rand(3,))

        # Limitar la gráfica
        max_val = np.max(np.abs(vectors)) + 1
        plt.xlim(-max_val, max_val)
        plt.ylim(-max_val, max_val)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Simulación de un espacio vectorial en 2D')
        plt.show()

    elif dim == 3:
        # Configuración de la gráfica 3D
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(0, 0, 0, vectors[:, 0], vectors[:, 1], vectors[:, 2], color=np.random.rand(len(vectors), 3))

        # Limitar la gráfica
        max_val = np.max(np.abs(vectors)) + 1
        ax.set_xlim([-max_val, max_val])
        ax.set_ylim([-max_val, max_val])
        ax.set_zlim([-max_val, max_val])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.title('Simulación de un espacio vectorial en 3D')
        plt.show()

def check_independence(vectors):
    """
    Verifica si un conjunto de vectores es linealmente independiente.

    Args:
    - vectors: Lista de vectores (listas o arrays).

    Returns:
    - True si son linealmente independientes, False en caso contrario.
    """
    matrix = np.array(vectors).T
    rank = np.linalg.matrix_rank(matrix)
    return rank == len(vectors)

# Ejemplo de uso:
# Lista de vectores en 2D
vectors_2d = [[2, 3], [-1, 4], [3, -2]]

# Graficar en 2D
plot_vector_space(vectors_2d, dim=2)

# Comprobar independencia lineal en 2D
is_independent_2d = check_independence(vectors_2d)
print("¿Los vectores en 2D son linealmente independientes?", is_independent_2d)

# Lista de vectores en 3D
vectors_3d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Graficar en 3D
plot_vector_space(vectors_3d, dim=3)

# Comprobar independencia lineal en 3D
is_independent_3d = check_independence(vectors_3d)
print("¿Los vectores en 3D son linealmente independientes?", is_independent_3d)
