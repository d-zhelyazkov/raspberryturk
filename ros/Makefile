
run_ros:
	docker build -t ros:dev .
	docker run -it --rm --network=host ros:dev

launch_bridge:
	ros2 launch rosbridge_server rosbridge_websocket_launch.xml &

subscribe:
	ros2 topic echo /move_ack &
	ros2 topic echo /changed_cells &
	ros2 topic echo /next_move &
	ros2 topic echo /error &

push_move_ack:
	ros2 topic pub /move_ack std_msgs/Empty -1

