import os

# Projektets namn
project_name = "Quake1_Docker_Server"

# Mappar att skapa
folders = [
    "id1",          # Här ska Quake 1 spelfiler (pak0.pak, pak1.pak) läggas
]

# Filer och deras innehåll
files = {
    "docker-compose.yml": 
        "version: '3'\n\n"
        "services:\n"
        "  quake1:\n"
        "    image: gazliddon/qs\n"
        "    container_name: quake1_server\n"
        "    ports:\n"
        "      - '27510:27510/udp'\n"
        "      - '27511:27511/tcp'\n"
        "    volumes:\n"
        "      - ./id1:/id1\n"
        "    restart: unless-stopped\n",

    "README.md":
        "# Quake 1 Docker Server\n\n"
        "## Setup\n\n"
        "1. Kopiera din legala id1-mapp från Quake 1 (Steam/GOG) till projektets root:\n\n"
        "   Quake1_Docker_Server/id1/\n\n"
        "2. Starta servern med Docker Compose:\n\n"
        "   docker-compose up -d\n\n"
        "3. Servern lyssnar på UDP 27510 (spel) och TCP 27511 (RCON, valfritt).\n\n"
        "---\n\n"
        "## Tips\n\n"
        "- Lämna id1-mappen ur GitHub (upphovsrätt).\n"
        "- Alla i gruppen kan klona repot och lägga in sina egna id1-filer.\n"
        "- Docker-compose.yml och scripts kan pushas som vanligt.\n",

    ".gitignore":
        "# Ignore Quake 1 game files\n"
        "id1/\n\n"
        "# Optional Docker artifacts\n"
        "*.log\n"
        "*.pid\n"
        "*.sock\n",

    "id1/README.txt": "Place your Quake 1 pak0.pak, pak1.pak, and other id1 files here. Do not push these to GitHub.\n"
}

# Skapa projektmappen
os.makedirs(project_name, exist_ok=True)

# Skapa mappar
for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

# Skapa filer
for filepath, content in files.items():
    full_path = os.path.join(project_name, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print(f"Projektet '{project_name}' är skapat! Lägg dina id1-filer i {project_name}/id1 och öppna projektet i VS Code.")