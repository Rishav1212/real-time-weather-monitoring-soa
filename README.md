
# 🌤️ Real-Time Weather Monitoring Application (SOA-Based)

This is a simple real-time weather monitoring application built using **Service-Oriented Architecture** and **Flask**. It fetches live weather data from the **OpenWeatherMap API** and displays it via a web interface.

---

## 🚀 How It Works

- The user enters a **city name**.
- A Flask web service sends a **GET request** to the OpenWeatherMap API.
- The API returns weather data in **JSON** format.
- The server parses the data and renders it in an interactive **Bootstrap-based UI**.

---

## 📁 Project Structure

```
weather-app/
├── app.py                   # Main Flask application
├── templates/
    └── weather.html         # HTML UI (Bootstrap styled)
```

---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- requests
- Bootstrap (via CDN)
- OpenWeatherMap API

---

## 🔧 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/real-time-weather-monitoring-soa.git
cd real-time-weather-monitoring-soa
```

2. **Install dependencies**
```bash
pip install flask requests
```

3. **Run the Flask app**
```bash
python app.py
```

4. **Open in browser**
```
http://localhost:5000/
```

---

## 🧪 Example Inputs and Outputs

### ✅ Valid City
**Input:** Kolkata  
**Output:** Displays temperature, humidity, wind speed, and weather condition.

### ❌ Invalid City
**Input:** asdfghj  
**Output:** `City not found or API error.`

---

## 📦 API Used
[OpenWeatherMap API](https://openweathermap.org/api) – free tier available for developers.

---

## 📌 Author

**Rishav Chakraborty**  
