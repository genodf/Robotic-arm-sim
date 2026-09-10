import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from kinematics import forward_kinematics

def draw_arm(base, elbow, end_effector, target_x, target_y):
    x0, y0 = base
    x1, y1 = elbow
    x2, y2 = end_effector
    
    x_points = [x0, x1, x2]
    y_points = [y0, y1, y2]
    
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.25)
    
    ax_theta1 = fig.add_axes([0.20, 0.12, 0.65, 0.03])
    ax_theta2 = fig.add_axes([0.20, 0.06, 0.65, 0.03])
    
    slider_theta1 = Slider(ax=ax_theta1, label="θ1 (degrees)", valmin=-180, valmax=180, valinit=theta1_degrees)
    slider_theta2 = Slider(ax=ax_theta2, label="θ2 (degrees)", valmin=-180, valmax=180, valinit=theta2_degrees)
    
    arm_line, = ax.plot(x_points, y_points, marker="o", linewidth=3)
    ax.plot(target_x, target_y, marker="x", markersize=10, color="red", label="Target")
    end_effector_point, = ax.plot(x2, y2, marker="s", markersize=10, label="End-effector")
    
    ax.set_aspect("equal", adjustable="box")
    workspace_limit = L1 + L2 + 20
    ax.set_xlim(-workspace_limit, workspace_limit)  
    ax.set_ylim(-workspace_limit, workspace_limit)
    ax.set_xlabel("x position (mm)")
    ax.set_ylabel("y position (mm)")
    ax.set_title("2-Link Planar Robot Arm")
    ax.grid(True)
    ax.legend()
    
    def update(value):
        new_theta1 = np.radians(slider_theta1.val)
        new_theta2 = np.radians(slider_theta2.val)
        new_base, new_elbow, new_end_effector = forward_kinematics(new_theta1, new_theta2, L1, L2)
        
        dx = new_end_effector[0] - target_x
        dy = new_end_effector[1] - target_y
        distance_to_target = np.hypot(dx, dy)
        
        if distance_to_target <= TARGET_TOLERANCE:
            print("Target reached!")
            
        new_x_points = (new_base[0], new_elbow[0], new_end_effector[0])
        new_y_points = (new_base[1], new_elbow[1], new_end_effector[1])
        arm_line.set_data(new_x_points, new_y_points)
        end_effector_point.set_data([new_end_effector[0]], [new_end_effector[1]])
        fig.canvas.draw_idle()
        
    slider_theta1.on_changed(update)
    slider_theta2.on_changed(update)
    plt.show()
    
    
L1 = 120
L2 = 100
TARGET_TOLERANCE = 8
# max_reach = L1 + L2
# min_reach = abs(L1 - L2)

target_x = 150
target_y = 80
# target_distance = np.hypot(target_x, target_y)
# print(f"Target distance from base: {target_distance:.2f} mm")

# if target_distance > max_reach:
#     print("Target is out of reach. (TOO FAR)")
# elif target_distance < min_reach:
#     print("Target is out of reach. (TOO CLOSE)")
# else:
#     print("Target is within reach.")
    
    
theta1_degrees = 30
theta2_degrees = 45

theta1 = np.radians(theta1_degrees)
theta2 = np.radians(theta2_degrees)

base, elbow, end_effector = forward_kinematics(theta1, theta2, L1, L2)

# print(f"Elbow position: ({elbow[0]:.2f}, {elbow[1]:.2f}) mm")
# print(f"End effector position: ({end_effector[0]:.2f}, {end_effector[1]:.2f}) mm")

draw_arm(base, elbow, end_effector, target_x, target_y)