
# Quake 1 Docker Server

## Setup

1. Kopiera din legala id1-mapp från Quake 1 (Steam/GOG) till projektets root:

   Quake1_Docker_Server/id1/

2. Starta servern med Docker Compose:

   docker-compose up -d

3. Servern lyssnar på UDP 27510 (spel) och TCP 27511 (RCON, valfritt).

---

## Tips

- Lämna id1-mappen ur GitHub (upphovsrätt).
- Alla i gruppen kan klona repot och lägga in sina egna id1-filer.
- Docker-compose.yml och scripts kan pushas som vanligt.
