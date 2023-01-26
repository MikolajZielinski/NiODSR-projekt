import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from direction_interfaces.msg import Directions
from trajectory_msgs.msg import  JointTrajectory, JointTrajectoryPoint


class ArucoToDirections(Node):

    def __init__(self):
        super().__init__('aruco_to_directions')
        self.listener = self.create_subscription(Directions, '/directions', self.listener_callback, 10)

        self.publisher_ = self.create_publisher(JointTrajectory, '/scaled_joint_trajectory_controller/joint_trajectory', 10)
        self.positions = [0.0, -1.57, 0.0, -1.57, 0.0, 0.0]
        timer_period = 4
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        if msg.up:
            self.positions = [0.0, -0.785, 0.0, -1.57, 0.0, 0.0]

        elif msg.down:
            self.positions = [0.0, -2.355, 0.0, -1.57, 0.0, 0.0]

        elif msg.left:
            self.positions = [1.57, -0.785, 0.0, -1.57, 0.0, 0.0]

        elif msg.right:
            self.positions = [1.57, -2.355, 0.0, -1.57, 0.0, 0.0]

        elif msg.stop:
            self.positions = [0.0, -1.57, 0.0, -1.57, 0.0, 0.0]

        else:
            self.positions = [0.0, -1.57, 0.0, -1.57, 0.0, 0.0]

    def timer_callback(self):
        point = JointTrajectoryPoint()
        point.positions = self.positions
        point.time_from_start.sec = 4

        traj = JointTrajectory()
        traj.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
        traj.points.append(point)
        self.publisher_.publish(traj)

def main(args=None):
    rclpy.init(args=args)

    aruco_to_directions = ArucoToDirections()

    rclpy.spin(aruco_to_directions)

    aruco_to_directions.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()