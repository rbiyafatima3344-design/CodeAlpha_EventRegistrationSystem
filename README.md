# 🎟️ Event Registration System

A backend **Event Registration System** built using **Django, Django REST Framework, and PostgreSQL**.

This project was developed as part of the **CodeAlpha Backend Development Internship – Task 2**.

---

## 📌 Project Overview

The Event Registration System provides REST APIs for managing events and user registrations.

Users can:

* 👤 Create an account
* 🔐 Login and receive an authentication token
* 📅 View available events
* 🔎 View event details
* 📝 Register for an event
* 📋 View their registrations
* ❌ Cancel a registration

The project uses **PostgreSQL** as the database and **Django REST Framework** for building APIs.

---

## 🚀 Features

* 👤 User Signup
* 🔐 User Login
* 🎫 Token Authentication
* 📅 Event List API
* 🔎 Event Detail API
* 📝 Event Registration
* 📋 My Registrations
* ❌ Cancel Registration
* 🗄️ PostgreSQL Database
* ⚙️ Django Admin Panel
* 🔧 Django REST Framework APIs

---

## 🛠️ Technologies Used

* 🐍 **Python**
* 🌐 **Django**
* 🔌 **Django REST Framework**
* 🐘 **PostgreSQL**
* 🔑 **Django REST Framework Token Authentication**

---

## 🔗 API Endpoints

| Method   | Endpoint                         | Description                  |
| -------- | -------------------------------- | ---------------------------- |
| `POST`   | `/api/signup/`                   | 👤 Create a new user         |
| `POST`   | `/api/login/`                    | 🔐 Login and generate token  |
| `GET`    | `/api/events/`                   | 📅 Get all events            |
| `GET`    | `/api/events/<id>/`              | 🔎 Get event details         |
| `POST`   | `/api/registration/<id>/`        | 📝 Register for an event     |
| `GET`    | `/api/my-registrations/`         | 📋 View user's registrations |
| `DELETE` | `/api/registration/<id>/cancel/` | ❌ Cancel registration        |

---

## 🗄️ Database

The application uses **PostgreSQL** for data storage.

The database manages:

* 👤 Users
* 📅 Events
* 📝 Registrations
* 🔑 Authentication Tokens

---

## ⚙️ Django Admin

The Django Admin Panel is used to manage:

* 👤 Users
* 📅 Events
* 📝 Registrations

Administrators can add, update, and delete events through the admin panel.

---

## 🧪 API Testing

The APIs were tested using the **Django REST Framework Browsable API**.

The following functionality was successfully tested:

* ✅ User Signup
* ✅ User Login
* ✅ Token Generation
* ✅ Event List
* ✅ Event Detail
* ✅ Event Registration
* ✅ My Registrations
* ✅ Cancel Registration

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sameeha4/CodeAlpha_EventRegistrationSystem.git
```

### 2️⃣ Open the Project

```bash
cd CodeAlpha_EventRegistrationSystem
```

### 3️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

### 7️⃣ Start the Development Server

```bash
python manage.py runserver
```

The project will run at:

```text
http://127.0.0.1:8000/
```

The API endpoints are available under:

```text
http://127.0.0.1:8000/api/
```

---

## 📂 Project Structure

```text
CodeAlpha_EventRegistrationSystem/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── events/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
└── event_registration_system/
    ├── settings.py
    ├── urls.py
    └── ...
```

---

## 🎯 Internship Task

**CodeAlpha Backend Development Internship**

### Task 2 — Event Registration System

The project demonstrates backend development using Django, REST APIs, database management, authentication, and event registration functionality.

---

## 👨‍💻 Author

**Rbiya Fatima**

🔗 GitHub: https://github.com/rbiyafatima3344_design

---

## 🏆 Project Status

**Status: ✅ Completed**

Built with ❤️ using Python, Django REST Framework, and PostgreSQL.
