# DevOps Lab 2 - Docker Multi-Container Application

This repository contains the code and report for DevOps Lab 2 at Pulchowk Campus. The lab demonstrates the setup and use of Docker on Ubuntu, including running containers, creating custom images, and deploying a multi-container application using Docker Compose.

## Project Structure

- **backend/** : Flask backend application with RESTful API endpoints.
- **docker-compose.yml** : Configuration for multi-container deployment (frontend, backend, database).
- **Dockerfile** : Custom image setup for the Flask backend.
- **report/** : LaTeX report documenting objectives, methodology, results, and discussion.
- **screenshots/** : Screenshots of Docker Compose, running containers, and other outputs.

## Features

- Multi-container application with **frontend**, **backend**, and **MySQL database**.
- Backend provides API endpoints to add and retrieve notes.
- Persistent database storage using Docker volumes.
- Networking between containers using Docker Compose service names.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dinesh-sirmal/Docker-file.git
cd Docker-file
