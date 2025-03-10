# Recipe API

## Description

This project is a Recipe API built using Django REST Framework. It allows users to manage recipes, tags, and ingredients. The API is designed to be fully containerized using Docker, making it easy to deploy and scale.

## Features

*   **User Authentication:** Secure user registration and authentication using Django's built-in authentication system and REST framework's token authentication.
*   **Recipe Management:** Create, read, update, and delete recipes.
*   **Tag and Ingredient Management:** Organize recipes using tags and ingredients.
*   **Image Uploads:** Upload images for recipes.
*   **API Documentation:** Comprehensive API documentation using drf-spectacular.
*   **Dockerized Deployment:** Easy deployment using Docker and Docker Compose.

## Technologies Used

*   **Django:** A high-level Python web framework.
*   **Django REST Framework:** A powerful and flexible toolkit for building Web APIs.
*   **PostgreSQL:** A robust and reliable open-source relational database.
*   **drf-spectacular:** An auto-schema generation tool for Django REST Framework.
*   **Docker:** A platform for developing, shipping, and running applications in containers.
*   **Nginx:** A high-performance web server and reverse proxy.
*   **uWSGI:** A fast WSGI server implementation, alternative to Gunicorn.
*   **AWS:** Cloud platform for deployment.

## Project Structure

```
recipe-app-api/
├── app/                      # Django project directory
│   ├── app/                  # Core Django settings and URLs
│   ├── core/                 # Core application logic (models, admin, etc.)
│   ├── recipe/               # Recipe application logic (serializers, views, etc.)
│   ├── user/                 # User application logic (serializers, views, etc.)
│   ├── manage.py             # Django management script
│   └── .flake8               # Linting checking tool configuration
├── proxy/                    # Nginx proxy configuration
│   ├── Dockerfile            # Dockerfile for the Nginx proxy
│   ├── default.conf.tpl      # Nginx configuration template
│   ├── uwsgi_params          # uWSGI parameters for Nginx
│   └── run.sh                # Script to start Nginx with environment variables
├── scripts/                  # Deployment scripts
│   └── run.sh                # Script to run migrations and start uWSGI
├── .github/                 # Github workflows
│   └── workflows/
│       └── checks.yml        # Github actions workflow file
├── .dockerignore             # Specifies intentionally untracked files that Docker should ignore
├── .gitignore                # Specifies intentionally untracked files that Git should ignore
├── Dockerfile                # Dockerfile for the Django application
├── docker-compose.yml        # Docker Compose file for local development
├── docker-compose-deploy.yml # Docker Compose file for deployment
├── .env                      # Environment variables (not committed to repository)
├── .env.sample               # Sample environment variables
├── requirements.txt          # Python dependencies
├── requirements.dev.txt      # Python development dependencies
└── README.md                 # Project README
```

## Getting Started

### Prerequisites

*   Docker
*   Docker Compose

### Local Development

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Zahkklm/recipe-app-api
    cd recipe-app-api
    ```

2.  **Create a `.env` file:**

    Copy the contents of `.env.sample` to a new file named `.env` and modify the variables as needed. Change the configurations according to your project.

    ```bash
    cp .env.sample .env
    ```

3.  **Build and run the Docker containers:**

    ```bash
    docker compose up --build
    ```

4.  **Access the application:**

    Open your web browser and navigate to `http://localhost:8000`.

### Deployment to AWS

1.  **Set up AWS resources:**

    *   Create an EC2 instance.
    *   Install Docker and Docker Compose on the EC2 instance.
    *   Configure security groups to allow traffic on port 80.

2.  **Configure environment variables:**

    Set the environment variables in your AWS environment (e.g., using AWS Systems Manager Parameter Store or EC2 instance environment variables).  Ensure the variables match those used in [docker-compose-deploy.yml](docker-compose-deploy.yml).

3.  **Copy the project files to the EC2 instance:**

    Use `scp` or a similar tool to copy the project files to your EC2 instance.

4.  **Build and deploy the application:**

    ```bash
    docker compose -f docker-compose-deploy.yml up --build
    ```

5.  **Access the application:**

    Open your web browser and navigate to the public IP address or domain name of your EC2 instance.

## API Endpoints

The API documentation is available at `/api/docs/` when the application is running.  This is configured in [app/app/urls.py](app/app/urls.py).