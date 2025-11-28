# 🏥 Smart Healthcare Monitoring System  
### AI-Based Post-Surgery Home Monitoring | Wound Detection | Vitals Check | Risk Assessment

## 🚀 Overview
This project is a Smart Healthcare System designed to assist post-surgery patients.  
It integrates **AI + IoT + FastAPI + HTML/CSS/JS** to provide:

- AI Wound Classification  
- Vitals Abnormality Detection  
- Combined Risk Score Calculation  
- Doctor Dashboard  
- Analytics Dashboard  

---

## 🧠 Features

### 🔍 1. AI Wound Image Classification
- Uses **MobileNetV2 CNN Model**
- Predicts:
  - Healthy
  - Mild Infection
  - Severe Infection  
- Returns label + confidence

### ❤️ 2. Vitals Monitoring System
Detects abnormalities in:
- Heart Rate
- Temperature
- SpO2

Backend returns alerts:
- High Fever  
- Low Oxygen  
- Tachycardia  
- Normal  

### ⚠ 3. Full Risk Assessment Engine
- Takes wound image + vitals  
- Computes 0–1 Risk Score  
- Color-coded:
  - Green → Safe  
  - Yellow → Moderate  
  - Red → High Risk (requires attention)

### 👨‍⚕️ 4. Doctor Dashboard
- Shows patient list + risk level  
- Auto-updating  
- Professional UI

### 📊 5. Analytics Dashboard
- Visual charts (Chart.js)
- Wound case distribution  
- Infection severity stats  

---

## 🏗 Tech Stack

### 🧩 Frontend
- HTML  
- CSS  
- JavaScript  
- Chart.js  

### ⚙ Backend
- FastAPI  
- TensorFlow  
- Scikit-Learn  
- Uvicorn  

---

## 📁 Folder Structure

/backend
├── main.py
├── routes/
├── ml/
├── models/
├── requirements.txt

/frontend
├── index.html
├── wound.html
├── vitals.html
├── risk.html
├── dashboard.html
├── analytics.html
├── script.js
└── style.css


---

## ▶ Running Backend

```bash
cd backend
uvicorn main:app --reload


http://127.0.0.1:8000


index.html

Contributors : 
Gagan R 