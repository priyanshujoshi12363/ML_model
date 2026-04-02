# 🚀 GigGuard AI — Smart Risk, Fraud & Payout Engine

GigGuard AI is an intelligent backend system designed for gig workers (delivery partners, drivers, etc.) that automates:

* ⚡ Risk detection
* 🛡️ Fraud detection
* 💰 Smart payout calculation
* 📦 Subscription-based protection plans

---

# 🧠 System Architecture

```
User Input
   ↓
INDRA (Risk Engine)
   ↓
KAVACH (Fraud Detection)
   ↓
Decision Layer
   ↓
DHAN (Payout Engine)
   ↓
Plan Cap (Basic / Standard / Premium)
   ↓
Final Response
```

---

# ⚙️ Features

## 🔥 1. INDRA — Risk Prediction

* Uses ML to calculate real-time risk score
* Based on weather, location, and environmental factors

## 🛡️ 2. KAVACH — Fraud Detection

* Detects suspicious claims using:

  * Speed
  * Claim frequency
  * GPS mismatch
  * Risk inconsistency

## 💰 3. DHAN — Payout Engine

* Predicts fair compensation using ML
* Applies plan-based payout limits

## 📦 4. Protection Plans

| Plan     | Cost | Coverage            | Max Payout |
| -------- | ---- | ------------------- | ---------- |
| Basic    | ₹34  | Rain only           | ₹600       |
| Standard | ₹58  | Rain + AQI + Curfew | ₹1200      |
| Premium  | ₹89  | All disruptions     | ₹2000      |

---

# 🧩 Tech Stack

### Backend

* FastAPI (Python)
* Node.js (User & Plan Management)

### ML Models

* LightGBM (Risk - INDRA)
* RandomForest (Fraud - KAVACH)
* RandomForest (Payout - DHAN)

### Database

* MongoDB Atlas

### Others

* Pydantic
* PyMongo
* dotenv

---

# 📁 Project Structure

```
app/
│
├── model/
│   ├── indra.py
│   ├── kavach.py
│   ├── dhan.py
│
├── service/
│   ├── driver_service.py
│   ├── feature_builder.py
│
├── pipeline/
│   └── pipeline.py
│
├── constants/
│   └── plans.py
│
└── main.py

ml/
├── train_indra.py
├── train_kavach.py
├── train_dhan.py
```

---

# 🚀 Installation & Setup

## 1️⃣ Clone Repo

```
git clone <your-repo-url>
cd gigguard
```

## 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

## 4️⃣ Setup Environment Variables

Create `.env` file:

```
MONGO_URL=your_mongodb_connection_string
```

---

# ▶️ Run Server

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 📮 API Usage

## 🔹 POST `/api/predict`

### Request Body:

```json
{
  "user_id": "driver_id_here",

  "rain": 80,
  "aqi": 300,
  "wind": 20,
  "visibility": 2,
  "humidity": 90,
  "temp": 32,
  "pressure": 1000,
  "hour": 14,
  "location_risk": 75,
  "curfew": 1,

  "speed": 40,
  "claims_last_4h": 0,
  "gps_distance": 50
}
```

---

### Response:

```json
{
  "success": true,
  "status": "Approved ✅",
  "plan": "standard",
  "indra": {...},
  "kavach": {...},
  "payout": {
    "final_payout": 1200
  }
}
```

---

# 🧠 How It Works

* INDRA calculates risk score
* KAVACH checks fraud
* If safe → DHAN calculates payout
* Plan caps the payout amount

---

# 🔒 Security

* Environment variables for secrets
* Input validation using Pydantic
* Fraud detection layer (KAVACH)

---

# 📈 Future Improvements

* 📊 Dashboard analytics
* 🤖 Plan upgrade recommendations
* 💳 Payment integration
* 📡 Real-time weather APIs

---

# 💣 Built For

* Gig Economy Platforms (Zomato, Swiggy, Uber)
* InsurTech Startups
* AI-based Risk Systems

---

# 👨‍💻 Author

**Priyanshu Joshi**

---

# ⭐ Final Note

This project demonstrates a **complete AI-driven backend system** combining:

* Machine Learning
* Fraud Detection
* Financial Logic
* Scalable Architecture

🚀 Ready for production & deployment
