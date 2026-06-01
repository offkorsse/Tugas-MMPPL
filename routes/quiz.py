from flask import Blueprint, render_template, request, jsonify, session
from datetime import datetime

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route("/<int:modul_id>", methods=["GET"])
def tampil(modul_id):
    return render_template("quiz/quiz.html", modul_id=modul_id)

@quiz_bp.route("/<int:modul_id>/submit", methods=["POST"])
def submit(modul_id):
    data = request.get_json()
    benar = data.get("benar", 0)
    total = data.get("total", 1)
    skor = round((benar / total) * 100)

    if "progres" not in session:
        session["progres"] = {}

    key = str(modul_id)
    session["progres"][key] = {
        "modul_id": modul_id,
        "skor": skor,
        "benar": benar,
        "total": total,
        "selesai": skor >= 60,
        "tanggal": datetime.now().strftime("%d %b %Y")
    }
    session.modified = True

    return jsonify({"skor": skor, "benar": benar, "total": total})
