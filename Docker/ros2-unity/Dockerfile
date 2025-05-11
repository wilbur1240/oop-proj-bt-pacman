FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV ROS_DISTRO=humble

ENV SHELL=/bin/bash \
    USER=rsa \
    UID=1000

RUN adduser --disabled-password --gecos "Default user" --uid ${UID} ${USER}

ENV HOME=/home/${USER}
WORKDIR ${HOME}

RUN echo "root:root" | chpasswd && echo "${USER}:111111" | chpasswd

# Set up user permissions
RUN usermod -aG sudo ${USER}

# Basic setup tools
RUN apt update && apt install -y --no-install-recommends \
    locales curl cmake make git vim wget sudo lsb-release \
    build-essential net-tools apt-utils software-properties-common \
    dialog libffi-dev python3-dev python3-pip python3-setuptools \
    apt-transport-https libglew-dev python3-tk tree less \
    python3-ipdb

# Python packages
RUN pip3 install --upgrade pip setuptools==58.2.0 && \
    pip3 install \
        python_tsp \
        pypozyx \
        pytest \
        scipy \
        opencv-python \
        pytransform3d \
        pandas \
        pytest-profiling \
        scikit-learn \
        mypy \
        mkdocs \
        mkdocs-with-pdf \
        mkdocstrings \
        mkdocs-material \
        "mkdocstrings[python]" \
        networkx[all] \
        xdoctest

# Optional: mkdocs-mermaid2-plugin
RUN pip3 install mkdocs-mermaid2-plugin

# Source ROS 2 and build workspace
RUN /bin/bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash"

# Ensure ROS 2 gets sourced for bash
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ${HOME}/.bashrc

# Set default user
USER ${USER}
