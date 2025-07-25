
# 🤖 Chatbot PoC using FastAPI & React.js

This is a Proof of Concept (PoC) chatbot application using a combination of FastAPI (Python backend) and React.js (frontend), with the Hugging Face `DialoGPT-small` model for conversational AI.

---

## 📌 Features

- Natural language chatbot using `microsoft/DialoGPT-small`
- Built-in CORS support for frontend-backend communication
- Clean and minimal React UI
- Scroll to bottom on new messages
- Enter key support for quick messaging
- REST API endpoint with JSON support

---

## 📁 Project Structure

```
chatbot-poc/
├── backend/
│   └── main.py              # FastAPI backend with DialoGPT
├── frontend/
│   └── src/
│       ├── App.js           # React UI logic
│       ├── App.css          # Chat styling
├── README.md                # Project documentation
```

---

## 🛠️ Technologies Used

| Layer      | Technology       |
|------------|------------------|
| Frontend   | React.js, Axios  |
| Backend    | FastAPI, Pydantic, Uvicorn |
| AI Model   | Hugging Face `DialoGPT-small` |
| ML Framework | PyTorch        |

---

## 🔧 Backend Setup – FastAPI

### 1. Navigate to Backend Folder

### 2. Start React Frontend

```bash
npm start
```

Frontend will be served at: [http://localhost:3000](http://localhost:3000)

---

## 🔗 API Endpoint

| Method | URL     | Description                        |
|--------|---------|------------------------------------|
| POST   | `/chat` | Sends message, returns bot reply   |

### ✅ Example Request

```json
{
  "message": "Hello there!"
}
```

### ✅ Example Response

```json
{
  "reply": "Hi! How can I assist you today?"
}
```

---

## 🧠 Notes

- This PoC uses a global session. For multi-user environments, use unique session IDs or persistent storage.
- You can switch the model (`DialoGPT`) with more advanced HuggingFace conversational models.
- Ideal for demo, test, and learning purposes.

---

## 🔮 Future Improvements

- Add user authentication and multi-session support
- Integrate a database for storing chat history
- Add avatars, timestamps, and UI enhancements
- Dockerize the app for deployment

---

## 🧪 Testing

Access the FastAPI Swagger UI for manual testing at:

```
http://localhost:8000/docs
```

---

## 📜 License

MIT License — Free to use, modify, and distribute.

---

## 👨‍💻 Author

Built by [Lalit Sharlawar]  
GitHub: [https://github.com/SharlawarL/chat-bote](https://github.com/SharlawarL/chat-bote)
