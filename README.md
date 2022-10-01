# inverse-kinematics-stewart-platform
Calculate Link length of a Stewart Platform link using inverse kinematics
# Inputs:
- T = Translation of Platform origin w.r.t Base origin
- alpha, beta and gamma angles: Angles to calculate rotation matrix. Rotation is about z, y and x axis and in that order.
- Anchor point coordinates connected to Base (in Base frame)
- Anchor point coordinates connected to Platform (in Platform frame)

# Output:
- Link length for the given parameters

# Note:
This is structured such that the functions can be called to calculate length of a single link. Using this, one can obtain the full inverse kinematics involving all the links if their anchor points coordinates are given in Base and Platform.
