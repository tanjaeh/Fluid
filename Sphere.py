# import numpy as np
# from mayavi import mlab
#
# [phi, theta] = np.mgrid[0:2 * np.pi:12j, 0:np.pi:12j]
# x = np.cos(phi) * np.sin(theta)
# y = np.sin(phi) * np.sin(theta)
# z = np.cos(theta)
#
# def plot_sphere(x_pos, y_pos, z_pos):
#     r = 10
#
#     return mlab.mesh(r * x + x_pos, r * y + y_pos, r * z + z_pos)
#
# def test_points3d():
#     t = np.linspace(0, 4 * np.pi, 20)
#     array = np.zeros_like(t)
#
#     x = np.sin(2 * t)
#     y = np.cos(t)
#     z = np.cos(2 * t)
#     # s = 2 + np.sin(t)
#     s = 2 + np.sin(array)
#
#     return mlab.points3d(x, y, z, s, scale_factor=.25)



