FROM python:3.10-slim

RUN apt update && apt -y install freeglut3-dev x11vnc xvfb jwm &&\
    pip install PyOpenGL notebook &&\
    mkdir -p /app/code
COPY startup.sh /app/startup.sh
RUN chmod -R 777 /app
ENV DISPLAY=:99
WORKDIR /app/code

ENTRYPOINT ["/app/startup.sh"]
