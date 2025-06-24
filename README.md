# Late Show API

A RESTful API for managing guests, episodes, and appearances on the Late Show.

---

## 🚀 Setup Instructions

### 1. **Clone the repository**
```bash
git clone <your-github-repo-link>
cd late-show-api-challenge
```

### 2. **Install dependencies**
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary pipenv shell
```

### 3. **PostgreSQL Setup**
- Install PostgreSQL if not already installed.
- Create a database and user:
  ```bash
  sudo -u postgres psql
  CREATE USER your_username WITH PASSWORD 'your_password';
  CREATE DATABASE late_show_db OWNER your_username;
  \q
  ```

### 4. **Environment Variables**
`server/config.py` with your credentials.

```
DATABASE_URI=postgresql://your_username:your_password@localhost:5432/late_show_db
JWT_SECRET_KEY=your_jwt_secret
```
---

## 🏃 How to Run

### 1. **Migrate the Database**
```bash
export FLASK_APP=server.app:app
flask db upgrade
```

### 2. **Seed the Database**
```bash
python -m server.seed
```

### 3. **Run the Server**
```bash
flask run
```

---

## 🔐 Auth Flow

1. **Register:**  
   `POST /register`  
   Body:
   ```json
   { "username": "yourname", "password": "yourpass" }
   ```

2. **Login:**  
   `POST /login`  
   Body:
   ```json
   { "username": "yourname", "password": "yourpass" }
   ```
   Response:
   ```json
   { "access_token": "<JWT_TOKEN>" }
   ```

3. **Token Usage:**  
   For protected routes, add header:  
   ```
   Authorization: Bearer <JWT_TOKEN>
   ```

---

## 📚 Route List & Sample Requests

### Register
- **POST /register**
- Request:
  ```json
  { "username": "alice", "password": "password123" }
  ```
- Response:
  ```json
  { "message": "User registered" }
  ```

### Login
- **POST /login**
- Request:
  ```json
  { "username": "alice", "password": "password123" }
  ```
- Response:
  ```json
  { "access_token": "..." }
  ```

### Get All Episodes
- **GET /episodes**
- Response:
  ```json
  [
    { "id": 1, "date": "2024-06-01", "number": 101 }
  ]
  ```

### Get Episode by ID
- **GET /episodes/1**
- Response:
  ```json
  {
    "id": 1,
    "date": "2024-06-01",
    "number": 101,
    "appearances": [
      { "id": 1, "rating": 5, "guest": "John Doe" }
    ]
  }
  ```

### Delete Episode (Protected)
- **DELETE /episodes/1**
- Header: `Authorization: Bearer <JWT_TOKEN>`
- Response:
  ```json
  { "message": "Episode deleted" }
  ```

---

## 🧪 Postman Usage Guide

1. **Import the collection:**  
   - Open Postman, click **Import**, select `challenge-4-lateshow.postman_collection.json`.

2. **Register and login:**  
   - Use the Register and Login requests to get your JWT token.

3. **Set Authorization:**  
   - For protected routes, go to the Authorization tab, select **Bearer Token**, and paste your JWT token.

4. **Send requests:**  
   - Use the provided requests or add your own to test all endpoints.

---

## 🔗 GitHub Repo

[GitHub Repository](<https://github.com/Davidkiki1/late-show-api-challenge>)
