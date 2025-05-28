#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# Movement bindings
move_bindings = {
    'w': (1, 0),
    's': (-1, 0),
    'a': (0, 1),
    'd': (0, -1),
    'x': (0, 0)
}

def get_key():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtlebot_teleop')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    speed = 0.2  # Linear speed (m/s)
    turn = 1.0   # Angular speed (rad/s)

    try:
        print("Use WASD keys to move the TurtleBot")
        print("Press X to stop")
        print("Press CTRL+C to quit")

        while not rospy.is_shutdown():
            key = get_key()
            if key in move_bindings:
                linear = move_bindings[key][0] * speed
                angular = move_bindings[key][1] * turn
                twist = Twist()
                twist.linear.x = linear
                twist.angular.z = angular
                pub.publish(twist)
            elif key == '\x03':  # Ctrl+C
                break

    except Exception as e:
        print(e)

    finally:
        # Stop the robot when exiting
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
