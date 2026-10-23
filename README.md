# Simple LMS - Django & PostgreSQL with Docker

Aplikasi Simple Learning Management System (LMS) berbasis Django dan PostgreSQL yang dijalankan menggunakan lingkungan terisolasi Docker Compose, serta dilengkapi pgAdmin untuk pengelolaan database.

---

## 🛠️ Prasyarat (Prerequisites)

Sebelum menjalankan proyek ini, pastikan sistem kamu sudah terpasang:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Engine & Compose)
- Git

---

## 📦 Paket & Dependency yang Di-install

Seluruh dependency Python yang dibutuhkan didefinisikan dalam file `requirements.txt`:

- **`Django>=5.2,<5.3`**: Framework utama untuk membangun aplikasi Simple LMS.
- **`psycopg[binary]>=3.2,<4`**: Adapter/driver PostgreSQL untuk Python/Django.

---

## ⚙️ Variabel Lingkungan (.env)

Proyek ini menggunakan file `.env` untuk menyimpan kredensial dan variabel lingkungan. Buat file `.env` di root proyek dengan menyalin dari `.env.example`:

```env
POSTGRES_DB=simple_lms
POSTGRES_USER=lms_user
POSTGRES_PASSWORD=lms_password

DB_NAME=simple_lms
DB_USER=lms_user
DB_PASSWORD=lms_password
DB_HOST=db
DB_PORT=5432

DJANGO_SECRET_KEY=dev-only-replace-this-with-a-long-random-key

PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=pgadmin_password
```

> ⚠️ Ganti seluruh nilai di atas dengan kredensial yang aman jika dipakai di luar lingkungan pengembangan.

---

## 🚀 Langkah-Langkah Menjalankan Proyek

### 1. Build dan Jalankan Container

Buka terminal/PowerShell di direktori proyek dan jalankan:

```powershell
docker compose up -d --build
```

### 2. Jalankan Database Migration

Terapkan migrasi struktur tabel ke database PostgreSQL:

```powershell
docker compose run --rm app python manage.py makemigrations accounts courses
docker compose run --rm app python manage.py migrate
```

### 3. Buat Akun Superuser Django

Buat akun administrator untuk mengakses Django Admin:

```powershell
docker compose run --rm app python manage.py createsuperuser
```

---

## 🌐 Akses Layanan & Endpoints

| Layanan | URL / Endpoint | Keterangan |
| --- | --- | --- |
| **Django Admin** | `http://localhost:8000/admin/` | Panel admin aplikasi LMS |
| **pgAdmin GUI** | `http://localhost:5050` | Panel manajemen database PostgreSQL |
| **PostgreSQL DB** | `db:5432` | Host koneksi internal di jaringan Docker (`lms_net`) |

### 🔑 Pengaturan Koneksi pgAdmin ke PostgreSQL

Saat menambahkan server baru di pgAdmin, gunakan:

- **Host name/address:** `db`
- **Port:** `5432`
- **Maintenance database:** `simple_lms` (sesuai `POSTGRES_DB`)
- **Username:** `lms_user` (sesuai `POSTGRES_USER`)
- **Password:** `lms_password` (sesuai `POSTGRES_PASSWORD`)

---

## 🧪 Pengujian & Data Latihan

### Menjalankan Unit Test

Untuk memverifikasi logika model dan batasan sistem:

```powershell
docker compose exec app python manage.py test courses
```

### Memuat Data Contoh (Fixture)

Jika ingin memuat data awal latihan:

```powershell
docker compose exec app python manage.py loaddata sample_data.json
```

### Ekspor Data Latihan ke Fixture

Jika ingin menyimpan data yang ada di database ke file JSON:

```powershell
docker compose exec app python manage.py dumpdata accounts.User courses --indent 2 --output sample_data.json
```