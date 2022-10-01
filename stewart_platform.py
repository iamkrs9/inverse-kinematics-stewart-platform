import numpy as np

cos = np.cos
sin = np.sin


def calc_rotation(alpha_z, beta_y, gamma_x):
    z = np.radians(alpha_z)
    y = np.radians(beta_y)
    x = np.radians(gamma_x)

    r01 = cos(z) * cos(y)
    r02 = -sin(z) * cos(x) + cos(z) * sin(y) * sin(x)
    r03 = sin(z) * sin(x) + cos(z) * sin(y) * cos(x)

    r11 = sin(z) * cos(y)
    r12 = cos(z) * cos(x) + sin(z) * sin(y) * sin(x)
    r13 = -cos(z) * sin(x) + sin(z) * sin(y) * cos(x)

    r21 = -sin(y)
    r22 = cos(y) * sin(x)
    r23 = cos(y) * cos(x)

    R = np.array([[r01, r02, r03], [r11, r12, r13], [r21, r22, r23]])

    return R


def point_in_3d(x, y, z=0.0):
    return np.array([x, y, z])


def calc_link_length(T, Rpb, p, b):
    return np.linalg.norm(T + np.dot(Rpb, p) - b)
