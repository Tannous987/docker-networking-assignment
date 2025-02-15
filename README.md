# Docker Networking & Volume Management Assignment

## Overview

This project demonstrates container networking and volume management using Docker Compose. It consists of a **Producer** that generates log data and a **Consumer** that retrieves and stores the logs persistently.

## Technologies Used
- Docker
- Docker Compose
- Flask (for Producer)
- Requests (for Consumer)

## Project Structure

```
/docker-networking-assignment
│-- /producer
│   │-- app.py         # Flask server generating random logs
│   │-- Dockerfile     # Instructions for building the Producer container
│   │-- requirements.txt # Dependencies for Flask app
│-- /consumer
│   │-- consumer.py    # Python script fetching logs from Producer
│   │-- Dockerfile     # Instructions for building the Consumer container
│   │-- requirements.txt # Dependencies for Consumer
│-- docker-compose.yml # Defines and orchestrates the multi-container setup
│-- README.md          # Project documentation
```

## Project Components

### 1. **Producer (Flask API)**

- Runs a Flask server that serves random log data.
- Used by the Consumer to fetch logs.

#### **Producer Dockerfile Explanation**
- Uses `python:3.8-alpine` as the base image.
- Copies the application files into the container.
- Installs required dependencies via `requirements.txt`.
- Exposes port `5000` and runs the Flask app.

### 2. **Consumer (Python Script)**

- Periodically fetches data from the Producer.
- Writes logs to a shared volume to persist across container restarts.

#### **Consumer Dockerfile Explanation**
- Uses `python:3.8-alpine` as the base image.
- Copies the application files into the container.
- Installs required dependencies via `requirements.txt`.
- Runs the Python script continuously to fetch and store logs.

### 3. **Docker Compose**

- Defines and runs multi-container Docker applications.
- Connects the Producer and Consumer via a Docker network.
- Mounts a volume to persist logs.

#### **Docker Compose Explanation**

The `docker-compose.yml` file sets up the following:

- **Network: `app-network`**
  - A bridge network allowing Producer and Consumer to communicate using service names.

- **Volume: `logs`**
  - Used by the Consumer to store log data persistently in `/data`.

- **Producer Service**
  - Built from `./producer/Dockerfile`.
  - Connected to `app-network`.
  - Exposes port `5000` for API access.

- **Consumer Service**
  - Built from `./consumer/Dockerfile`.
  - Connected to `app-network`.
  - Mounts the `logs` volume at `/data`.
  - Depends on the Producer service.

## How to Run
### Prerequisites
- Docker installed (`docker --version`)
- Docker Compose installed (`docker-compose --version`)

### Configure Docker Without `sudo` (Optional)
By default, Docker commands require `sudo`. To run Docker without `sudo`, add your user to the Docker group:

1. Add your user to the Docker group:
   ```bash
   sudo usermod -aG docker $USER
   ```
   (Replace `$USER` with your actual username if needed.)

2. Restart your system or log out and back in:
   ```bash
   sudo reboot
   ```

3. Verify your user is in the Docker group:
   ```bash
   groups
   ```

### Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Tannous987/docker-networking-assignment.git
   cd docker-networking-assignment
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
   - --build flag build the images for the services defined in the docker-compose.yml file, if the images already exist you can omit this flag unless you changed anything.
   - The Producer will generate random logs.
   - The Consumer will retrieve logs and store them.

3. Stop the containers when done:
   ```bash
   docker-compose down
   ```

### Verifying Persistent Logs
Even after stopping the containers, logs are stored in the Docker volume. To check the last 10 lines of the log file, run:
   ```bash
   sudo tail /var/lib/docker/volumes/docker-networking-assignment_logs/_data/logs.txt
   ```
   -replace tail with cat to see the whole file.

This ensures data persistence across container restarts.

## Finally To Remove Everything
Including containers, volumes, networks, images, and orphaned containers, you can run:
   ```bash
   docker-compose down --volumes --rmi all --remove-orphans
   ```

### Manually Building and Running the Containers (this approach is optional using docker-compose is simpler and recommended but using this approach you will have more control)
If you want to build and run without `docker-compose`:

#### **Build the images**
If needed, you can manually build the Docker images:
   ```bash
   docker build -t manually-built-producer-image ./producer
   docker build -t manually-built-consumer-image ./consumer
   ```

#### **Create a bridge network**
```bash
docker network create manually-created-network
```
- If no driver is specified the default one will be a bridge driver

#### **Run the producer container from the manually-built-producer-image**
```bash
docker run -d --name producer --network manually-created-network -p 5000:5000 manually-built-producer-image
```
- docker run: Starts a new container.
- -d: Runs the container in the background.
- --name producer: Names the container producer.
- --network manually-created-network: Connects the container to the manually-created-network.
- -p 5000:5000: Maps port 5000 of the host to port 5000 in the container.
- manually-built-producer-image: Specifies the Docker image used to create the container.

#### **Run the consumer container from the manually-built-consumer-image**
```bash
docker run -d --name consumer --network manually-created-network -v docker-networking-assignment_logs:/data manually-built-consumer-image
```
- docker run: Starts a new container.
- -d: Runs the container in the background.
- --name consumer: Names the container consumer.
- -network manually-created-network: Connects the container to the manually-created-network.
- -v docker-networking-assignment_logs:/data: Mounts the docker-networking-assignment_logs volume from the host to the /data directory inside the container. 
- This allows persistent data storage.
- manually-built-consumer-image: Specifies the Docker image used to create the container.

Now, the system is running without `docker-compose`! 
#### **Check the logs of 2 containers**
```bash
docker logs producer
docker logs consumer
```

#### **Stop the 2 containers**
```bash
docker stop producer consumer
```

### Verifying Persistent Logs
Even after stopping the containers, logs are stored in the Docker volume. To check the last 10 lines of the log file, run:
   ```bash
   sudo tail /var/lib/docker/volumes/docker-networking-assignment_logs/_data/logs.txt
   ```
   -replace tail with cat to see the whole file.

This ensures data persistence across container restarts.

### Finally Remove everything manually created
Including containers(make sure they are stopped before removing them), volumes, networks, images, you can run:
```bash
docker rm producer consumer
docker volume rm docker-networking-assignment_logs
docker network rm manually-created-network
docker rmi manually-built-producer-image manually-built-consumer-image
```







