from flask import Flask, render_template, request, jsonify
from pathlib import Path
import re
import math
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),
    static_folder=str(STATIC_DIR),
    static_url_path="/static"
)

app.config["JSON_AS_ASCII"] = False


# ---------------------------------------------------------
# ANA SAYFA
# ---------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------------------------
# SAĞLIK KONTROLÜ
# ---------------------------------------------------------

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "Doro Lojistik",
        "time": datetime.now().isoformat()
    })


# ---------------------------------------------------------
# TEKLİF HESAPLAMA / TALEP SİSTEMİ
# ---------------------------------------------------------

@app.route("/api/quote", methods=["POST"])
def quote():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Geçerli bir istek gönderilmedi."
        }), 400

    origin = clean_text(data.get("origin"))
    destination = clean_text(data.get("destination"))
    cargo = clean_text(data.get("cargo"))
    weight = clean_text(data.get("weight"))
    vehicle = clean_text(data.get("vehicle"))
    name = clean_text(data.get("name"))
    phone = clean_text(data.get("phone"))
    email = clean_text(data.get("email"))

    required_fields = {
        "origin": origin,
        "destination": destination,
        "cargo": cargo,
        "vehicle": vehicle,
        "name": name,
        "phone": phone
    }

    missing = [
        key for key, value in required_fields.items()
        if not value
    ]

    if missing:
        return jsonify({
            "success": False,
            "message": "Lütfen zorunlu alanların tamamını doldurun.",
            "missing": missing
        }), 400

    if len(phone) < 7:
        return jsonify({
            "success": False,
            "message": "Lütfen geçerli bir telefon numarası girin."
        }), 400

    if email and not valid_email(email):
        return jsonify({
            "success": False,
            "message": "Lütfen geçerli bir e-posta adresi girin."
        }), 400

    # -----------------------------------------------------
    # Burada GERÇEK fiyat uydurmuyoruz.
    #
    # Gerçek teklif için şirketin fiyatlandırma sistemi,
    # mesafe, yük tipi, araç, yakıt, geçiş ücretleri,
    # tarih vb. gerçek veriler gerekir.
    #
    # Şimdilik güvenli şekilde "talep alındı" sistemi
    # çalışıyor.
    # -----------------------------------------------------

    request_id = create_request_id(
        origin,
        destination,
        name
    )

    return jsonify({
        "success": True,
        "request_id": request_id,
        "message": "Teklif talebiniz başarıyla oluşturuldu.",
        "summary": {
            "origin": origin,
            "destination": destination,
            "cargo": cargo,
            "weight": weight or "Belirtilmedi",
            "vehicle": vehicle
        }
    })


# ---------------------------------------------------------
# YARDIMCI FONKSİYONLAR
# ---------------------------------------------------------

def clean_text(value, max_length=250):
    if value is None:
        return ""

    value = str(value).strip()

    # Gereksiz HTML benzeri içerikleri temizle
    value = re.sub(r"<[^>]*>", "", value)

    # Birden fazla boşluğu tek boşluğa indir
    value = re.sub(r"\s+", " ", value)

    return value[:max_length]


def valid_email(email):
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


def create_request_id(origin, destination, name):
    base = f"{origin}{destination}{name}"
    numeric = sum(ord(char) for char in base)

    # Basit, geçici talep numarası.
    # Gerçek sistemde database ID kullanılabilir.
    number = abs(numeric * 7919) % 1000000

    return f"DORO-{number:06d}"


# ---------------------------------------------------------
# HATA SAYFALARI
# ---------------------------------------------------------

@app.errorhandler(404)
def not_found(error):
    if request.path.startswith("/api/"):
        return jsonify({
            "success": False,
            "message": "API endpoint bulunamadı."
        }), 404

    return render_template("index.html"), 404


@app.errorhandler(500)
def server_error(error):
    if request.path.startswith("/api/"):
        return jsonify({
            "success": False,
            "message": "Sunucu tarafında beklenmeyen bir hata oluştu."
        }), 500

    return "Sunucu tarafında beklenmeyen bir hata oluştu.", 500


# ---------------------------------------------------------
# UYGULAMAYI ÇALIŞTIR
# ---------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("DORO LOJİSTİK WEB SUNUCUSU")
    print("=" * 60)
    print(f"Proje klasörü : {BASE_DIR}")
    print(f"Templates     : {TEMPLATE_DIR}")
    print(f"Static        : {STATIC_DIR}")
    print("=" * 60)
    print("Sunucu: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
