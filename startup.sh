#!/bin/bash

# start X11 + Window Manager + VNC server

export DISPLAY=:99
Xvfb ${DISPLAY} -ac -listen tcp -screen 0 800x600x16 &
sleep 3
jwm -display ${DISPLAY} &
sleep 3
x11vnc -display ${DISPLAY}.0 -forever -shared -nopw
