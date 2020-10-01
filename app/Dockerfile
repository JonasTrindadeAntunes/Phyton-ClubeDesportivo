FROM python:3.8-slim-buster

# ensures our console output looks familiar and is not buffered by Docker, which we don’t want
ENV PYTHONUNBUFFERED=1
# means Python wont try to write .pyc files which we also do not desire
ENV PYTHONDONTWRITEBYTECODE=1

# copy your project
COPY . /app
WORKDIR /app

# install pip requirements
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
