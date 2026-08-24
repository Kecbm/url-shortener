# URL Shortener 🚀

Practical **System Design** project to build a URL shortener that gradually evolves to support from 1 up to 1,000,000+ users.

## 📈 Architecture Evolution

The system grows in 3 main phases:

1. **[Phase 1 (MVP - up to 1k users)](./1_mvp/):** Basic API + Relational Database. Focus on the Base62 algorithm and database structure.
2. **[Phase 2 (10k to 100k users)](./2_caching/):** Addition of a Load Balancer, Multiple API Instances, and Cache (Redis).
3. **[Phase 3 (1M+ users)](./3_scale/):** Database Read Replicas, Distributed ID Service, and Rate Limiter.

## 🛠️ Tech Stack

* **Backend:** Python (FastAPI and Django)
* **Main Database:** SQLite, PostgreSQL
* **Cache & Proxy:** Redis, Nginx
* **Infrastructure:** Docker & Docker Compose

## 🗺️ Development Roadmap

### 🟢 Phase 1: MVP (Up to 1,000 users)
```bash
# Create the environment
python -m venv venv

# Active the environment
source venv/bin/activate

# Run the server
fastapi dev main.py

# Init db
python database.py

# Execute the function
python base62.py
```

### 🟡 Phase 2: The First Bottleneck (10k to 100k users)
- [ ] **Task 1: SLO Metrics & Middleware (1h):** Implement FastAPI middleware to log request latency, establishing the baseline to measure our P95 (<400ms) and P99 (<150ms) targets.
- [ ] **Task 2: Dependencies & Env Vars (1h):** Update `requirements.txt` (add `psycopg2-binary`, `redis`, `python-dotenv`, and an HTTP load testing tool like `locust`) and setup the `.env` file.
- [ ] **Task 3: PostgreSQL Migration (1h):** Replace `sqlite3` with `psycopg2` in `main.py`, explicitly configuring connection timeouts to ensure fast failures and maintain system availability.
- [ ] **Task 4: Resilient Redis Caching (1h):** Connect to Redis for the `GET` route to handle the 99% read traffic, ensuring a graceful fallback to the DB if the cache server goes down.
- [ ] **Task 5: API Dockerfile (1h):** Create a `Dockerfile` at the root of the project to package the Python code and FastAPI into a standardized image.
- [ ] **Task 6: Docker Compose Infrastructure (1h):** Create a `docker-compose.yml` file to spin up `postgres`, `redis`, and configure 2 simultaneous replicas of the FastAPI application.
- [ ] **Task 7: Nginx Load Balancer (1h):** Create an `nginx.conf` file to distribute traffic across the API replicas, adding the Nginx service to Docker Compose.
- [ ] **Task 8: Load Testing & SLO Verification (1h):** Use Locust to simulate concurrent user traffic (high RPS), verifying if the system sustains the load while meeting the defined latency SLOs.
...
- [ ] Desenho da arquitetura no Scalidraw, seguindo o padrão da imagem do mvp, focando nas rotas e insert e select separados na parte do db

### 🔴 Phase 3: Massive Scale (1M+ users)
- [ ] **Task 1: Redis Rate Limiter (1h):** Implement a Token Bucket algorithm middleware using Redis to limit the number of `POST /shorten` requests per IP, preventing abuse and DDoS attacks.
- [ ] **Task 2: Distributed ID Generator (1h):** Replace the PostgreSQL `AUTOINCREMENT` with a highly available ID generation strategy (e.g., a Redis-backed Ticket Server or Snowflake algorithm) to remove the write bottleneck.
- [ ] **Task 3: PostgreSQL Replication (Infra) (1h):** Update the `docker-compose.yml` to deploy a PostgreSQL Master-Slave architecture, separating write nodes from read nodes.
- [ ] **Task 4: Read/Write Split Routing (1h):** Refactor the API database logic to route all `INSERT` operations to the Master DB and all `SELECT` operations to the Read Replica DB.
- [ ] **Task 5: Replication Lag Mitigation (1h):** Implement a fallback mechanism (Eventual Consistency handling) where if a freshly created link is not yet found in the Read Replica, the API temporarily checks the cache or Master DB.
- [ ] **Task 6: Stress Testing & Tuning (1h):** Run intensive load tests using Locust to simulate massive traffic spikes, verifying the rate limiter's effectiveness and ensuring the Read Replicas maintain the P99 < 150ms SLO.
...
- [ ] Desenho da arquitetura no Scalidraw, seguindo o padrão da imagem do mvp, focando nas rotas e insert e select separados na parte do db

### 🏗️ Architectural Evolution and Trade-offs

**Phase 1: MVP and Validation (Up to 1k users)**
The project's architecture was intentionally designed to balance delivery speed and product validation. In this initial stage, we prioritized simplicity and local consistency using SQLite. Our focus was on correctly structuring the shortening algorithm (Base62) and the redirection logic, without adding premature infrastructure complexity.

![MVP data flow diagram](assets/mvp.jpeg)

- TODO: Vídeo about use the MVP

**Phase 2: High Availability and SLOs (10k to 100k users)**
To support the first major traffic leap and respect our latency SLOs (P99 < 150ms for redirects), the infrastructure evolved into a distributed environment. We migrated to PostgreSQL to ensure safe concurrency, introduced Redis as a resilient caching layer to absorb the 99% read traffic, and adopted Nginx as a Load Balancer to orchestrate multiple Docker-containerized API instances.

**Phase 3: Global Scale (1M+ users)**
Facing massive traffic, we embraced eventual consistency to protect the system's integrity. We implemented database read replicas (Read/Write Split) to distribute the load, adopted a distributed ID generator to remove the primary database bottleneck, and shielded the API with a Redis-based Rate Limiter to prevent abuse, ensuring the application's continuous resilience.

---

## 👤 Author

<div align="center">
  Project developed by <a href="https://kecbm.vercel.app/">Klecianny Melo</a> 👩🏾‍💻 
</div>

</br>

If you liked this project, give it a ⭐ and feel free to reach out!
