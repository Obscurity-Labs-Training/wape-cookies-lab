# wape-cookies-lab

This project demonstrates how to set and retrieve a basic cookie using Flask, without additional security settings. The project is packaged with Docker for easy setup and execution.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cookie-demo.git
   cd cookie-demo
   ```

2. **Build the Docker image**:
   ```bash
   docker-compose build
   ```

3. **Run the Docker container**:
   ```bash
   docker-compose up
   ```

4. **Test the Application**:
   - Go to `http://localhost:5000/set_cookie` to set a cookie.
   - Go to `http://localhost:5000/get_cookie` to retrieve the cookie.

5. **Stop the Application**:
   - Run `docker-compose down` to stop the container.

Enjoy the lab!