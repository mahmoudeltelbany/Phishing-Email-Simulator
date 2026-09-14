import os
from functools import wraps

from flask import Flask, jsonify, request, render_template, session


app = Flask(__name__)

# In production, use an environment variable.
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "dev-only-change-me"
)


# --------------------------------------------------------------------------
# Demo database
# --------------------------------------------------------------------------

USERS = {
    "demo@mystory.com": {
        "name": "Demo Writer",
        "password": "password123",
    }
}


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def login_required(view):
    """Reject the request unless a user is signed in."""

    @wraps(view)
    def wrapped(*args, **kwargs):

        if "user_email" not in session:
            return jsonify({
                "error": "Not signed in"
            }), 401

        return view(*args, **kwargs)

    return wrapped


# --------------------------------------------------------------------------
# Request Logger
# --------------------------------------------------------------------------

@app.before_request
def log_request():

    print("\n" + "=" * 60)
    print("INCOMING REQUEST")
    print("=" * 60)

    print("Method:", request.method)
    print("URL:", request.url)
    print("Path:", request.path)

    print("\nHeaders:")
    for key, value in request.headers:
        print(f"  {key}: {value}")

    # JSON body
    json_data = request.get_json(silent=True)

    if json_data:
        print("\nJSON Body:")
        print(json_data)

    # Form data
    if request.form:
        print("\nForm Data:")
        print(request.form.to_dict())

    print("=" * 60)


# --------------------------------------------------------------------------
# Page routes
# --------------------------------------------------------------------------

@app.route("/")
def login_page():

    return render_template("login.html")


# --------------------------------------------------------------------------
# API routes
# --------------------------------------------------------------------------

@app.route("/api/login", methods=["POST"])
def api_login():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Expected JSON body"
        }), 400

    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not email or not password:
        return jsonify({
            "error": "Email and password are required"
        }), 400

    user = USERS.get(email)

    if not user or user["password"] != password:
        return jsonify({
            "error": "Incorrect email or password"
        }), 401

    session["user_email"] = email

    if data.get("remember"):
        session.permanent = True

    return jsonify({
        "message": f"Welcome back, {user['name']}!",
        "email": email
    }), 200


@app.route("/api/logout", methods=["POST"])
def api_logout():

    session.pop("user_email", None)

    return jsonify({
        "message": "Signed out"
    }), 200


@app.route("/api/data", methods=["GET"])
@login_required
def get_data():

    email = session["user_email"]

    return jsonify({
        "message": "Hello, World!",
        "signed_in_as": email
    })


@app.route("/api/whoami", methods=["GET"])
def whoami():

    email = session.get("user_email")

    return jsonify({
        "signed_in": email is not None,
        "email": email
    })


# --------------------------------------------------------------------------
# Error handlers
# --------------------------------------------------------------------------

@app.errorhandler(404)
def not_found(_e):

    return jsonify({
        "error": "Not found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(_e):

    return jsonify({
        "error": "Method not allowed"
    }), 405


# --------------------------------------------------------------------------
# Run application
# --------------------------------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5050,
        debug=True
    )