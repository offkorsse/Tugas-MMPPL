from flask import Blueprint, render_template, request, redirect, url_for, session

modul_bp = Blueprint("modul", __name__)

@modul_bp.route("/")
def dashboard():
    # TODO: fetch modul list + user progress from DB
    return render_template("modul/dashboard.html")

@modul_bp.route("/<int:modul_id>")
def detail(modul_id):
    # TODO: fetch modul detail + pelajaran list
    return render_template("modul/detail.html", modul_id=modul_id)

@modul_bp.route("/<int:modul_id>/pelajaran/<int:pelajaran_id>")
def pelajaran(modul_id, pelajaran_id):
    # TODO: fetch pelajaran content
    return render_template("modul/pelajaran.html", modul_id=modul_id, pelajaran_id=pelajaran_id)
