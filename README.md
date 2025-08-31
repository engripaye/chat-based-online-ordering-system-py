---
# 💬 Chat-Based Online Ordering System

<img width="1536" height="1024" alt="Architecture of Chat Ordering System" src="https://github.com/user-attachments/assets/7bd4a321-6f60-4105-bb1a-6f8c4fdf10fc" />

A **Flask-powered backend application** for managing **chat-driven online orders**, user authentication, and order persistence. The system provides **RESTful APIs** consumed by a simple web frontend and stores all order data in a **MySQL database**.

---

## 🚀 Features

* 💬 **Chat-based ordering** – users can place and manage orders via a chat interface
* 🔑 **Authentication system** – secure login and registration
* 📦 **Order Management** – create, update, and track orders in real time
* 🗄️ **MySQL database integration** – persistent storage of users and orders
* ⚡ **REST APIs** – endpoints to support frontend and external integrations

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Authentication:** Flask-Login / JWT
* **Frontend:** Simple web client consuming REST APIs
* **Deployment:** Docker (optional)

---

## 📂 Project Structure

```
chat-ordering-system/
│── app/
│   ├── __init__.py          # App initialization
│   ├── models.py            # Database models (User, Order, Message)
│   ├── routes.py            # Flask routes (APIs)
│   ├── services.py          # Business logic
│   ├── auth.py              # Authentication handling
│   └── config.py            # Configurations (DB, secret keys)
│
│── migrations/              # Database migrations
│── tests/                   # Unit & integration tests
│── requirements.txt         # Python dependencies
│── Dockerfile               # Docker setup
│── README.md
```

---

## ⚡ Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/chat-ordering-system.git
cd chat-ordering-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Update `app/config.py` with your MySQL credentials:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/chat_ordering_db"
SECRET_KEY = "your-secret-key"
```

### 5️⃣ Initialize Database

```bash
flask db init
flask db migrate
flask db upgrade
```

### 6️⃣ Run Application

```bash
flask run
```

App runs at 👉 `http://127.0.0.1:5000`

---

## 📡 API Endpoints

### 🔹 Authentication

* `POST /api/register` → Register new user
* `POST /api/login` → User login

### 🔹 Orders

* `POST /api/orders` → Create new order
* `GET /api/orders` → Get all orders
* `GET /api/orders/<id>` → Get order by ID
* `PUT /api/orders/<id>` → Update order status
* `DELETE /api/orders/<id>` → Cancel order

### 🔹 Chat Messages

* `POST /api/messages` → Send a message
* `GET /api/messages/<order_id>` → Fetch messages for an order

---

## 🧪 Testing

Run unit tests:

```bash
pytest
```

---

## 🚀 Deployment with Docker

Build and run using Docker:

```bash
docker build -t chat-ordering-system .
docker run -d -p 5000:5000 chat-ordering-system
```

---

## 🚀 Future Improvements

* [ ] Add chatbot integration (Dialogflow / Rasa)
* [ ] Implement push notifications for order updates
* [ ] Add role-based access (admin, user)
* [ ] Integrate payment gateway

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📜 License

MIT License © 2025 \[Engr. Ipaye Babatunde]

---

⚡ Do you want me to also **generate a clean architecture diagram (Flask API → MySQL → Web Frontend → Chat workflow)** image so this README looks more visually appealing?
