# 🚀 FastAPI Learning Project

A beginner-friendly **FastAPI CRUD API** built to learn the core concepts of FastAPI using a simple JSON file as the database.

This project covers everything from creating your first API to implementing CRUD operations with request validation using **Pydantic**.

---

## 📚 What You'll Learn

This project demonstrates the following FastAPI concepts:

- ✅ Creating a FastAPI application
- ✅ Path Parameters
- ✅ Query Parameters
- ✅ Request Body Validation
- ✅ Pydantic Models
- ✅ Computed Fields
- ✅ HTTP Status Codes
- ✅ HTTP Exceptions
- ✅ JSON Responses
- ✅ CRUD Operations
- ✅ Reading and Writing JSON Files
- ✅ API Documentation using Swagger UI

---

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic v2
- JSON (used as a lightweight database)

---

## 📂 Project Structure

```
fastapi-learning/
│
├── main.py              # Main FastAPI application
├── people.json          # JSON database
├── requirements.txt     # Project dependencies
├── README.md
└── __pycache__/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Move into the project directory

```bash
cd fastapi-learning
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the Project

Start the server using

```bash
uvicorn main:app --reload
```

The API will run at

```
http://127.0.0.1:8000
```

---

## 📖 Interactive API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## Home

```
GET /
```

Returns a welcome message.

---

## About

```
GET /about
```

Returns information about the project.

---

## Get All People

```
GET /people
```

Returns all people stored in the JSON database.

---

## Get Person by ID

```
GET /person/{person_id}
```

Example

```
GET /person/p1
```

---

## Sort People

```
GET /sort?sortby=age&order=asc
```

Available parameters

| Parameter | Values |
|-----------|---------|
| sortby | age, weight |
| order | asc, desc |

Examples

```
/sort?sortby=age&order=asc

/sort?sortby=weight&order=desc
```

---

## Create Person

```
POST /create
```

Example Request

```json
{
  "id": "p5",
  "name": "John",
  "age": 24,
  "weight": 72,
  "height": 1.75,
  "education": "B.Tech"
}
```

---

## Update Person

```
PUT /update/{id}
```

Only send the fields you want to update.

Example

```json
{
  "weight": 80
}
```

or

```json
{
  "name": "John Doe",
  "age": 25,
  "education": "M.Tech"
}
```

---

## Delete Person

```
DELETE /delete/{id}
```

Example

```
DELETE /delete/p5
```

---

# Request Validation

The project uses **Pydantic v2** for request validation.

Validation includes:

- Positive age
- Positive height
- Positive weight
- Required fields while creating a person
- Optional fields while updating a person

---

# Automatic BMI Calculation

Whenever a person is created or updated, BMI is automatically calculated using a computed field.

Formula:

```
BMI = Weight / Height²
```

The API also returns a health verdict based on BMI.

| BMI | Verdict |
|------|----------|
| <18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25 - 29.9 | Overweight |
| 30+ | Obese |

---

# Error Handling

The project demonstrates proper error handling using `HTTPException`.

Examples include

- Person not found
- Duplicate person ID
- Invalid query parameters
- Validation errors

---

# Learning Objectives

By completing this project, you will understand:

- FastAPI project structure
- CRUD API development
- Request validation
- Query parameters
- Path parameters
- Response models
- HTTP status codes
- JSON as a simple database
- API testing with Swagger UI

---

# Future Improvements

Some ideas to extend this project:

- Authentication with JWT
- SQLite/PostgreSQL integration
- SQLAlchemy ORM
- PATCH endpoint
- Pagination
- Search API
- Filtering
- Docker support
- Unit testing with Pytest
- Logging
- Environment variables
- File uploads
- Deployment using Render/Railway

---

# Contributing

Feel free to fork this repository, improve it, and submit a pull request.

---

# License

This project is created for educational purposes and is free to use and modify.

---

## ⭐ If this project helped you learn FastAPI, consider giving it a star!