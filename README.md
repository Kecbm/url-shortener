# URL Shortener 🚀

Practical System Design project to build a URL shortener that gradually evolves to support from 1 up to 1,000,000+ users.

## 📈 Architecture Evolution

The system grows in 3 main phases:

* **Phase 1 (MVP - up to 1k users):** Basic API + Relational Database. Focus on the Base62 algorithm and database structure.
* **Phase 2 (10k to 100k users):** Addition of a Load Balancer, Multiple API Instances, and Cache (Redis).
* **Phase 3 (1M+ users):** Database Read Replicas, Distributed ID Service, and Rate Limiter.
