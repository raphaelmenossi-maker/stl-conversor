from PIL import Image
import numpy as np
from stl import mesh

def jpg_to_stl(input_path, output_path):
    img = Image.open(input_path).convert('L')
    img = img.resize((200, 200))

    data = np.array(img)
    rows, cols = data.shape

    vertices = []
    faces = []

    for i in range(rows):
        for j in range(cols):
            z = (data[i][j] / 255.0) * 10
            vertices.append([i, j, z])

    vertices = np.array(vertices)

    def idx(i, j):
        return i * cols + j

    for i in range(rows - 1):
        for j in range(cols - 1):
            v1 = idx(i, j)
            v2 = idx(i+1, j)
            v3 = idx(i, j+1)
            v4 = idx(i+1, j+1)

            faces.append([v1, v2, v3])
            faces.append([v2, v4, v3])

    faces = np.array(faces)

    m = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))

    for i, f in enumerate(faces):
        for j in range(3):
            m.vectors[i][j] = vertices[f[j]]

    m.save(output_path)