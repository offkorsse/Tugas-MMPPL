from flask import Blueprint, render_template, session

progress_bp = Blueprint("progress", __name__)

# Nama modul sesuai urutan index (id 1-6)
NAMA_MODUL = {
    "1": "Dasar Python",
    "2": "Variabel",
    "3": "Tipe Data",
    "4": "Fungsi",
    "5": "Operator",
    "6": "Pernyataan IF",
}

@progress_bp.route("/")
def lihat():
    progres_raw = session.get("progres", {})

    # Bangun data lengkap untuk semua modul
    semua_modul = []
    total_skor = 0
    jumlah_selesai = 0

    for key, nama in NAMA_MODUL.items():
        data = progres_raw.get(key)
        if data:
            semua_modul.append({
                "nama": nama,
                "skor": data["skor"],
                "selesai": data["selesai"],
                "tanggal": data["tanggal"],
                "status": "selesai" if data["selesai"] else "sedang",
            })
            total_skor += data["skor"]
            if data["selesai"]:
                jumlah_selesai += 1
        else:
            semua_modul.append({
                "nama": nama,
                "skor": None,
                "selesai": False,
                "tanggal": "-",
                "status": "belum",
            })

    jumlah_dikerjakan = len(progres_raw)
    rata_skor = round(total_skor / jumlah_dikerjakan) if jumlah_dikerjakan > 0 else 0
    persen_total = round((jumlah_selesai / len(NAMA_MODUL)) * 100)

    return render_template(
        "progress/progress.html",
        semua_modul=semua_modul,
        jumlah_selesai=jumlah_selesai,
        rata_skor=rata_skor,
        persen_total=persen_total,
    )
