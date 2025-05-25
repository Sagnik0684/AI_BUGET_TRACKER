#!/bin/bash

echo "🌟 Starting Backend (Django)..."
cd backend
python manage.py runserver &
BACK_PID=$!

echo "🌈 Starting Frontend (React)..."
cd ../frontend
npm start &

# Trap to kill Django when script is stopped
trap "kill $BACK_PID" EXIT

# Waits so both run
wait