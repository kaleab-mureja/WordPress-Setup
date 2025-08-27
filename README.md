# Self-Contained WordPress & FastAPI Development Environment

This is a complete, self-contained development environment that includes a WordPress instance, a MySQL database, and a FastAPI application, all running in Docker containers.

## 🚀 Getting Started

Ensure you have Docker and Docker Compose installed on your machine.

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd [your-repo-name]
    ```

2.  **Start the containers:**
    This single command will build the FastAPI container and start all services in the background.
    ```bash
    docker-compose up -d
    ```

## 🌐 Accessing the Services

Once the containers are up, you can access the services at the following URLs:

* **WordPress:** [http://localhost:8000](http://localhost:8000)
    * The database is pre-configured, so you should be taken directly to the WordPress setup screen.

* **FastAPI:** [http://localhost:8001](http://localhost:8001)

## 🔑 Default Credentials

The default credentials for the database are stored in the `.env` file.

* **Database Name:** `wordpress_db`
* **Database User:** `wp_user`
* **Database Password:** `wp_password`

## 🧪 Running Tests

To validate the setup, you can run the test suite defined in `docker-compose.test.yml`. This command will perform a basic installation check for WordPress.

```bash
docker-compose -f docker-compose.yml -f docker-compose.test.yml run --rm test_runner
