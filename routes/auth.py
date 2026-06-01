from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Akun prototype hardcoded — ganti dengan DB query saat production
        AKUN = {
            "admin":      {"password": "admin123",      "role": "admin"},
            "instruktur": {"password": "instruktur123", "role": "instruktur"},
            "user":       {"password": "user123",       "role": "pengguna"},
        }

        akun = AKUN.get(username)
        if akun and akun["password"] == password:
            session["user"] = username
            session["role"] = akun["role"]
            # Arahkan ke halaman sesuai role
            if akun["role"] == "admin":
                return redirect(url_for("admin.panel"))
            elif akun["role"] == "instruktur":
                return redirect(url_for("instruktur.portal"))
            else:
                return redirect(url_for("modul.dashboard"))
        else:
            flash("Username atau password salah.", "danger")
    return render_template("auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # TODO: hash password, save to DB
        flash("Akun berhasil dibuat. Silakan login.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
