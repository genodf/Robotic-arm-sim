import numpy as np

def forward_kinematics(theta1, theta2, L1, L2):
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    link2_angle = theta1 + theta2

    x2 = x1 + L2 * np.cos(link2_angle)
    y2 = y1 + L2 * np.sin(link2_angle)
    
    return (0, 0), (x1, y1), (x2, y2)                                                                                                           