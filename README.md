# 🧠 AI Budget Tracker

A full-stack intelligent budget tracking app that predicts expense categories using machine learning, with Django backend and React frontend.

---

## 🌟 Features

- User registration and login (Django Auth)
- Expense category prediction using ML (Scikit-learn)
- Clean and animated UI (React + CSS)
- SQLite database (lightweight and portable)
- Secure form handling
- Styled for responsiveness

---

## 🛠 Tech Stack

- **Backend:** Django, Python, SQLite
- **Frontend:** React.js, CSS
- **ML:** scikit-learn (Naive Bayes with TF-IDF)

---

## 📦 Setup Instructions

### 🔁 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ai-budget-tracker.git
cd ai-budget-tracker

---

## Commands

### Backend 

cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

### Frontend

cd frontend
npm install
npm start

### Create SuperUser

python manage.py createsuperuser

## To run run.sh once

chmod +x run.sh

## To run run.sh anytime

./run.sh