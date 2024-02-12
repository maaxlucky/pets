# pull the oficial base image
FROM python:3.12

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /app/

# exposes port 8000 for access from other apps
EXPOSE 8000

# what command to run after launching container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]