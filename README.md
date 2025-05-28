# ROS1-Turtlebot-Control-Usiing-Teleop-Keys


````markdown
# 🐢 TurtleBot Teleop - ROS 1 Keyboard Controller

A simple Python script to control a TurtleBot in ROS 1 using your keyboard (WASD-style teleoperation).

## 📦 Requirements

- ROS 1 (Noetic, Melodic, etc.)
- A TurtleBot (simulated or real)
- Python (usually comes with ROS)
- `geometry_msgs` (included with ROS)

## 🚀 Installation

Clone this repository into your ROS workspace:

```bash
cd ~/catkin_ws/src
git clone https://github.com/your-username/turtlebot_teleop.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
````

Make the script executable:

```bash
chmod +x ~/catkin_ws/src/turtlebot_teleop/turtlebot_teleop.py
```

## 🎮 Usage

Make sure your TurtleBot (or simulation) is running.

Then launch the teleop node:

```bash
rosrun turtlebot_teleop turtlebot_teleop.py
```

## 🧭 Controls

* `W`: Move forward
* `S`: Move backward
* `A`: Turn left
* `D`: Turn right
* `X`: Stop
* `Ctrl + C`: Exit

