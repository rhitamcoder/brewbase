# ☕ Brewbase

**A dynamic, database-backed directory of remote-work-friendly cafes — built with Flask and SQLite.**

Brewbase is a full-stack web app that lets you browse, add, and remove cafes based on what remote workers actually care about: wifi, power sockets, seating, whether you can take a call, and how much a coffee costs. Unlike a static listing, every cafe lives in a real database — so the site updates instantly as entries are added or removed, with no rebuild or redeploy required.

---

## ✨ Features

- 📋 **Browse cafes** in a responsive card grid, each showing photo, location, amenities, seat count, and coffee price
- ➕ **Add a new cafe** through a clean, collapsible form — no page reload needed to reveal it
- 🗑️ **Delete a cafe** directly from its card
- 🏷️ **Amenity tags** (Wifi, Power Sockets, Toilet, Calls OK) rendered dynamically based on what's stored in the database
- 🔗 **Direct Google Maps links** for every cafe location
- 📱 Fully responsive layout, from desktop down to mobile
- 🎨 Custom warm, coffee-shop-inspired theme (Lora + Inter fonts, CSS custom properties for easy re-theming)

---

## 🛠️ Tech Stack

- **Python 3** + **Flask** — routing and server-side logic
- **SQLite** — lightweight relational database for storing cafe entries
- **Jinja2** — server-side templating (`render_template`)
- **HTML5 / CSS3** — custom-styled frontend, no CSS framework
- **Google Fonts** — Lora (headings) & Inter (body)

---

## 📁 Project Structure

```
brewbase/
├── app.py                 # Flask application (routes + DB logic)
├── cafes.db                # SQLite database
├── templates/
│   └── index.html          # Main page template (Jinja2)
├── static/
│   └── style.css           # Stylesheet
└── README.md
```

---

## 🗄️ Database Schema

The app uses a single `cafe` table:

| Column           | Type         | Notes                          |
|------------------|--------------|---------------------------------|
| `id`             | INTEGER      | Primary key                     |
| `name`           | VARCHAR(250) | Required, unique                |
| `map_url`        | VARCHAR(500) | Required — Google Maps link     |
| `img_url`        | VARCHAR(500) | Required — cafe photo URL       |
| `location`       | VARCHAR(250) | Required                        |
| `has_sockets`    | BOOLEAN      | Required                        |
| `has_toilet`     | BOOLEAN      | Required                        |
| `has_wifi`       | BOOLEAN      | Required                        |
| `can_take_calls` | BOOLEAN      | Required                        |
| `seats`          | VARCHAR(250) | Optional (e.g. `"20-30"`)       |
| `coffee_price`   | VARCHAR(250) | Optional (e.g. `"£2.50"`)       |

---

## 🔀 Routes

| Route                | Method | Description                              |
|-----------------------|--------|-------------------------------------------|
| `/`                   | GET    | Displays all cafes from the database      |
| `/add`                | POST   | Adds a new cafe from the submitted form   |
| `/delete/<int:cafe_id>` | POST | Deletes the cafe with the given ID        |

---

## ▶️ Getting Started

### Prerequisites
- Python 3
- Flask

```
pip install flask
```

### Running the App

```
git clone https://github.com/rhitamcoder/brewbase.git
```
```
cd brewbase
```
```
python app.py
```

The app will start in debug mode at `http://127.0.0.1:5000/` — open it in your browser to start browsing and adding cafes.

> **Note:** The repo ships with a `cafes.db` file pre-populated with sample cafe entries, so the app works out of the box. Feel free to clear it out and start fresh with your own data.

---

## 🖼️ Adding a Cafe

Click **"+ Add a new cafe"** to reveal the form, fill in the cafe's name, location, map link, photo URL, seating, and coffee price, tick whichever amenities apply, and submit — the new entry appears in the grid immediately, no page reload required.

---

## 🔗 Related Project

A static, database-free version of this same idea also exists — **[Cafeb](https://github.com/rhitamcoder/cafeb)** — built as a plain HTML/CSS site for comparison.

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
