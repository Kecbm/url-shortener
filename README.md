# URL Shortener 🚀

Projeto prático de **System Design** para construir um encurtador de URLs que evolui gradativamente para suportar de 1 até 1.000.000+ de usuários.

## 📈 Evolução da Arquitetura

O sistema cresce em 3 fases principais:

1. **Fase 1 (MVP - até 1k usuários):** API Básica + Banco Relacional. Foco no algoritmo Base62 e estrutura do banco.
2. **Fase 2 (10k a 100k usuários):** Adição de Load Balancer, Múltiplas Instâncias da API e Cache (Redis).
3. **Fase 3 (1M+ usuários):** Read Replicas no Banco, Serviço Distribuído de IDs e Rate Limiter.
