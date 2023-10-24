# def project_3d_to_2d(vertices):
#     model_view = glGetDoublev(GL_MODELVIEW_MATRIX)
#     projection = glGetDoublev(GL_PROJECTION_MATRIX)
#     viewport = glGetIntegerv(GL_VIEWPORT)

#     result = []
#     for vertex in vertices:
#         if vertex == 's':
#             result.append('s')
#         else:
#             x, y, z = gluProject(*vertex, model_view, projection, viewport)
#             x = x / (WIDTH/2) - 1.0
#             y = -1 * (y / (HEIGHT/2) - 1.0)
#             result.append((x, y))
#     return result

# def print_2d_coordinates():
#     print("2D Coordinates of Cube Vertices:")
#     print(project_3d_to_2d(cube))

# def keyboard(key, x, y):
#     if key == b'p':
#         print_2d_coordinates()