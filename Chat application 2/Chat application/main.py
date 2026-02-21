from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
from datetime import datetime

app = FastAPI()

# Store active connections: {room_name: [list of websocket objects]}
rooms = {}
# Store usernames: {websocket_object: username}
usernames = {}
# Global set of active usernames to prevent duplicates
active_usernames = set()

@app.websocket("/ws/{room_name}/{username}")
async def websocket_endpoint(websocket: WebSocket, room_name: str, username: str):
    if username in active_usernames:
        await websocket.accept()
        await websocket.send_text(json.dumps({"type": "error", "message": "Username already taken"}))
        await websocket.close()
        return

    await websocket.accept()
    
    if room_name not in rooms:
        rooms[room_name] = []
    
    rooms[room_name].append(websocket)
    usernames[websocket] = username
    active_usernames.add(username)
    
    # Notify room about new user
    join_msg = {
        "type": "system",
        "sender": "System",
        "text": f"{username} has joined the room.",
        "timestamp": datetime.now().strftime("%H:%M")
    }
    await broadcast_to_room(room_name, join_msg)
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Add timestamp and sender
            message_data["sender"] = username
            message_data["timestamp"] = datetime.now().strftime("%H:%M")
            message_data["type"] = "user"
            
            await broadcast_to_room(room_name, message_data)
    except WebSocketDisconnect:
        rooms[room_name].remove(websocket)
        active_usernames.remove(username)
        del usernames[websocket]
        
        leave_msg = {
            "type": "system",
            "sender": "System",
            "text": f"{username} has left the room.",
            "timestamp": datetime.now().strftime("%H:%M")
        }
        await broadcast_to_room(room_name, leave_msg)

async def broadcast_to_room(room_name: str, message: dict):
    if room_name in rooms:
        for connection in rooms[room_name]:
            await connection.send_text(json.dumps(message))

@app.get("/", response_class=HTMLResponse)
async def get():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

app.mount("/static", StaticFiles(directory="static"), name="static")

