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
- [x] **Task 1: Setup:** Create a virtual environment (`venv`), install FastAPI, and run a basic "Hello World".

```bash
# Create the environment
python -m venv venv

# Active the environment
source venv/bin/activate

# Run the server
fastapi dev main.py
```

- [x] **Task 2: Database:** Set up a local **SQLite** database and create the main table (`id`, `original_url`, `short_hash`).

```bash
# Init db
python database.py
```

- [x] **Task 3: Algorithm:** Create a standard Python function that converts an integer to Base62.

```bash
# Execute the function
python base62.py
```

- [x] **Task 4: Creation Route:** Create a `POST` endpoint that receives a URL, saves it to SQLite, generates the Base62 hash, and returns the short link.
- [ ] **Task 5: Redirect Route (1h):** Create a `GET` endpoint that receives the hash, queries SQLite, and performs a 301/302 redirect.
- [ ] **Task 6: Validation (1h):** Add basic string validation for the URL and logic to prevent saving duplicate links.

- [ ] **Task 7: Frontend (1h):** Validate the option of creating a frontend to group the three stages of the study project

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
