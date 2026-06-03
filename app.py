from flask import Flask, render_template
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.profile_routes import profile_bp
from routes.post_routes import post_bp
from routes.request_routes import request_bp
from routes.stats_routes import stats_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(post_bp)
app.register_blueprint(request_bp)
app.register_blueprint(stats_bp)


@app.route("/")
def home():
    return render_template("signup.html")


@app.route("/login-page")
def login_page():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/create-profile-page")
def create_profile_page():
    return render_template("create_profile.html")


@app.route("/create-post-page")
def create_post_page():
    return render_template("create_post.html")


@app.route("/creators")
def creators():
    return render_template("creators.html")


@app.route("/send-request-page")
def send_request_page():
    return render_template("send_request.html")


@app.route("/my-requests")
def my_requests():
    return render_template("my_requests.html")


if __name__ == "__main__":
    app.run(debug=True)