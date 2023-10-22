# docker-python-opengl
<p>Docker image to develop OpenGL apps with python.</p>
<p>The image provides a virtual framebuffer (xvfb), a minimalistic window manager (jwm) and a VNC server (x11vnc), so you can develop opengl apps entirely within the container with no external dependencies.</p>
<p>You only need a VNC client to display the container desktop.</p>

# Run container

```
docker compose up
```
Now, you can connect your VNC client to localhost:5900 to display the container's desktop.
# Opengl Development
<p>Your host folder './code' is mounted on the container's folder './app/code'. You can create .py files there and run them within the container.</p>
<p>You can also use Visual Studio Code extension "Dev containers" to attach vscode to the container and develop from there as if you were coding on the host.</p>
<p>I encourage you to install the vscode extension "Python" so that you can debug your code.</p>
<p>Make sure you create .py files from the host -not from the container-, because the container is running with "root" user, so the files you create from the container will belong to "root" user instead of your current user.</p>
# Shutting down the container

```
docker compose down
```
