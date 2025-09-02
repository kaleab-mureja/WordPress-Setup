# Self-Contained WordPress & FastAPI Development Environment

This is a complete, self-contained development environment that includes a WordPress instance, a MySQL database, and a FastAPI application, all running in Docker containers.

---

## 🚀 Getting Started

Ensure you have Docker and Docker Compose installed on your machine.

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd [your-repo-name]
    ```

2.  **Start the containers:**
    This command will build the FastAPI container and start all services in the background.
    ```bash
    docker-compose up -d
    ```

---

## 🌐 Accessing the Services

Once the containers are up, you can access the WordPress site at the following URL. The FastAPI service is for internal use and testing.

* **WordPress:** [http://localhost:8000](http://localhost:8000)

---

## 🔑 Default Credentials

The default credentials for the database are stored in the `.env` file.

* **Database Name:** `wordpress_db`
* **Database User:** `wp_user`
* **Database Password:** `wp_password`

---

## 🧪 Running Tests

This environment includes a robust test suite to validate your application. The tests are defined in `docker-compose.test.yml` and use custom Docker images built from `Dockerfile` and `Dockerfile.test-runner`.

### WordPress Plugin Test

This command runs the `run_tests.py` script to test your custom WordPress plugin's functionality.

```bash
docker-compose -f docker-compose.yml -f docker-compose.test.yml run --rm test_runner
