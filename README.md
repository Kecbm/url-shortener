# URL Shortener 🚀

Practical **System Design** project to build a URL shortener that gradually evolves to support from 1 up to 1,000,000+ users.

## 📈 Architecture Evolution

The system grows in 3 main phases:

1. **[Phase 1 (MVP - up to 1k users)](./1_mvp/):** Basic API + Relational Database. Focus on the Base62 algorithm and database structure.
2. **[Phase 2 (10k to 100k users)](./2_caching/):** Addition of a Load Balancer, Multiple API Instances, and Cache (Redis).
3. **[Phase 3 (1M+ users)](./3_scale/):** Database Read Replicas, Distributed ID Service, and Rate Limiter.

## 🛠️ Tech Stack

* **Backend:** Python (FastAPI or Django)
* **Main Database:** PostgreSQL
* **Cache & Proxy:** Redis, Nginx
* **Infrastructure:** Docker & Docker Compose

## 🗺️ Development Roadmap

### 🟢 Phase 1: MVP (Up to 1,000 users)
- [ ] **Task 1: Setup (1h):** Create a virtual environment (`venv`), install the web framework, and run a "Hello World" route.
- [ ] **Task 2: Database (1h):** Spin up PostgreSQL via Docker, connect the application, and create the main table (`id`, `original_url`, `short_hash`).
- [ ] **Task 3: Algorithm (1h):** Create a function that converts an integer (database ID) to Base62.
- [ ] **Task 4: Creation Route (1h):** Create a `POST` endpoint (receives URL, saves to the DB, generates Base62, and returns the short link).
- [ ] **Task 5: Redirect Route (1h):** Create a `GET` endpoint (receives hash, searches for the URL in the DB, and performs a 301/302 redirect).
- [ ] **Task 6: Validation (1h):** Validate the received URL, prevent duplicate links, and test the API.

### 🟡 Phase 2: The First Bottleneck (10k to 100k users)
- [ ] Dockerize the application.
- [ ] Add Nginx as a Load Balancer.
- [ ] Integrate Redis for URL caching.

### 🔴 Phase 3: Massive Scale (1M+ users)
- [ ] Set up Database Read Replicas.
- [ ] Implement a Distributed ID Generation Service.
- [ ] Implement Rate Limiting.

---

## 👤 Author

<div align="center">
  Project developed by <a href="https://kecbm.vercel.app/">Klecianny Melo</a> 👩🏾‍💻 
</div>

</br>

If you liked this project, give it a ⭐ and feel free to reach out!
