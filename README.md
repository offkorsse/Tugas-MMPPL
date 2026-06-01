# Py-Learn — Prototype

Aplikasi pembelajaran Python berbasis website (Flask).

## Struktur Folder

```
py-learn/
├── app.py                  # Entry point Flask
├── models.py               # SQLAlchemy database models
├── requirements.txt
├── routes/
│   ├── auth.py             # Login, register, logout
│   ├── modul.py            # Dashboard & detail modul
│   ├── quiz.py             # Kuis & submit jawaban
│   ├── progress.py         # Progres pengguna
│   ├── admin.py            # Panel admin
│   └── instruktur.py       # Portal instruktur
├── templates/
│   ├── base.html           # Layout utama (navbar, flash)
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── modul/
│   │   ├── dashboard.html  # Daftar modul + progress
│   │   ├── detail.html     # Daftar pelajaran dalam modul
│   │   └── pelajaran.html  # Teori + sandbox editor
│   ├── quiz/
│   │   └── quiz.html       # Kuis pilihan ganda
│   ├── progress/
│   │   └── progress.html
│   ├── admin/
│   │   ├── panel.html
│   │   ├── pengguna.html
│   │   └── modul.html
│   └── instruktur/
│       ├── portal.html
│       ├── tambah_modul.html
│       └── edit_modul.html
└── static/
    ├── css/style.css
    ├── js/
    └── img/
```

## Cara Menjalankan

```bash
# 1. Buat virtual environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan development server
python app.py
```

Buka `http://localhost:5000` di browser.

## Stack Teknologi

| Layer    | Teknologi                          |
|----------|------------------------------------|
| Backend  | Python 3.11 + Flask                |
| Frontend | HTML5, CSS3, Bootstrap 5, Vanilla JS |
| Database | PostgreSQL + SQLAlchemy ORM        |
| Editor   | Ace Editor                         |
| Sandbox  | Pyodide (Python di WebAssembly)    |
| Versioning | Git + GitHub                     |
| Task Mgmt | Trello + GitHub Issues            |

## Modul yang Direncanakan

1. Dasar Python
2. Variabel
3. Tipe Data
4. Fungsi
5. Operator
6. Pernyataan IF
7. Perulangan (versi berikutnya)
8. List & Dictionary (versi berikutnya)

## Catatan Pengembangan

- Pendekatan: **Incremental + Iteratif**
- Integrasi: **Bottom-Up** (Autentikasi & DB → Konten → Sandbox → Kuis → Progress)
- Pengujian: **Black-Box Testing** + PyTest unit test
- Branch strategy: **Feature Branch Workflow**
