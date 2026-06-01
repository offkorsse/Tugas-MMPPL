from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # hashed
    role = db.Column(db.String(20), default="pengguna")   # pengguna | admin | instruktur
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    progres = db.relationship("Progres", backref="user", lazy=True)

class Modul(db.Model):
    __tablename__ = "modul"
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text)
    index_urutan = db.Column(db.Integer, nullable=False)

    pelajaran = db.relationship("Pelajaran", backref="modul", lazy=True)
    kuis = db.relationship("Kuis", backref="modul", lazy=True)

class Pelajaran(db.Model):
    __tablename__ = "pelajaran"
    id = db.Column(db.Integer, primary_key=True)
    id_modul = db.Column(db.Integer, db.ForeignKey("modul.id"), nullable=False)
    judul = db.Column(db.String(100), nullable=False)
    konten = db.Column(db.Text, nullable=False)
    contoh_kode = db.Column(db.Text)

class Kuis(db.Model):
    __tablename__ = "kuis"
    id = db.Column(db.Integer, primary_key=True)
    id_pelajaran = db.Column(db.Integer, db.ForeignKey("pelajaran.id"))
    pertanyaan = db.Column(db.Text, nullable=False)
    pilihan = db.Column(db.JSON, nullable=False)  # list of strings
    kunci_jawaban = db.Column(db.String(1), nullable=False)  # "A" | "B" | "C" | "D"

class Progres(db.Model):
    __tablename__ = "progres"
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    id_modul = db.Column(db.Integer, db.ForeignKey("modul.id"), nullable=False)
    modul_selesai = db.Column(db.Boolean, default=False)
    nilai = db.Column(db.Integer, default=0)
    tanggal_update = db.Column(db.DateTime, default=datetime.utcnow)

class Sandbox(db.Model):
    __tablename__ = "sandbox"
    id = db.Column(db.Integer, primary_key=True)
    id_sesi = db.Column(db.String(64), nullable=False)
    bahasa = db.Column(db.String(20), default="python3")
    timeout = db.Column(db.Integer, default=10)

class Statistik(db.Model):
    __tablename__ = "statistik"
    id = db.Column(db.Integer, primary_key=True)
    id_admin = db.Column(db.Integer, db.ForeignKey("users.id"))
    total_modul = db.Column(db.Integer, default=0)
    rata_rata_skor = db.Column(db.Float, default=0.0)
