# matimil-ragnarok-server

Docker setup for the **MatiMil Ragnarok Online Server**.  
Includes the game server (rAthena), FluxCP web panel, and MySQL with initialization scripts.

---

## 📦 Contents

- `rathena/` – rAthena server code and configuration  
- `fluxcp/` – FluxCP web panel for account and server management  
- `mysql/db-init/` – MySQL database initialization scripts  
- `docker-compose.yml` – Docker Compose setup for all components  
- `.github/workflows/` – CI/CD workflows  

---

## ⚙️ Configuration

- **rAthena** → `rathena/conf/`  
- **FluxCP** → `fluxcp/`  
- **MySQL** → `mysql/db-init/`  
- **Docker Compose** → edit ports and environment variables in `docker-compose.yml`  

---

## 🛠 Development

- Submit changes via Pull Request  
- Automated checks run with GitHub Actions  