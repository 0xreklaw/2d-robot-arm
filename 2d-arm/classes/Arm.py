from typing import Tuple
import pygame
import math

class Arm:
    def __init__(self, base_pos: Tuple[int, int], linkage_length: int, num_linkages: int):
        self.base_pos = base_pos
        self.linkage_length = linkage_length
        self.num_linkages = num_linkages
        self.joint_positions = [self.base_pos] + [(0, 0)] * num_linkages
        self.update_joint_positions()

    def update_joint_positions(self):
        for i in range(1, self.num_linkages + 1):
            prev_x, prev_y = self.joint_positions[i - 1]
            angle = math.atan2(self.joint_positions[i][1] - prev_y, self.joint_positions[i][0] - prev_x)
            joint_x = prev_x + self.linkage_length * math.cos(angle)
            joint_y = prev_y + self.linkage_length * math.sin(angle)
            self.joint_positions[i] = (joint_x, joint_y)

    def update_end_effector_pos(self, mouse_pos: Tuple[int, int]):
        target_x, target_y = mouse_pos
        threshold = 1.0  # Distance threshold to stop the IK solver

        for _ in range(10):  # Iteration limit to ensure convergence
            for i in reversed(range(1, self.num_linkages + 1)):
                # Calculate current end effector position
                effector_x, effector_y = self.joint_positions[-1]
                
                # Calculate the vector from the current joint to the end effector
                vector_ex = effector_x - self.joint_positions[i - 1][0]
                vector_ey = effector_y - self.joint_positions[i - 1][1]
                
                # Calculate the vector from the current joint to the target position
                vector_tx = target_x - self.joint_positions[i - 1][0]
                vector_ty = target_y - self.joint_positions[i - 1][1]
                
                # Calculate the angles
                angle_e = math.atan2(vector_ey, vector_ex)
                angle_t = math.atan2(vector_ty, vector_tx)
                
                # Calculate the rotation angle
                rotation_angle = angle_t - angle_e
                
                # Update joint positions
                for j in range(i, self.num_linkages + 1):
                    joint_x = self.joint_positions[j][0] - self.joint_positions[i - 1][0]
                    joint_y = self.joint_positions[j][1] - self.joint_positions[i - 1][1]
                    
                    rotated_x = joint_x * math.cos(rotation_angle) - joint_y * math.sin(rotation_angle)
                    rotated_y = joint_x * math.sin(rotation_angle) + joint_y * math.cos(rotation_angle)
                    
                    self.joint_positions[j] = (
                        rotated_x + self.joint_positions[i - 1][0],
                        rotated_y + self.joint_positions[i - 1][1]
                    )
                
                # Check if the end effector is close enough to the target
                if math.sqrt((effector_x - target_x) ** 2 + (effector_y - target_y) ** 2) < threshold:
                    return

    def draw(self, screen):
        for i in range(self.num_linkages):
            pygame.draw.line(screen, (0, 0, 0), self.joint_positions[i], self.joint_positions[i + 1], 5)
            pygame.draw.circle(screen, (0, 0, 0), self.joint_positions[i], 5, 0)
        pygame.draw.circle(screen, (1, 0, 0), self.joint_positions[-1], 5, 0)
