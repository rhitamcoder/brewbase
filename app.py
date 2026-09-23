from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_PATH = "cafes.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row #lets us access columns by name, e.g. row["name"]
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cafes = conn.execute("SELECT * FROM cafe").fetchall()
    conn.close()
    return render_template("index.html", cafes=cafes)

@app.route("/add", methods=["POST"])
def add_cafe():
    name = request.form.get("name")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location")
    seats = request.form.get("seats")
    coffee_price = request.form.get("coffee_price")

    # checkboxes only appear in form data if they were checked, so use "in request.form"
    has_sockets = 1 if "has_sockets" in request.form else 0
    has_toilet = 1 if "has_toilet" in request.form else 0
    has_wifi = 1 if "has_wifi" in request.form else 0
    can_take_calls = 1 if "can_take_calls" in request.form else 0

    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO cafe (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:cafe_id>", methods=["POST"])
def delete_cafe(cafe_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM cafe WHERE id = ?", (cafe_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

