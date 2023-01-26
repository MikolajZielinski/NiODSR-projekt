import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from direction_interfaces.msg import Directions
from ros2_aruco_interfaces.msg import ArucoMarkers


class ArucoToDirections(Node):

    def __init__(self):
        super().__init__('aruco_to_directions')
        self.aruco_marekr = self.create_subscription(ArucoMarkers, '/aruco_markers', self.listener_callback, 10)
        self.aruco_marekr
        self.direction = Directions()

        self.publisher_ = self.create_publisher(Directions, '/directions', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        if msg.poses[0].position.x <= 216 and msg.poses[0].position.y >= 173 and msg.poses[0].position.y <= 306:
            self.direction.left = True
            self.direction.up = False
            self.direction.down = False
            self.direction.right = False
            self.direction.stop = False

        elif msg.poses[0].position.x >= 382 and msg.poses[0].position.y >= 173 and msg.poses[0].position.y <= 306:
            self.direction.right = True
            self.direction.up = False
            self.direction.down = False
            self.direction.left = False
            self.direction.stop = False

        elif msg.poses[0].position.y <= 173 and msg.poses[0].position.x >= 216 and msg.poses[0].position.x <= 382:
            self.direction.up = True
            self.direction.down = False
            self.direction.left = False
            self.direction.right = False
            self.direction.stop = False

        elif msg.poses[0].position.y >= 306 and msg.poses[0].position.x >= 216 and msg.poses[0].position.x <= 382:
            self.direction.down = True
            self.direction.up = False
            self.direction.left = False
            self.direction.right = False
            self.direction.stop = False

        elif msg.poses[0].position.y > 173 and msg.poses[0].position.y < 306 and msg.poses[0].position.x > 216 and msg.poses[0].position.x < 382:
            self.direction.stop = True
            self.direction.up = False
            self.direction.down = False
            self.direction.left = False
            self.direction.right = False

        else:
            self.direction.up = False
            self.direction.down = False
            self.direction.left = False
            self.direction.right = False
            self.direction.stop = False

    def timer_callback(self):
        self.publisher_.publish(self.direction)

def main(args=None):
    rclpy.init(args=args)

    aruco_to_directions = ArucoToDirections()

    rclpy.spin(aruco_to_directions)

    aruco_to_directions.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()