FROM ros:foxy

RUN apt update && apt install -y ros-${ROS_DISTRO}-rosbridge-server

RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

COPY Makefile Makefile
