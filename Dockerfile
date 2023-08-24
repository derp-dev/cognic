FROM ghcr.io/ai-dock/jupyter-pytorch:2.0.1-py3.10-cuda-11.8.0-base-22.04

LABEL Name=cognic Version=0.0.69

# Set the working directory in the container
WORKDIR /app
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
