# AURORA | Next-Gen Real-Time Chat Experience

AURORA is a high-performance, ultra-premium real-time chat platform built using Python (FastAPI) and a modern Glassmorphism frontend. It features an animated mesh-gradient UI, secure room management, and instantaneous message delivery via WebSockets.


## 🎨 Features
- **Cinematic UI**: Vibrant, animated mesh backgrounds with multi-layered glassmorphism.
- **Real-Time Synergy**: Zero-latency communication via WebSockets.
- **Matrix (Room) Management**: Group-based sectors for organized discussions.
- **Rich Media Support**: Live timestamps, bold/italic formatting, and link parsing.

---

## 🚀 The Easiest Way to Run (Windows)

1. **Install Dependencies** (Only needed once):
   - Open the folder, click the address bar at the top, type `cmd`, and press Enter.
   - Paste: `pip install -r requirements.txt`
   - Press Enter.

2. **Start the Chat**:
   - **Method A (Easiest)**: Just **double-click** the `launch_chat.bat` file in this folder.
   - **Method B (Manual)**: If the `.bat` file is missing or you are on Windows:
     - Open your terminal/CMD in this folder.
     - Type: `python -m uvicorn main:app --host 0.0.0.0 --port 8000`
     - Press **Enter**. (Access it at `http://localhost:8000`)

---

## 🌐 How to Chat with Friends (Anywhere in the World)

AURORA is pre-configured for global connectivity:

1.  **Using the Bat File**: Run `launch_chat.bat` and look for the window titled **"AURORA TUNNEL"**.
2.  **Manual Tunneling**: 
    - If you are using the manual startup (Method B), open a **second** terminal.
    - Type: `ssh -R 80:localhost:8000 serveo.net` and press Enter.
3.  **Get the Link**: In the tunnel window, look for the line starting with `https://...` (e.g., `https://random.serveousercontent.com`).
4.  **Share**: Send that link to your friends in any city!

---

## 📝 Usage Guide
1. **Login**: Enter your Name and a **Sector** (Room Name).
2. **Chat**: Type in the box and hit Enter.
3. **Format**: Use the bold/italic icons next to the input box.
4. **Rooms**: Both people must join the **EXACT** same Sector name to see each other.

---

## 🏮 Troubleshooting (502 Error)
If your friend sees a "502 Bad Gateway" or "Page not working":
- Wait 5 seconds and refresh the page.
- Ensure the black terminal windows are still open on your computer.
- Click **"Advanced"** -> **"Proceed"** if the browser shows a security warning.

---

## 🔒 Security & Performance
- **XSS Prevention**: Messages are sanitized for safety.
- **FastAPI Backend**: Optimized for high concurrency and speed.
- **Automatic Cleanup**: Graceful handling of user disconnections.
