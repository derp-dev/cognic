FROM ghcr.io/chenhunghan/ialacol-cuda12:4d1fc25e74e8560a885c298827f010a2780980c3
# FROM ghcr.io/ai-dock/jupyter-pytorch:2.0.1-py3.10-cuda-11.8.0-base-22.04

LABEL Name=cognic Version=0.0.69

# Set the working directory
WORKDIR /app

# Copy any additional files or scripts required by your application
COPY . /app

# Set the entrypoint command to run your application
CMD [ "python", "app.py" ]

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code to the container
COPY . .

# Expose the desired ports
EXPOSE 8888 6006

# Set the ulimit options
CMD ["bash", "-c", "ulimit -l unlimited && ulimit -s 65536 && python /app/langsmith.py"]

# docker run -it --rm --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -v .:/app cognosis /bin/bash
# docker run -it --rm --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -v .:/app cognosis bash -c "ulimit -l unlimited && ulimit -s 65536 && python /app/app.py"
