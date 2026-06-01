from flask import Flask
from routes.auth import auth_bp
from routes.modul import modul_bp
from routes.quiz import quiz_bp
from routes.progress import progress_bp
from routes.admin import admin_bp
from routes.instruktur import instruktur_bp

app = Flask(__name__)
app.secret_key = "pylearn-secret-key"

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(modul_bp, url_prefix="/modul")
app.register_blueprint(quiz_bp, url_prefix="/quiz")
app.register_blueprint(progress_bp, url_prefix="/progress")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(instruktur_bp, url_prefix="/instruktur")

@app.route("/")
def index():
    from flask import redirect, url_for
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pylearn.db"
    app.run(debug=True)
