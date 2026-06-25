# Geo Alert Bot

A consent-based geolocation notification system built with **Python (Flask)**, **JavaScript**, and **Telegram Bot API**.  
The application requests location permission from the user through the browser Geolocation API, sends the coordinates to a Flask backend, and delivers real-time alerts to Telegram with map links and reverse-geocoded location details.

---

## Features

- Capture user location through browser **Geolocation API**
- Send real-time location alerts to **Telegram**
- Reverse geocode latitude/longitude into a readable address
- Display Google Maps / OpenStreetMap links
- Lightweight frontend with simple permission flow
- Deployable using **Netlify (frontend)** + **Render (backend)**

---

## Tech Stack

- **Frontend:** HTML, JavaScript
- **Backend:** Python, Flask
- **Bot Integration:** Telegram Bot API
- **Geocoding:** OpenStreetMap / Nominatim
- **Deployment:** Netlify, Render

---

## Project Structure

```bash
geo-alert-bot/
│── app.py
│── index.html
│── requirements.txt
│── .gitignore
│── README.md




## How It Works
- User opens the hosted webpage
- Browser requests location permission
- If permission is granted, latitude/longitude are captured
- Frontend sends the location data to the Flask backend
- Backend formats the data and sends an alert to Telegram
- Reverse geocoding converts coordinates into a readable address



## Setup

1. Clone the repository
        git clone https://github.com/your-username/geo-alert-bot.git
        cd geo-alert-bot
2. Create and activate a virtual environment
        python3 -m venv venv
            source venv/bin/activate
3. Install dependencies
        pip install -r requirements.txt
4. Set environment variables
        export BOT_TOKEN="your_telegram_bot_token"
        export CHAT_ID="your_telegram_chat_id"
5. Run the Flask app
        python app.py