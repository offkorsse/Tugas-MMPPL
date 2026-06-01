from flask import Blueprint, render_template, request, redirect, url_for, flash

instruktur_bp = Blueprint("instruktur", __name__)

@instruktur_bp.route("/")
def portal():
    # TODO: fetch modul milik instruktur, aktivitas user
    return render_template("instruktur/portal.html")

@instruktur_bp.route("/modul/baru", methods=["GET", "POST"])
def tambah_modul():
    if request.method == "POST":
        # TODO: save new modul to DB, set status pending validasi
        flash("Modul berhasil diunggah, menunggu validasi.", "info")
        return redirect(url_for("instruktur.portal"))
    return render_template("instruktur/tambah_modul.html")

@instruktur_bp.route("/modul/<int:modul_id>/edit", methods=["GET", "POST"])
def edit_modul(modul_id):
    if request.method == "POST":
        # TODO: update modul in DB
        flash("Modul berhasil diperbarui.", "success")
        return redirect(url_for("instruktur.portal"))
    return render_template("instruktur/edit_modul.html", modul_id=modul_id)
