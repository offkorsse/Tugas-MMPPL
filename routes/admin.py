from flask import Blueprint, render_template

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
def panel():
    # TODO: fetch statistik, user list, modul list
    return render_template("admin/panel.html")

@admin_bp.route("/pengguna")
def kelola_pengguna():
    return render_template("admin/pengguna.html")

@admin_bp.route("/modul")
def kelola_modul():
    return render_template("admin/modul.html")
