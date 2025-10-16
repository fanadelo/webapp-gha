# ======================
# BASE IMAGE
# ======================
FROM python:3.12-slim

# =======================
# KATALOG ROBOCZY
# =======================
WORKDIR /app

# =======================
# INSTALACJA ZALEŻNOŚCI
# =======================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# =======================
# KOPIOWANIE PLIKÓW APLIKACJI
# =======================
COPY . .

# =======================
# URUCHOMIENIE APLIKACJI
# =======================
CMD ["python", "app/web.py"]