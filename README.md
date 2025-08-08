# Phishing Campaign Simulator

## ⚠️ Ethical Warning
This project was created for educational purposes to understand the mechanics of phishing attacks and to build defensive awareness. **Never use this tool against individuals without their explicit, written consent.** Unauthorized phishing is illegal and unethical.

---

## Project Objective
This project is a fully functional phishing campaign simulator built with Python and Flask. The application serves a realistic-looking login page, tracks user interaction (form submissions) without storing sensitive credentials, and redirects users to an educational page. The goal is to demonstrate an understanding of social engineering tactics and secure application development.
<img width="1920" height="1080" alt="Screenshot 2025-08-08 140705" src="https://github.com/user-attachments/assets/cc989af9-ce8b-4aa1-ba19-09ed00dfe167" />

---

## Technology Stack
* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
<img width="1920" height="1080" alt="Screenshot 2025-08-08 140655" src="https://github.com/user-attachments/assets/c6647ff8-8a77-4651-8b20-3064809166a0" />

---

## How it Works
1.  An administrator would send a simulated phishing email to a target user containing a link to this web application.
2.  The user clicks the link and is presented with a fake login page (`login.html`).
3.  When the user submits their credentials, the application's backend (`app.py`) logs that a submission occurred (<img width="1920" height="1080" alt="Screenshot 2025-08-08 140640" src="https://github.com/user-attachments/assets/3db94f0c-d04d-4843-a459-1ed0cd27200c" />
without saving the password) and immediately redirects the user.
4.  The user is sent to an educational page (`/caught`) that explains that this was a test and provides tips on how to spot real phishing attacks.
<img width="1920" height="1080" alt="Screenshot 2025-08-08 140751" src="https://github.com/user-attachments/assets/82da2a03-e777-48d3-9f1b-c850048f4ef7" />

---

## Setup and Usage
1.  Clone the repository and `cd` into the project directory.
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Install the required packages: `pip install -r requirements.txt`
4.  Run the application: `flask run`
5.  Access the fake login page at `http://127.0.0.1:5000`.
