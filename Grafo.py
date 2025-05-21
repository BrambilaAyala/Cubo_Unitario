import numpy as np
import matplotlib.pyplot as plt

#Vertices
vertices_proj = np.array([
    [0.000, 0.000, 0.000],     # a'
    [0.558, -0.036, -0.496],   # b'
    [0.723, 0.186, -0.390],    # c'
    [0.165, 0.221, 0.107],     # d'
    [0.246, -0.133, 0.307],    # e'
    [0.804, -0.169, -0.190],   # f'
    [0.969, 0.052, -0.083],    # g'
    [0.411, 0.088, 0.414]      # h'
])

# Conexiones de las aristas
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # base
    (4, 5), (5, 6), (6, 7), (7, 4),  # parte superior
    (0, 4), (1, 5), (2, 6), (3, 7)   # verticales
]

# Dibujar la proyeccion de los puntos
fig, ax = plt.subplots(figsize=(6, 6))
for start, end in edges:
    x_coords = [vertices_proj[start][0], vertices_proj[end][0]]
    y_coords = [vertices_proj[start][1], vertices_proj[end][1]]
    ax.plot(x_coords, y_coords, 'k')

labels = ["a'", "b'", "c'", "d'", "e'", "f'", "g'", "h'"]
for i, (x, y, _) in enumerate(vertices_proj):
    ax.text(x, y, labels[i], fontsize=10, color='blue')

ax.set_aspect('equal')
ax.set_title("Proyección Axonométrica Trimétrica del Cubo")
ax.axis('off')
plt.tight_layout()
plt.show()
