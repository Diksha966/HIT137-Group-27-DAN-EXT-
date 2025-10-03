# HIT137 Assignment 3 – GUI with Hugging Face Models

## 📖 Project Overview
This project is a simple Python application with a **Tkinter GUI** that demonstrates the use of machine learning models from Hugging Face. It applies **Object-Oriented Programming (OOP) concepts** such as encapsulation, inheritance, polymorphism, and decorators.

The system allows users to:
- Enter **text** and classify its sentiment (Positive/Negative).
- Choose an **image** and classify it into categories (e.g., cat breeds).

---

## ✨ Features
- **Text Classification** using a DistilBERT model.
- **Image Classification** using a Vision Transformer model.
- **Tkinter GUI** with:
  - Radio buttons for selecting text or image input.
  - Input box for text, file chooser for images.
  - Scrollable output box to display results.
  - Section explaining OOP concepts used.
- **Reusable design** with modular files:
  - `model_base.py` → abstract base class.
  - `model_text.py` → text model handler.
  - `model_image.py` → image model handler.
  - `decorators.py` → simple logger and timer.
  - `main.py` → GUI runner.

---

## ▶️ How to Run
1. Clone this repo:
   ```bash
   git clone <your-github-repo-url>
   cd hit137-gui
   git clone <your-github-repo-url>
   cd hit137-gui
