# Robotic-arm chess: vision and ROS 2 integration

A 2023 side project at Ocado Technology: a robotic arm playing chess against a person. This fork adds board vision, move detection and ROS 2 integration to [Joey Meyer's Raspberry Turk](https://github.com/joeymeyer/raspberryturk) (original README below).

My changes:

- **Board vision** – better calibration of the perspective transform that turns a camera frame into a top-down, square-aligned board image (`raspberryturk/embedded/vision/`, `raspberryturk/core/vision/`), plus raw-image capture for calibration (`capture_raw_imgs.py`)
- **Move detection** – each board image is compared with the previous one, and the two squares that changed most give the move, which is then checked against the game state (python-chess)
- **ROS 2 integration** (`ros/`) – after the arm confirms a move on `/move_ack`, the node detects the opponent's move, updates the game, asks Stockfish for the reply, and publishes `/changed_cells`, `/next_move` and `/error` over rosbridge. The node runs in Docker.

Python · OpenCV · ROS 2 (roslibpy, rosbridge) · python-chess · Stockfish · Docker

---

<p align="center">
  <img src="http://www.raspberryturk.com/assets/img/logo.svg" width="120px" />
</p>

# Raspberry Turk

The Raspberry Turk is a robot that can play chess—it's entirely open source, based on Raspberry Pi, and inspired by the 18th century chess playing machine, the Mechanical Turk. The project incorporates aspects of computer vision, data science, machine learning, robotics, 3D printing, and—of course—chess.

## Website

A website describing the robot and how it was made can be found [here](http://www.raspberryturk.com).

## Creator

[Joey Meyer](http://www.raspberryturk.com/aboutme.html)

## License

Raspberry Turk is available under the MIT license. See the LICENSE file for more info.
