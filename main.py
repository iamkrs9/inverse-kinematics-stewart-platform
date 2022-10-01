import stewart_platform as sp


def main():
    print("Inverse Kinematics for 6DOF Stewart Platform\n\n")

    base_x = float(input("Enter x coordinate of anchor point on Base defined in Base coordinate frame: "))
    base_y = float(input("Enter y coordinate of anchor point on Base defined in Base coordinate frame: "))

    platform_x = float(
        input("\n\nEnter x coordinate of anchor point on Platform defined in Platform coordinate frame: "))
    platform_y = float(input("Enter y coordinate of anchor point on Platform defined in Platform coordinate frame: "))

    platform_x_in_base = float(input("\n\nEnter x coordinate of Platform origin in Base coordinate frame: "))
    platform_y_in_base = float(input("Enter y coordinate of Platform origin in Base coordinate frame: "))
    platform_z_in_base = float(input("Enter z coordinate of Platform origin in Base coordinate frame: "))

    alpha = float(input("\n\nEnter angle in degrees for rotation about z-axis: "))
    beta = float(input("Enter angle in degrees for rotation about y-axis: "))
    gamma = float(input("Enter angle in degrees for rotation about x-axis: "))

    T = sp.point_in_3d(platform_x_in_base, platform_y_in_base, platform_z_in_base)
    Rpb = sp.calc_rotation(alpha, beta, gamma)
    p = sp.point_in_3d(platform_x, platform_y)
    b = sp.point_in_3d(base_x, base_y)

    l = sp.calc_link_length(T, Rpb, p, b)
    print("The lenght of the leg is: ", l)


if __name__ == '__main__':
    main()
