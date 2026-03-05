#Setup of the container
FROM python:3.11
COPY . .

WORKDIR /home/app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r /home/app/requirements.txt
COPY . .

RUN echo "Container for an IoT application built successfully"
ENV PYTHONPATH=/home/app