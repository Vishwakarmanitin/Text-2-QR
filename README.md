# 📱 Text-2-QR Generator

A sleek, responsive, and modern web application built with **Flask** and **Bootstrap 5** that allows users to instantly convert text or URL links into high-quality, scannable QR codes.

---

## ✨ Features

- **Instant QR Generation**: Converts text or URLs to QR codes instantly using an in-memory byte stream.
- **Base64 Rendering**: QR codes are injected directly into the HTML markup without saving clutter files to the server.
- **Modern User Interface**: Features a beautiful glassmorphic card design with smooth hover animations and a premium gradient background.
- **Responsive Layout**: Completely mobile-friendly layout optimized for all screen sizes.

---

## 🚀 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, FontAwesome (Icons)
- **Core Library**: `qrcode` (with `pillow` for image formatting)

---

## 🛠️ Installation & Setup

Follow these quick steps to get the project running locally on your computer:

### 1. Clone the Repository
```bash
git clone https://github.com
cd Text-2-QR
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv .env
.env\Scripts\activate

# macOS/Linux
python3 -m venv .env
source .env/bin/activate
```

### 3. Install Dependencies
```bash
pip install Flask qrcode pillow
```

### 4. Run the Application
```bash
python app.py
```

Open your web browser and navigate to: **`http://127.0.0`**

---

## 📂 Project Structure

```text
├── app.py              # Main Flask application logic
├── templates/
│   └── index.html      # Frontend HTML/CSS/UI structure
└── README.md           # Project documentation
```

---

## 📝 License

This project is open-source and available under the MIT License.
