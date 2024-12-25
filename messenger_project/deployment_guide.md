Deployment Guide
================

1. **Install Docker and Docker Compose:**
   - Verify Docker installation: `docker --version`
   - Verify Docker Compose installation: `docker-compose --version`

2. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd messenger_project
   ```

3. **Build and Start Services:**
   ```bash
   docker-compose up --build
   ```
   This command builds and starts all services in Docker containers.

4. **Check Running Containers:**
   ```bash
   docker ps
   ```
   Ensure all services are running properly.

5. **Access Services:**
   - **AuthService:** http://localhost:5000
   - **MessageService:** http://localhost:5001
   - **MediaService:** http://localhost:5002
   - **NotificationService:** http://localhost:5003
   - **Consul UI:** http://localhost:8500
   - **Load Balancer (HAProxy):** http://localhost:80

6. **Database Access:**
   - Connect using pgAdmin, DBeaver, or another database client.
   - **Host:** localhost
   - **Port:** 5432
   - **User:** user
   - **Password:** password
   - **Database:** messenger_db

7. **Stop Services:**
   ```bash
   docker-compose down
   ```
   Stops and removes all running containers.

8. **View Logs for Debugging:**
   ```bash
   docker-compose logs -f
   ```
   Monitors logs for debugging and error detection.

9. **Consul Configuration and Checks:**
   - Register services in Consul using HTTP API:
     ```bash
     curl --request PUT --data '{"Name": "authservice", "Address": "authservice", "Port": 5000}' http://localhost:8500/v1/agent/service/register
     ```
   - Verify service registration in Consul UI.

10. **Testing APIs:**
    - Use **Postman** or **curl** to test API endpoints for each service.
    - Example test for AuthService registration:
      ```bash
      curl --request POST \
      --url http://localhost:5000/register \
      --header 'Content-Type: application/json' \
      --data '{"username": "testuser", "email": "testuser@example.com", "password": "testpass"}'
      ```
    - Example test for MediaService file upload:
      ```bash
      curl --request POST \
      --url http://localhost:5002/upload \
      --form 'file=@/path/to/your/file.txt'
      ```

11. **Scaling Services (Optional):**
    - Modify `docker-compose.override.yml` to define replicas.
      Example for MessageService:
      ```yaml
      services:
        messageservice:
          deploy:
            replicas: 3
      ```
    - Apply scaling:
      ```bash
      docker-compose up --scale messageservice=3
      ```

12. **Monitoring Health Status:**
    - Check health endpoints for each service:
      ```bash
      curl http://localhost:5000/health
      ```
    - Verify response:
      ```json
      {"status": "healthy"}
      ```

13. **HAProxy Configuration:**
    - HAProxy is configured as a load balancer and resolves services using Docker DNS.
    - Configuration file: `haproxy.cfg`
    - Example HAProxy logs can be monitored:
      ```bash
      docker logs <haproxy-container-id>
      ```

