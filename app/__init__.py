from flask import Flask, render_template, redirect, url_for
from app.booking import bp as booking_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(booking_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/logout")
    def logout():
        return redirect(url_for("index"))

    return app
