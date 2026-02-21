# AURORA | Next-Gen Real-Time Chat Experience

AURORA is a high-performance, ultra-premium real-time chat platform built using Python (FastAPI) and a modern Glassmorphism frontend. It features an animated mesh-gradient UI, secure room management and instantaneous message delivery via WebSockets.

## 🚀 Features
* Real-time communication using WebSockets
* Room-based chat system
* Username authentication with duplicate prevention
* Live timestamps for messages
* Sender identification for each message
* Basic text formatting (bold, italic, links)
* Automatic scroll to latest message
* Graceful handling of user disconnections
* Responsive modern UI design

## 🛠️ Technologies Used
* **Frontend:** HTML, CSS, JavaScript
* **Backend:** FastAPI (Python)
* **Protocol:** WebSockets

## 📂 Project Structure
```
Chat-Application/
│
├── main.py
├── requirements.txt
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```
## ▶️ How to Run Locally

1. Clone or download the project.
2. Install dependencies:
      pip install -r requirements.txt
3. Start the server:
      uvicorn main:app --reload
4. Open your browser and go to:
      http://localhost:8000
   
## 🌐 Live Demo
The project is deployed and accessible at:
[https://chat-application-1bz2.onrender.com](https://chat-application-1bz2.onrender.com)

## 🧪 Testing Instructions
1. Open the application in two browser windows (or one incognito window).
2. Enter different usernames.
3. Join the same room.
4. Send messages and verify real-time communication.

## 🔐 Security & Edge Case Handling
* Prevents duplicate usernames
* Prevents impersonation
* Handles user disconnect events
* Validates message inputs

## 📌 Assignment Compliance
This project fulfills the internship requirements by implementing:
   * Real-time chat using WebSockets
   * Room creation and joining
   * Username-based authentication
   * Timestamped messages
   * Responsive user interface







